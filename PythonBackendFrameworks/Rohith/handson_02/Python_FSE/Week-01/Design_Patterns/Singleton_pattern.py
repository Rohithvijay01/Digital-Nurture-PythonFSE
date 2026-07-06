from enum import Enum
 class Singleton(enum):
    instance = 1

    def showuser(self)-> None:
        print("This is a singleton class")



 def main():
    Singleton.instance.showeuser()

if __name__ == "__main__":
    main()
