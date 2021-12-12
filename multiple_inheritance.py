class Father:
    def drinks(self):
        print("Drinking")

class Mother:
    def cook(self):
        print("Cooking")

class Son(Father, Mother):
    def talk(self):
        print("Talking")
        

objS = Son()

objS.drinks()
objS.cook()
objS.talk()