from door import Door
from floor import Floor

class Room(Floor) :
    def __init__(self, name, doorList : list[Door]) : #Constructor
        super().__init__()
        self.name = name
        self.doorList = doorList
        self.connectedRooms = []
        self.items = []

    def getName(self) :
        return self.name

    def getDoorList(self) :
        return self.doorList

    def addConnectedRoom(self, room):
        self.connectedRooms.append(room)

    def getConnectedRooms(self) :
        return self.connectedRooms

    def setDescription(self, description) : # Override parent
        self.description = description
    
    def getDescription(self) :
        return self.description

    def addItem(self, item) :
        self.items.append(item)

    def getItems(self) :
        return self.items

    def removeItem(self, item) :
        self.items.remove(item)