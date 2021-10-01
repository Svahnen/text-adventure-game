# This is where the main program lives
from item import Item
from room import Room
from door import Door
from lock import Lock


def createWorld ():
    rooms = [] # This will be floors in the future that return all possible rooms

    # Create items
    masterKey = Item("Office Key")

    # Create all locks
    officeLock = Lock(masterKey, True)
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
    expeditionRoom.setDescription("You are in the expedition room, you see a note on the wall with the numbers 987 and a key on a desk")
    
    # Append the rooms into the rooms list
    rooms.append(corridorRoom)
    rooms.append(expeditionRoom)
    rooms.append(officeRoom)

    action(rooms)


def compareRoomDoors(currentRoom, nextRoom) :
    for doorInNextRoom in nextRoom.getDoorList() :
        for doorInCurrentRoom in currentRoom.getDoorList() :
            if doorInNextRoom == doorInCurrentRoom :
                if doorInCurrentRoom.isOpen():
                    return nextRoom # Return the new room so it can update currentRoom
                else:
                    print("-------------------------------")
                    print("The door is closed")
                    return currentRoom

def walk(currentRoom):
    print("These are the options")
    connectedRooms = currentRoom.getConnectedRooms()
    for room in connectedRooms :
        print(room.getName())
    userInput = input("Where do you want to go: ")
    userInput = userInput.lower()
    connectedRoomFound = False
    for room in connectedRooms :
        if room.getName() == userInput :
            connectedRoomFound = True
            if compareRoomDoors(currentRoom, room):
                return room # If rooms have a matching door return the next room
    if not connectedRoomFound :
        print("-------------------------------")
        print("There is no room with that name")
        return currentRoom # If user typed a room name that did not exist, return currentRoom


def openDoor(potentialDoors, inventory) :
    doorFound = False
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
                # TODO: Try to unlock the door if key is in inventory
                for item in inventory :
                    if potentialDoors[index].lock.unlock(item) :
                        print("You have used a key from your inventory")
                        potentialDoors[index].open()
            doorFound = True
        elif potentialDoors[index].getName() == userInput :
            print("The door is already open.")
            doorFound = True
    if not doorFound : # if doorFound == False: same same
        print("There is no door with that name")


def closeDoor(potentialDoors):
    doorFound = False
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


def doorAction(currentRoom, inventory):
    print("-------------------------------")
    print("These are the following door(s)")
    potentialDoors = currentRoom.getDoorList()
    for door in potentialDoors :
        if door.isOpen() :
            print(door.getName() + " open")
        else :
            print(door.getName() + " closed")
    print("1. open ")
    print("2. close ")
    print("9. cancel ")
    try:
        actionInput = int(input("What do you want to do? "))
        if actionInput == 1 :
            openDoor(potentialDoors, inventory)
        elif actionInput == 2 :
            closeDoor(potentialDoors)
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


def pickUpItem(room, inventory) :
    itemList = room.getItems()
    for item in itemList:
        print(item.getName())
    itemFound = False
    userInput = input("What item do you want to pick up? ")
    for item in itemList:
        if userInput.lower() == item.getName().lower() :
            print("You have picked up:", item.getName())
            itemFound = True
            inventory.append(item)
            room.removeItem(item)
    if not itemFound :
        print("There is no item with that name")


def startGame():
    print("The final study year is almost over.")
    print("You have unfortunately failed your last")
    print("exam and your mission is now to brake into")
    print("the principals office and change your degree... ")
    print("-------------------------------")
    input("Press enter to start")


def action(rooms):
    running = True
    currentRoom = rooms[0]
    inventory = []
    startGame()
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
                pickUpItem(currentRoom, inventory)
            elif action == 9 :
                print("Try to find a better game loser!")
                running = False
            else:
                print("There is no action with that number")
        except ValueError:
            print("You need to enter a number!")


createWorld()