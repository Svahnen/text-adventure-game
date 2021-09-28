class Lock :
    def __init__(self,  code, initiallyLocked) :
        self.code = code
        self.locked = initiallyLocked

    def unlock(self, code) :
        """ 
        Tries to unlock this lock using the given code.
        Returns True if it worked, otherwise False
        """
        if self.code == code :
            self.locked = False
            return True
        return False

    def lock(self) :
        """ Locks this lock. Always succeeds """
        self.locked = True

    def isLocked(self) :
        """ Checks if this lock is locked """
        return self.locked