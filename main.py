# This is where the main program lives
import random # Library in python that we use in row 18
from item import Item
from room import Room
from door import Door
from lock import Lock
from database import readDatabase, writeToDatabase



def createWorld ():
    rooms = [] # This will be floors in the future that return all possible rooms

    # Create items
    masterKey = Item("Office Key")

    # Set password for the computer
    pcPass = str(random.randint(100,999)) # Generate a number between 100-999 and convert them to a string

    # Create all locks
    officeLock = Lock(masterKey, True) # Create lock for office using masterKey and set lock to initially unlocked
    expeditionLock = Lock(masterKey, False) # Create lock for office using masterKey and set lock to initially locked

    # Create all doors
    expeditionDoor = Door("expedition", expeditionLock) # Create door, set door name and set the right doorlock to the right door
    officeDoor = Door("office", officeLock) 

    # Create all rooms
    corridorRoom = Room("corridor",[expeditionDoor, officeDoor]) # Create room and set their connected doors
    expeditionRoom = Room("expedition", [expeditionDoor])
    officeRoom = Room("office", [officeDoor])

    # Add items to rooms
    expeditionRoom.addItem(masterKey)
    #expeditionRoom.addItem(ball) this is how you add another item

    # Connect rooms together
    corridorRoom.addConnectedRoom(expeditionRoom) # corridor leads to expedition
    corridorRoom.addConnectedRoom(officeRoom) # corridor leads to office
    expeditionRoom.addConnectedRoom(corridorRoom) # expedition leads to corridor
    officeRoom.addConnectedRoom(corridorRoom) # office leads to corridor

    # Add descriptions to the rooms
    officeRoom.setDescription("You are standing in an office and you see a computer on the desk")
    corridorRoom.setDescription("You are standing in the corridor")
    expeditionRoom.setDescription("You are in the expedition room, you see a note on the wall with the numbers " + pcPass + " and a key on a desk")
    
    # Append the rooms into the rooms list
    rooms.append(corridorRoom)
    rooms.append(expeditionRoom)
    rooms.append(officeRoom)
    
    action(rooms, pcPass) # Run the actual program



def isDoorOpenBetween(currentRoom, nextRoom) : # isDoorOpenBetween checks if there's a open door in between the rooms
    for doorInNextRoom in nextRoom.getDoorList() :
        for doorInCurrentRoom in currentRoom.getDoorList() :
            if doorInNextRoom == doorInCurrentRoom :
                if doorInCurrentRoom.isOpen():
                    return True # Both rooms have the door and it's open
                else:
                    return False


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
            if isDoorOpenBetween(currentRoom, room):
                return room # Rooms have a matching open door, return the next room
            else:
                print("-------------------------------")
                print("The door is closed")
                return currentRoom
    if not connectedRoomFound :
        print("-------------------------------")
        print("There is no room with that name")
        return currentRoom


def unlockDoor(inventory, door):
    for item in inventory :
        if door.lock.unlock(item) :
            print("You have used a key from your inventory")


def openDoor(potentialDoors, inventory) :
    doorFound = False
    userInput = input("Which door do you want to open: ")
    userInput = userInput.lower()
    for index in range(len(potentialDoors)) :
        if potentialDoors[index].getName() == userInput : 
            if potentialDoors[index].open():
                print("-------------------------------")
                print(potentialDoors[index].getName(), "door is open")
            else:
                print("The door is locked")
                unlockDoor(inventory,potentialDoors[index])
                potentialDoors[index].open()
            doorFound = True # sets only if the door is found in the list
    if not doorFound : # if doorFound == False: same same
        print("There is no door with that name")


def closeDoor(potentialDoors):
    doorFound = False
    userInput = input("Which door do you want to close: ")
    userInput = userInput.lower()
    for index in range(len(potentialDoors)) :
        if potentialDoors[index].getName() == userInput : 
            potentialDoors[index].close()
            print("-------------------------------")
            print(potentialDoors[index].getName(), "door is closed")
            doorFound = True
    if not doorFound : 
        print("There is no door with that name")


def doorAction(currentRoom, inventory): # Inventory is only here so we can pass it on to openDoor
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
            closeDoor(potentialDoors) # Does not need to check if there's a key
        elif actionInput == 3 :
            print("Key menu used")
            return
        elif actionInput == 9 :
            return
        else :
            print("There is no action with that number")
    except ValueError:
        print("You need to enter a number!")


def useComputer(pcPass):
    userPass = input("Enter password: ")
    if userPass == pcPass :
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


def startMessage(rooms, inventory):
    while True:
        print("The final study year is almost over.")
        print("You have unfortunately failed your last")
        print("exam and your mission is now to brake into")
        print("the principals office and change your degree... ")
        print("-------------------------------")
        print("1. Start a new game")
        print("2. Load items from previous game")
        try:
            action = int(input())
            if action == 1 :
                return []
            elif action == 2 :
                return loadGame(rooms, inventory)
            else:
                print("-------------------------------")
                print("There is no action with that number")
                print("-------------------------------")
        except ValueError:
            print("-------------------------------")
            print("You need to enter a number!")
            print("-------------------------------")


def saveGame(inventory):
    saveList = []
    for item in inventory:
        saveList.append(item.getName())
    writeToDatabase(saveList)


def loadGame(rooms, inventory):
    items = readDatabase()
    itemsFound = False
    for room in rooms:
        for item in room.getItems():
            for itemName in items:
                if itemName.lower() == item.getName().lower() :
                    inventory.append(item)
                    room.removeItem(item)
                    itemsFound = True
    if not itemsFound:
        print("-------------------------------")
        print("There was no items to load")


def action(rooms, pcPass):
    running = True
    currentRoom = rooms[0]
    inventory = []
    startMessage(rooms, inventory)
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
                running = useComputer(pcPass)
            elif not currentRoom.getItems() == [] and action == 7 :
                pickUpItem(currentRoom, inventory)
            elif action == 9 :
                print("Try to find a better game loser!")
                running = False
                saveGame(inventory)
            else:
                print("There is no action with that number")
        except ValueError:
            print("You need to enter a number!")


createWorld()