class Main:
    def greet(self, name=None):
        
        if name is not None:
            print("Hello",name)
        else:
            print("Hello")
            
obj = Main()


obj.greet()
obj.greet("Shayan")