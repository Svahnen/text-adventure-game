## A text adventure
This game is a Demo built to be able to expand and include more rooms, floors and pussels.
You play as a student that have failed his/her grades.
The mission is to break into the office that holds your grades and change them.


## Project info:
Morning standup meetings on every project day, 9:00.


## Backlog

### Epics
- Be able to move between rooms: Done
- Pick up items: Done
- Interact with a map
- Player inventory, keys, laxatives
    - Use key automatically when opening a door: Done
    - Use laxative in teachers coffee
- Login computer and change grades
    - Find computer login in expedition: Done
    - Use login on computer: Done
- NPC teacher that moves around and needs to be avoided
- Laxative timer

### Tasks:
1. Create a room class: Done
2. Build one floor and 2 rooms: Done
3. Add a door between the rooms: Done
4. Build a Look function that looks for doors that can be opened or closed
    - Open function: Done
    - Close function: Done
5. Add description to the rooms, for example: "You are standing in a corridor and you see two doors": Done
6. Add a lock class that can be added to the doors, display locked message if locked
    - Lock class: Done
    - Message: Done
7. Manage strings so the player can type both Office and office: Done
8. Show extra menu item if room have items, menu "Pick up": Done
9. Implement pickUp function: Done
10. When using "open" look through inventory and use key automatically if found: Done
11. Add doors to the rooms with a class function instead. Would make it possible to create rooms without doors.
12. Implement random computer password: Done
13. Add a floor class that is a parent to room: Done


## Bugs:
1. In office menu, put quit game under "Use the computer": Fixed
2. When choosing the option to close/open a door that's already closed/open. It says that I have closed the door expedition, but also saying that there is no door with that name: Fixed