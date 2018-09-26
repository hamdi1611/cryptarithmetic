import copy
from Number import Number
import help

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
                        return 0

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
    
    # Return maximum index i which satisfy the condition
    # the condition: all element (list) in self.getList() at index i is input by value or len(list)-1 < levelDOne()
    def levelDone(self):
        level = -1
        for e in self.getList()[-1]:
            if e.isSetByValue():
                level +=1
        return level



    # Return true if there is no rules break
    def isGood(self):
        listX = []
        level = self.levelDone()
        for li in self.getList():
            if li[-1].isSetByValue() and li[1].getValue()==0:
                return False

            if len(li) <= level:
                listX.append(li[:])
            else:
                listX.append(li[:level+1])
        return help.isRight(listX)
        