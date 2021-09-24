# This is where the main program lives

from room import Room
from door import Door



def createWorld ():
    rooms = [] # This will be floors in the future that return all possible rooms

    # Create all doors
    expeditionDoor = Door("expedition")
    officeDoor = Door("office")

    # Create all rooms
    corridorRoom = Room("corridor",[expeditionDoor, officeDoor])
    expeditionRoom = Room("expedition", [expeditionDoor])
    officeRoom = Room("office", [officeDoor])

    # Connect rooms together
    corridorRoom.addConnectedRoom(officeRoom) # corridor A leads to office
    corridorRoom.addConnectedRoom(expeditionRoom) # corridor A leads to expedition
    expeditionRoom.addConnectedRoom(corridorRoom) # expedition leads to corridor
    officeRoom.addConnectedRoom(corridorRoom) # office leads to corridor

    # Append the rooms into the rooms list
    rooms.append(corridorRoom)
    rooms.append(expeditionRoom)
    rooms.append(officeRoom)

    action(rooms)
    


def walk(currentRoom):
    print("These are the options")
    connectedRooms = currentRoom.getConnectedRooms() # The beginning of the fix
    for room in connectedRooms :
        print(room.getName())
    userInput = input("Where do you want to go: ")
    for index in range(len(connectedRooms)) :
        if connectedRooms[index].getName() == userInput :
            for doorInNextRoom in connectedRooms[index].getDoorList() :
                for doorInCurrentRoom in currentRoom.getDoorList() :
                    if doorInNextRoom == doorInCurrentRoom :
                        if doorInCurrentRoom.isOpen():
                            return connectedRooms[index] # Return the new room so it can update currentRoom
                        else:
                            print("-------------------------------")
                            print("The door is closed")
                            return currentRoom


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
                currentRoom = walk(currentRoom)
            elif action == 2 :
                doorAction(currentRoom)
        except ValueError:
            print("You need to enter a number!")
            

createWorld()