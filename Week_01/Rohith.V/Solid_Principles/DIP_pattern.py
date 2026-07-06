from abc import ABC, abstractmethod

class NotificationService(ABC):
    @abstractmethod
    def send_notification(self, message: str, recipient: str):
        pass

class EmailSender(NotificationService):
    def send_notification(self, message: str, recipient: str):
        print(f"Sending Email to {recipient}: {message}")

class SMSSender(NotificationService):
    def send_notification(self, message: str, recipient: str):
        print(f"Sending SMS to {recipient}: {message}")

class NotificationManager:
    def __init__(self, service: NotificationService):
        #  Depends completely on the abstraction interface, not concrete classes
        self.service = service

    def send(self, message: str, recipient: str):
        self.service.send_notification(message, recipient)


if __name__ == "__main__":
    # We can inject Email service
    email_service = EmailSender()
    app_with_email = NotificationManager(service=email_service)
    app_with_email.send("Hello via Email!", "user@domain.com")

    sms_service = SMSSender()
    app_with_sms = NotificationManager(service=sms_service)
    app_with_sms.send("Hello via SMS!", "+123456789")