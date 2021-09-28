class Door :
    def __init__(self, name) :
        self.name = name
        self.currentlyOpen = False
        self.lock = None

    def open(self) :
        if self.lock == None : # See if there is a lock
            self.currentlyOpen = True
            return self.currentlyOpen
        else : # If there is a lock, see if its unlocked
            if not self.lock.isLocked() :
                self.currentlyOpen = True
                return self.currentlyOpen
            else :
                return self.currentlyOpen

    def close(self) :
        self.currentlyOpen = False

    def isOpen(self) :
        return self.currentlyOpen
    
    def getName(self) : 
        return self.name
    
    def setLock(self, lock) : 
        self.lock = lock
        