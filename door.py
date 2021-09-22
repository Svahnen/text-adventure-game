class Door :
    def __init__(self) :
        #self._lock = lock
        self.currentlyOpen = False

    def open(self) :
        self.currentlyOpen = True

    def close(self) :
        self.currentlyOpen = False

    def isOpen(self) :
        return self.currentlyOpen