class Door :
    def __init__(self, name) :
        self.name = name
        self.currentlyOpen = False

    def open(self) :
        self.currentlyOpen = True

    def close(self) :
        self.currentlyOpen = False

    def isOpen(self) :
        return self.currentlyOpen
    
    def getName(self) : 
        return self.name
        