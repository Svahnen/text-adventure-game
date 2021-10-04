from abc import abstractmethod

class Floor :
    def __init__(self):
        self.description = "Initial description"

    @abstractmethod
    def setDescription(self) :
        """ Every class that inherit from floor class need a description """