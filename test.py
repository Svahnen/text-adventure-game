from room import Room
from door import Door
import sys, inspect



rooms = [] # This will be floors in the future that return all possible rooms
expeditionDoor = Door("expedition")
officeDoor = Door("office")
rooms.append(Room("corridor A",[expeditionDoor, officeDoor]))
rooms.append(Room("expedition", [expeditionDoor]))
rooms.append(Room("office", [officeDoor]))


print(officeDoor.__annotations__)