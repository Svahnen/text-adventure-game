from abc import abstractmethod

# Room could be child to something very abstract as for example "Space"
# Du ska kunna säga att child klassen är parent klassen, tex Rum är ett Utrymme
class Floor :
    def __init__(self):
        self.description = "Initial description"

    @abstractmethod
    def setDescription(self) :
        """ Every class that inherit from floor class need a description """