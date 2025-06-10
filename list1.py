class car:
    def __init__(self,name,colour):
        self.name=name
        self.colour=colour

    def intro(self):
        print("my car is", self.name,self.colour)
bmw=car("bmw","red")
bmw.intro()
indigo=car("indigo","blue")
indigo.intro()