from abc import ABC, abtractmethod

class UsbPowerSocket(ABC):
    @abtractmethod
    def connect_flat(self) -> str:
        pass

class IndianCharger:
    def plug_roundpin(self) -> str: 
        return "Charging with round pin charger"  

class  Adapter(UsbPowerSocket):
    def __init__(self, charger : IndianCharger):
        self.charger = charger

    def connect_flat(self) -> str:
        return self.charger.plug_roundpin()

my charger = IndianCharger()
hotel_socket = Adapter(charger)

print(hotel_socket.connect_flat())

