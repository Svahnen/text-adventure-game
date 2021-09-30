# text-adventure-game

Pusselspel:
Utspelar sig i Nackademins lokaler
Uppdraget: komma in i personalrummet och ändra sina betyg
Text på engelska eller svenska?
Potentiella pussel:
Karta som berättar vart rätt rum är
Hitta nycklar till olika rum
Användarnamn och lösenord till datorn med betygen
Spika kaffet i personalrummet med laxermedel
Potentiella fiender, som kanske tex dricker kaffe och behöver luras iväg:
Mikael Boman
Jonathan Holmström
(Kanske ställa en fråga i början av spelet vad eleven heter och hens lärare heter, så de kan bli mer personligt för den som spelar, samt spelet behöver inte ha ngs namn i sig)

# Email instructions
Så era spelmekaniker blir:

Röra sig mellan rum: Done
Plocka upp items och hålla i dom (nycklar och laxermedel)
Interagera med karta
Använda items på saker i rummet (nycklar i dörrar, laxermedel på kaffe)
Inloggning till dator
Non-Player Karaktärer som kan röra sig mellan rum baserat på förhållanden
Timer
Check varje timer tick som kollar om en NPC är i samma rum som dig (för att avgöra om du blivit hittad)

Detta låter fullt lösbart på 3 pers på 2 veckor så ni har mitt "ok" att köra på. Visar det sig att ni blir klara med det ni planerat innan deadline (utan att jobba övertid) så släng på nått extra pussel. Men ja, ert innehåll ser bra ut med objekt som kan röra sig och interageras med på olika sätt.

/Mvh
Jonathan


# My email
Gameplay:
1: Hitta nyckel till personalrummet inne på expeditionen
2: Hitta Användarnamn och lösenord på en post-it lapp på Mikael Bomans skrivbord
3: MVP: Logga in på datorn och ändra alla betyg till VG: Success! Spelet är slut

Om tid finnes:
3: Jonathan sitter i personalrummet, spika hans kaffe med laxermedel
4: Jonathan går på toaletten, göm dig snabbt! (timer som tickar ner)
Alternativt slut: Logga in på datorn och ändra alla betyg till VG: Success! Spelet är slut

### Gameplay:
1: Hitta nyckel till personalrummet inne på expeditionen
2: Hitta Användarnamn och lösenord på en post-it lapp på Mikael Bomans skrivbord
3: MVP: Logga in på datorn och ändra alla betyg till VG: Success! Spelet är slut
3: Jonathan sitter i personalrummet, spika hans kaffe med laxermedel
4: Jonathan går på toaletten, göm dig snabbt! (timer som tickar ner)
Alternativt slut: Logga in på datorn och ändra alla betyg till VG: Success! Spelet är slut

Ordningen på rummen kan komma att justeras om utifall vi har tid att lägga in alternativa pussel

## Rules:
Morning standup meetings on every project day, 9:00

Make classes for things like for example rooms that are going to be used multiple times

### Blueprint:
1. Create a room class: Done
2. Begin with 1 floor and 2 rooms: Done
3. Add a door between the rooms: Done
4. Build a Look function that looks for doors that can be opened or closed: Done
5. Add description to the rooms, for example: "You are standing in a corridor and you see two doors": Being worked on
6. Add a lock class that can be added to the doors, add a description that a key is needed when locks are locked.
7. Add doors to the rooms with a function instead? Would make the code cleaner since a function on the room class that adds doors could be 1 line for each door added, and would also make us able to create rooms without doors
8. Manage strings so the player can type both Office and office


### Bugs:
1. In office menu, put quit game under "Use the computer": Done
2. When choosing the option to close/open a door that's already closed/open. It says that I have closed the door expedition, but also saying that there is no door with that name.: Done


## Next step:
Show extra menu item if room have items, menu "Pick up".: Done
Finish the pickUp function
When using "open" look through inventory and use key automatically if found.