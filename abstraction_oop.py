from abc import ABC

class Bird(ABC):
    def canFly(self):
        pass
    

class Parrot(Bird):
    def canFly(self):
        print("Yes")

class Penguin(Bird):
    def canFly(self):
        print("No")
        
        
objParrot = Parrot()
objPenguin = Penguin()

objParrot.canFly()
objPenguin.canFly()