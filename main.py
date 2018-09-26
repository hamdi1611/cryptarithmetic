from Number import Number
from State import State
import help

# Example : SEND + MORE = MONEY

z = Number('S')
e = Number('E')
n = Number('N')
d = Number('D')
m = Number('M')
o = Number('O')
r = Number('R')
y = Number('Y')

s = State()
s.getList().append([d, n, e, z])
s.getList().append([e, r, o, m])
s.getList().append([y, e, n, o, m])

print ('Solusi:')
answer = help.solve(s)
print ([[(x.getAlpha(), x.getValue()) for x in apa] for apa in answer[0].getList()])