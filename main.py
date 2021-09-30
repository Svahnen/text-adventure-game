# This is where the main program lives

from room import Room
from door import Door
from lock import Lock


def createWorld ():
    rooms = [] # This will be floors in the future that return all possible rooms

    # Keys
    masterKey = 123

    # Create all locks
    officeLock = Lock(masterKey, False) # TODO: set lock to be True (initially locked)
    expeditionLock = Lock(masterKey, False)

    # Create all doors
    expeditionDoor = Door("expedition", expeditionLock)
    officeDoor = Door("office", officeLock)

    # Create all rooms
    corridorRoom = Room("corridor",[expeditionDoor, officeDoor])
    expeditionRoom = Room("expedition", [expeditionDoor])
    officeRoom = Room("office", [officeDoor])

    # Add items to rooms
    expeditionRoom.addItem(masterKey)

    # Connect rooms together
    corridorRoom.addConnectedRoom(expeditionRoom) # corridor A leads to expedition
    corridorRoom.addConnectedRoom(officeRoom) # corridor A leads to office
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
    connectedRoomFound = False
    for room in connectedRooms :
        print("57")
        print("58", room.getName())
        if room.getName() == userInput :
            connectedRoomFound = True
            print("60")
            try: # See is the door list in current room and next room have a matching door
                for doorInNextRoom in room.getDoorList() :
                    for doorInCurrentRoom in currentRoom.getDoorList() :
                        if doorInNextRoom == doorInCurrentRoom :
                            if doorInCurrentRoom.isOpen():
                                return room # Return the new room so it can update currentRoom
                            else:
                                print("-------------------------------")
                                print("The door is closed")
                                return currentRoom
            except:
                # The next room probably have no doors
                return room
    if not connectedRoomFound :
        print("-------------------------------")
        print("There is no room with that name")
        return currentRoom


# TODO: Move open and close to separate functions
# TODO: Add automatic unlock if player have key in inventory
def doorAction(currentRoom, inventory):
    doorFound = False
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
    if not inventory == [] :
        print("3. Use keytag")
    print("9. cancel ")
    try:
        actionInput = int(input("What do you want to do? "))
        if actionInput == 1 :
            userInput = input("Which door do you want to open: ")
            userInput = userInput.lower()
            for index in range(len(potentialDoors)) :
                if potentialDoors[index].getName() == userInput and potentialDoors[index].isOpen() == False :
                    if not potentialDoors[index].lock.isLocked() :
                        potentialDoors[index].open()
                        print("-------------------------------")
                        print("You have now opened the door", potentialDoors[index].getName())
                    else:
                        print("The door is locked")
                    doorFound = True
                elif potentialDoors[index].getName() == userInput :
                    print("The door is already open.")
                    doorFound = True
            if not doorFound : # if doorFound == False: same same
                print("There is no door with that name")
        elif actionInput == 2 :
            userInput = input("Which door do you want to close: ")
            userInput = userInput.lower()
            for index in range(len(potentialDoors)) :
                if potentialDoors[index].getName() == userInput and potentialDoors[index].isOpen(): 
                    potentialDoors[index].close()
                    print("-------------------------------")
                    print("You have now closed the door", potentialDoors[index].getName())
                    doorFound = True
                elif potentialDoors[index].getName() == userInput :
                    print("The door is already closed")
                    doorFound = True
            if not doorFound : 
                print("There is no door with that name")
        elif actionInput == 3 :
            print("Key menu used")
            return
        elif actionInput == 9 :
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

# TODO: implement this
def pickUpItem(room) :
    item = None # Will be an item from room.getItems()
    # TODO: Loop through items in "room" and let user type name of item to pick up
    print("You have now picked up item", item)
    return item


def action(rooms):
    running = True
    currentRoom = rooms[0]
    inventory = []
    print("this is a test:",currentRoom.getItems())
    while running:
        print("-------------------------------")
        print("***** " + currentRoom.getName() + " *****")
        print(currentRoom.getDescription())
        print("-------------------------------")
        print("What do you want to do?")
        print("1. Walk")
        print("2. Look for doors")
        if not currentRoom.getItems() == []: 
            print("7. Pick up an item")
        if currentRoom.getName() == "office":
            print("3. Use the computer")
        print("9. Quit game")
        try:
            action = int(input())
            if action == 1 :
                currentRoom = walk(currentRoom)
            elif action == 2 :
                doorAction(currentRoom, inventory)
            elif currentRoom.getName() == "office" and action == 3 :
                running = useComputer()
            elif not currentRoom.getItems() == [] and action == 7 :
                inventory.append(pickUpItem(currentRoom))
            elif action == 9 :
                print("Try to find a better game loser!")
                running = False
            else:
                print("There is no action with that number")
        except ValueError:
            print("You need to enter a number!")


createWorld()