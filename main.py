# This is where the main program lives

from room import Room
from door import Door


def createWorld ():
    rooms = [] # This will be floors in the future that return all possible rooms
    expeditionDoor = Door("expedition")
    officeDoor = Door("office")
    rooms.append(Room("corridor A",[expeditionDoor, officeDoor]))
    rooms.append(Room("expedition", [expeditionDoor]))
    rooms.append(Room("office", [officeDoor]))
    action(rooms)

def walk(rooms,currentRoom):
    print("These are the following door(s)")
    potentialDoors = currentRoom.getDoorList()
    for door in potentialDoors:
        print(door.getName())
    userInput = input("Where do you want to go: ")
    for index in range(len(rooms)) :
        if rooms[index].getName() == userInput :
             return rooms[index]
        
def doorAction(currentRoom):
    print("These are the following door(s)")
    potentialDoors = currentRoom.getDoorList()
    for door in potentialDoors:
        print(door.getName())
    userInput = input("Which door do you want to open: ")
    for index in range(len(potentialDoors)) :
        if potentialDoors[index].getName() == userInput :
             potentialDoors[index].open()

def action(rooms):
    currentRoom = rooms[0]
    while True:
        print("You are currently in " + currentRoom.getName())
        print("What do you want to do?")
        print("1. Walk")
        print("2. Look for doors")
        try:
            action = int(input())
            if action == 1 :
                currentRoom = walk(rooms, currentRoom)
            elif action == 2 :
                doorAction(currentRoom)
        except ValueError:
            print("You need to enter a number!")
            

createWorld()