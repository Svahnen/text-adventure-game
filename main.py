# This is where the main program lives

from room import Room
from door import Door

randomDoor = Door()
print(randomDoor.isOpen())
randomDoor.open()
print(randomDoor.isOpen())



def createWorld ():
    rooms = [] # This will be floors in the future that return all possible rooms
    rooms.append(Room("expedition"))
    rooms.append(Room("office"))
    currentRoom = rooms[0]
    while True:
        print("Location: "+ currentRoom.getName())
        currentRoom = walk(rooms)
        print("Location: "+ currentRoom.getName())
        print("-----------------------------------")

def walk(rooms):
    print("The room names are:")
    for room in rooms:
        print(room.getName())
    roomName = input("Where do you want to go? ")
    for room in rooms:
        if roomName == room.getName():
            return room

#createWorld()

