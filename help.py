from Number import Number

def isRight(listX):
    more = 0
    sum = 0
    length = len(listX[-1])
    for j in range(0,length):
        for i in range(0, len(listX)-1):
            if j < len(listX[i]):
                sum += listX[i][j].getValue()
        sum += more
        if sum % 10 != listX[-1][j].getValue():
            return False
        more = sum // 10
        sum = 0
    return True

def solve(s):
    if s.getList()[-1][-1].isSetByValue():
        return [s]
    else:
        container = s.childs()
        while len(container) > 0 and not container[0].levelDone()+1 == len(s.getList()[-1]):
            temp = []
            for e in container:
                for a in e.childs():
                    if a.isGood():
                        temp.append(a)
            container = temp
        return container