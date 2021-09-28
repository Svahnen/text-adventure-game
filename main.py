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

    # Add descriptions to the rooms
    officeRoom.setDescription("You are standing in an office and you see a computer on the desk")
    corridorRoom.setDescription("You are standing in the corridor")
    expeditionRoom.setDescription("You are in the expedition room, you see a postit note on the wall with the numbers: 987")
    
    # Append the rooms into the rooms list
    rooms.append(corridorRoom)
    rooms.append(expeditionRoom)
    rooms.append(officeRoom)

    action(rooms)


def walk(currentRoom):
    print("These are the options")
    connectedRooms = currentRoom.getConnectedRooms()
    for room in connectedRooms :
        print(room.getName())
    userInput = input("Where do you want to go: ")
    userInput = userInput.lower()
    for index in range(len(connectedRooms)) :
        if connectedRooms[index].getName() == userInput :
            try: # See is the door list in current room and next room have a matching door
                for doorInNextRoom in connectedRooms[index].getDoorList() :
                    for doorInCurrentRoom in currentRoom.getDoorList() :
                        if doorInNextRoom == doorInCurrentRoom :
                            if doorInCurrentRoom.isOpen():
                                return connectedRooms[index] # Return the new room so it can update currentRoom
                            else:
                                print("-------------------------------")
                                print("The door is closed")
                                return currentRoom
            except:
                # The next room probably have no doors
                return connectedRooms[index]
        else:
            print("-------------------------------")
            print("There is no room with that name")
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
            userInput = userInput.lower()
            for index in range(len(potentialDoors)) :
                if potentialDoors[index].getName() == userInput :
                    potentialDoors[index].open()
                    print("-------------------------------")
                    print("You have now opened the door", potentialDoors[index].getName())
                else :
                    print("There is no door with that name")
        elif actionInput == 2 :
            userInput = input("Which door do you want to close: ")
            userInput = userInput.lower()
            for index in range(len(potentialDoors)) :
                if potentialDoors[index].getName() == userInput :
                    potentialDoors[index].close()
                    print("-------------------------------")
                    print("You have now closed the door", potentialDoors[index].getName())
                else :
                    print("There is no door with that name")
        elif actionInput == 3 :
            return
        else :
            print("There is no action with that number")
    except ValueError:
        print("You need to enter a number!")

def useComputer():
    userPass = input("Enter password: ")
    if userPass == "987" :
        print("You have changed your grades and completed the game!")
        return False
    else :
        print("You entered the wrong password! Try to find the password somewhere in the building")
        return True


def action(rooms):
    running = True
    currentRoom = rooms[0]
    while running:
        print("-------------------------------")
        print("***** " + currentRoom.getName() + " *****")
        print(currentRoom.getDescription())
        print("-------------------------------")
        print("What do you want to do?")
        print("1. Walk")
        print("2. Look for doors")
        if currentRoom.getName() == "office":
            print("3. Use the computer")
        print("9. Quit game")
        try:
            action = int(input())
            if action == 1 :
                currentRoom = walk(currentRoom)
            elif action == 2 :
                doorAction(currentRoom)
            elif currentRoom.getName() == "office" and action == 3 :
                running = useComputer()
            elif action == 9 :
                print("Try to find a better game loser!")
                running = False
            else:
                print("There is no action with that number")
        except ValueError:
            print("You need to enter a number!")


createWorld()