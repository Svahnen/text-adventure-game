# This is where the main program lives

from room import Room
from door import Door


def createWorld ():
    rooms = [] # This will be floors in the future that return all possible rooms
    rooms.append(Room("corridor A"))
    rooms.append(Room("expedition"))
    action(rooms)

def walk(rooms,currentRoom):
    print(currentRoom.getName())
    print("The room names are:")
    for room in rooms:
        print(room.getName())
    roomName = input("Where do you want to go? ")
    for room in rooms:
        if roomName == room.getName():
            return room

def action(rooms):
    currentRoom = rooms[0]
    while True:
        print("What do you want to do?")
        print("1. Walk")
        try:
            action = int(input())
            if action == 1 :
                currentRoom = walk(rooms, currentRoom)
        except ValueError:
            print("You need to enter a number!")
            

createWorld()

