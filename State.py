class State:
    def __init__(self):
        self.list = [] # list of list of objek Number
        self.level = -1
        self.remaining = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] # list of remaining integer 0-9 which is not used yet

    # Getter and Setter
    def getList(self):
        return self.list
    def getLevel(self):
        return self.level
    def setLevel(self, level):
        self.level = level
    def getRemaining(self):
        return self.remaining

    # Return other childs of this state 
    # Child has level one higher than their parent
    # Level means how far each list in self.list is set with value
    # Level=1 means for e in self.list, e[0] and e[1] has been set by value (if still not out of range)
    def childs(self):
        childs = []

        return childs