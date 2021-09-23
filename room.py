from door import Door

class Room :
    def __init__(self, name, doorList : list[Door]) : #Constructor
        self.name = name
        self.doorList = doorList
        self.connectedRooms = []

    def getName(self) :
        return self.name

    def getDoorList(self) :
        return self.doorList

    def addConnectedRoom(self, room):
        self.connectedRooms.append(room)

    def getConnectedRooms(self) :
        return self.connectedRooms