import copy

class State:
    def __init__(self):
        self.list = [] # list of list of object Number
        self.remaining = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] # list of remaining integer 0-9 which is not used yet

    # Getter and Setter
    def getList(self):
        return self.list
    def getRemaining(self):
        return self.remaining
    def copyList(self, input_list):
        self.list = copy.deepcopy(input_list)
    def copyRemaining(self, input_list):
        self.remaining = copy.deepcopy(input_list)
    def popRemaining(self, idx):
        return self.remaining.pop(idx)

    # Assigning (with pop) value from self.remaining[idx]
    def assigning(self, idx):
        for i in range(0, len(self.getList())):
            for e in self.getList():
                if (i < len(e)):
                    if (not e[i].isSetByValue()):
                        e[i].setValue(self.popRemaining(idx))
                        break

    # Return other childs of this state 
    # Child has one more than its parent which is assigned from remaining to list
    def childs(self):
        childs = []
        
        for i in range(0, len(self.getRemaining())):
            child = State()
            child.copyList(self.getList())
            child.copyRemaining(self.getRemaining())
            
            child.assigning(i)
            childs.append(child)

        return childs