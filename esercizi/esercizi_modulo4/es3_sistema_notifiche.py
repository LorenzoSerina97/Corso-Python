"""
Esercizio 3: Sistema di Notifiche
Modulo 4 - Laboratorio Pratico

Obiettivo: Creare un sistema di notifiche usando classi astratte e polimorfismo.
- Classe astratta Notificatore con metodo astratto invia()
- Implementazioni concrete: Email, SMS, Push, Webhook
- Dimostrazione del polimorfismo
"""

from abc import ABC, abstractmethod
from datetime import datetime


class Notificatore(ABC):
    """Classe astratta base per tutti i notificatori."""
    
    def __init__(self, nome):
        self.nome = nome
        self.messaggi_inviati = 0
    
    @abstractmethod
    def invia(self, messaggio):
        """
        Invia un messaggio.
        
        Args:
            messaggio: Il messaggio da inviare
        """
        pass
    
    def log(self, destinatario, messaggio):
        """Registra l'invio di un messaggio."""
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] {self.nome} → {destinatario}: {messaggio}")
        self.messaggi_inviati += 1
    
    def statistiche(self):
        """Restituisce le statistiche di invio."""
        return f"{self.nome}: {self.messaggi_inviati} messaggi inviati"


class EmailNotificatore(Notificatore):
    """Notificatore via email."""
    
    def __init__(self, email, smtp_server="smtp.example.com"):
        super().__init__("Email")
        self.email = email
        self.smtp_server = smtp_server
    
    def invia(self, messaggio):
        """Invia una email."""
        self.log(self.email, messaggio)
        print(f"  📧 [Simulato] Email inviata via {self.smtp_server}")
    
    def invia_con_allegato(self, messaggio, allegato):
        """Invia email con allegato."""
        self.log(self.email, f"{messaggio} [Allegato: {allegato}]")
        print(f"  📧 [Simulato] Email con allegato inviata")


class SMSNotificatore(Notificatore):
    """Notificatore via SMS."""
    
    def __init__(self, telefono):
        super().__init__("SMS")
        self.telefono = telefono
    
    def invia(self, messaggio):
        """Invia un SMS."""
        # Tronca il messaggio se troppo lungo
        messaggio_breve = messaggio[:160] if len(messaggio) > 160 else messaggio
        self.log(self.telefono, messaggio_breve)
        print(f"  📱 [Simulato] SMS inviato ({len(messaggio_breve)} caratteri)")


class PushNotificatore(Notificatore):
    """Notificatore via push notification."""
    
    def __init__(self, device_id, app_name="MyApp"):
        super().__init__("Push")
        self.device_id = device_id
        self.app_name = app_name
    
    def invia(self, messaggio):
        """Invia una notifica push."""
        self.log(f"Device:{self.device_id[:8]}...", messaggio)
        print(f"  🔔 [Simulato] Push inviata tramite {self.app_name}")


class WebhookNotificatore(Notificatore):
    """Notificatore via webhook (es. Slack, Discord)."""
    
    def __init__(self, url, servizio="Webhook"):
        super().__init__(servizio)
        self.url = url
    
    def invia(self, messaggio):
        """Invia un messaggio via webhook."""
        self.log(self.url[:30] + "...", messaggio)
        print(f"  🌐 [Simulato] POST request inviata")


class SlackNotificatore(WebhookNotificatore):
    """Notificatore specifico per Slack."""
    
    def __init__(self, webhook_url, canale="#general"):
        super().__init__(webhook_url, "Slack")
        self.canale = canale
    
    def invia(self, messaggio):
        """Invia un messaggio su Slack."""
        self.log(self.canale, messaggio)
        print(f"  💬 [Simulato] Messaggio Slack inviato")


class GestoreNotifiche:
    """Gestisce multiple modalità di notifica."""
    
    def __init__(self):
        self.notificatori = []
    
    def aggiungi(self, notificatore):
        """Aggiunge un notificatore."""
        self.notificatori.append(notificatore)
        print(f"✓ Aggiunto notificatore: {notificatore.nome}")
    
    def notifica_tutti(self, messaggio):
        """Invia il messaggio attraverso tutti i notificatori."""
        print(f"\n📢 Invio messaggio a {len(self.notificatori)} canali...")
        print("-" * 40)
        for notificatore in self.notificatori:
            notificatore.invia(messaggio)
        print("-" * 40)
    
    def statistiche(self):
        """Mostra le statistiche di tutti i notificatori."""
        print("\n📊 Statistiche:")
        for n in self.notificatori:
            print(f"  • {n.statistiche()}")


# ==================== TEST ====================
if __name__ == "__main__":
    print("=" * 50)
    print("TEST SISTEMA DI NOTIFICHE")
    print("=" * 50)
    
    # Creazione notificatori
    email = EmailNotificatore("utente@example.com")
    sms = SMSNotificatore("+39 333 1234567")
    push = PushNotificatore("abc123def456ghi789")
    slack = SlackNotificatore("https://hooks.slack.com/services/xxx", "#alerts")
    
    # Test singolo notificatore
    print("\n--- Test Singoli Notificatori ---")
    email.invia("Benvenuto nel sistema!")
    sms.invia("Il tuo codice OTP è: 123456")
    push.invia("Hai un nuovo messaggio")
    slack.invia("Deploy completato con successo")
    
    # Test email con allegato
    print("\n--- Test Email con Allegato ---")
    email.invia_con_allegato("Ecco il report mensile", "report.pdf")
    
    # Test polimorfismo con lista
    print("\n--- Test Polimorfismo ---")
    notificatori = [email, sms, push, slack]
    messaggio = "⚠️ Manutenzione programmata alle 02:00"
    
    for n in notificatori:
        n.invia(messaggio)
    
    # Test GestoreNotifiche
    print("\n--- Test GestoreNotifiche ---")
    gestore = GestoreNotifiche()
    gestore.aggiungi(EmailNotificatore("admin@example.com"))
    gestore.aggiungi(SMSNotificatore("+39 333 9876543"))
    gestore.aggiungi(SlackNotificatore("https://hooks.slack.com/xxx", "#devops"))
    
    gestore.notifica_tutti("🚀 Nuovo rilascio v2.0 disponibile!")
    gestore.statistiche()
    
    print("\n✅ Tutti i test completati con successo!")
