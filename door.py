class Door :
    def __init__(self, name) :
        self.name = name
        #self._lock = lock
        self.currentlyOpen = False
        self.connectedRooms = []

    def open(self) :
        self.currentlyOpen = True

    def close(self) :
        self.currentlyOpen = False

    def isOpen(self) :
        return self.currentlyOpen
    
    def getName(self) : 
        return self.name

    def addConnectedRoom(self, room):
        self.connectedRooms.append(room)

    def getConnectedRooms(self) :
        return self.connectedRooms
        