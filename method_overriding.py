class Father:
    def drink(self):
        print("Drinks more")
        
class Son(Father):
    def drink(self):
        print("Drinks less")
        
        
objF = Father()
objS = Son()

objF.drink()
objS.drink()