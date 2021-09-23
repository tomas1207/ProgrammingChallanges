
import sys
from cliManager import cliManager
from inspect import signature

if __name__ =="__main__":

    cli = cliManager()

    possibleCalls = cli.possiblecalls()
    print(signature(possibleCalls["Create"]))

    parameters = cli.genparameters(sys.argv)
    print(parameters)

    todo = possibleCalls[sys.argv[1]](*parameters)
    todo.save()