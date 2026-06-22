from abc import ABC , abtractmethod

class Bird(ABC):
    @abtractmethod
    def sound(self) -> None:
        pass

class FlyingBird(ABC):
    @abtractmethod
    def fly(self) -> None:
        pass


class Sparrow(FlyingBird , Bird):
    def sound(self) -> None:
        print("Sparrow sound: Chirp chirp")

    def fly(self) -> None:
        print("Sparrow is flying")


class Penguin(Bird):
    def sound(self) -> None:
        print("Penguin sound: Honk honk")   



def main():
    sparrow = Sparrow()
    penguin = Penguin()

    sparrow.sound()
      

    penguin.sound()  

    flying_bird : FlyingBird = Sparrow()
    flying_bird.fly()          