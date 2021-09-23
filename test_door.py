from door import Door

testDoor = Door("office") # Creates a door under the variable testDoor
print(testDoor.isOpen())
testDoor.open()
print(testDoor.isOpen())
print(testDoor.getName()) # 'getter/getName will return the name of the door.
  