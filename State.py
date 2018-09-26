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
    def removeRemaining(self, idx):
        return self.remaining.remove(idx)

    # Assigning (with pop) value from self.remaining[idx]
    def assigning(self, idx):
        for i in range(0, len(self.getList()[-1])):
            for e in self.getList():
                if (i < len(e)):
                    if (not e[i].isSetByValue()):
                        e[i].setValue(idx)
                        self.removeRemaining(idx)
                        return 0

    # Return other childs of this state 
    # Child has one more than its parent which is assigned from remaining to list
    def childs(self):
        childs = []
        
        for i in self.getRemaining():
            child = State()
            child.copyList(self.getList())
            child.copyRemaining(self.getRemaining())
            
            child.assigning(i)
            childs.append(child)

        return childs
    
    # Return maximum index i which satisfy the condition
    # the condition: all element (list) in self.getList() at index i is input by value or len(list)-1 < levelDOne()
    def levelDone(self):
        lili = []
        level = 0
        while level < len(self.getList()[-1]) and self.getList()[-1][level].isSetByValue():
            level +=1
        lili.append(level-1)
        for li in self.getList():
            level = 0
            while level < len(li) and li[level].isSetByValue():
                level +=1
            if not level == len(li):
                lili.append(level-1)
        return min(lili)

    # Return true if there is no rules break
    def isGood(self):
        listX = []
        level = self.levelDone()
        for li in self.getList():
            if li[-1].isSetByValue() and li[-1].getValue()==0:
                return False

            if len(li) <= level:
                listX.append(li[:])
            else:
                listX.append(li[:level+1])
        return help.isRight(listX)
        