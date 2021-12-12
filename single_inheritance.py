class Father:
    def drinks(self):
        print("He drinks")

class Son(Father):
    def talk(self):
        print("He talks")
        

objS = Son()

objS.drinks()
objS.talk()