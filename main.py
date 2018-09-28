import help

# Example : input integer 2, then SEND + MORE = MONEY
problem = help.inputProblem()

if len(problem.getList())==0:
    print('\nThere in no answer')
else:
    answer = help.solve(problem)
    if len(answer)==0:
        print('\nThere in no answer')
    else:
        print ('\nSolution:')
        for s in answer:
            help.printSolution(s)
            print('')