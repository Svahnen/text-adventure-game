# This is where the main program lives

from room import Room
from door import Door



def createWorld ():
    rooms = [] # This will be floors in the future that return all possible rooms
    expeditionDoor = Door("expedition")
    officeDoor = Door("office")
    rooms.append(Room("corridor",[expeditionDoor, officeDoor]))
    rooms.append(Room("expedition", [expeditionDoor]))
    rooms.append(Room("office", [officeDoor]))
    rooms[0].addConnectedRoom(rooms[1]) # corridor A leads to office
    rooms[0].addConnectedRoom(rooms[2]) # corridor A leads to expedition
    rooms[1].addConnectedRoom(rooms[0]) # expedition leads to corridor A
    rooms[2].addConnectedRoom(rooms[0]) # office leads to corridor A
    action(rooms)
    



def walk(rooms,currentRoom):
    print("These are the options")
    connectedRooms = currentRoom.getConnectedRooms()
    for room in connectedRooms :
        print(room.getName())
    userInput = input("Where do you want to go: ")
    for index in range(len(rooms)) :
        if rooms[index].getName() == userInput :
            for door in currentRoom.getDoorList() :
                if door.getName() == userInput :
                    if door.isOpen():
                        return rooms[index]
                    else:
                        print("-------------------------------")
                        print("The door is closed")
                        return currentRoom
# When you in office, you can't go back to Corridor because there is no check which door we want to go to.





def doorAction(currentRoom):
    print("-------------------------------")
    print("These are the following door(s)")
    potentialDoors = currentRoom.getDoorList()
    for door in potentialDoors:
        if door.isOpen():
            print(door.getName() + " open")
        else:
            print(door.getName() + " closed")

    print("1. open ")
    print("2. close ")
    print("3. cancel ")
    try:
        actionInput = int(input("What do you want to do? "))
        if actionInput == 1 :
            userInput = input("Which door do you want to open: ")
            for index in range(len(potentialDoors)) :
                if potentialDoors[index].getName() == userInput :
                    potentialDoors[index].open()
                    print("-------------------------------")
                    print("You have now opened the door", potentialDoors[index].getName())
        elif actionInput == 2 :
            userInput = input("Which door do you want to close: ")
            for index in range(len(potentialDoors)) :
                if potentialDoors[index].getName() == userInput :
                    potentialDoors[index].close()
                    print("-------------------------------")
                    print("You have now closed the door", potentialDoors[index].getName())
        elif actionInput == 3 :
            return
    except ValueError:
        print("You need to enter a number!")

    

def action(rooms):
    currentRoom = rooms[0]
    while True:
        print("-------------------------------")
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