from Number import Number
from State import State

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

def component(a, problem):
    for li in problem.getList():
        for e in li:
            if a == e.getAlpha():
                return e
    return Number(a)

def inputProblem():
    problem = State()
    print ("How many words do you want type into addition? (not include a word as a solution)")
    n = int(input("Input positive integer: "))
    temp = ""
    for i in range(n+1):
        word = input()
        temp += word
        problem.getList().append([])
        if i==n-1:
            for j in range(0, len(problem.getList()[0])):
                print('-', end="")
            print('--- +')
        for a in word:
            problem.getList()[i].insert(0, component(a, problem))
    if len(set(temp)) > 10:
        return State()
    else:
        return problem

def printSolution(s):
    n = len(s.getList())
    for i in range(0, n):
        if i == n-1:
            for j in range(0, len(s.getList()[i])):
                print('-', end="")
            print('--- +')
        temp = []
        for e in s.getList()[i]:
            temp.insert(0, str(e.getValue()))
        print(''.join(temp))
    