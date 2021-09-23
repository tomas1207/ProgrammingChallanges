from todo import Todo
class cliManager:
    
    def possiblecalls(self):
        return {"Create":Todo.create,"Read":Todo.readcsv}

    def genparameters(self,list):
        argsList = []

        if len(list) <= 1:
            return

        for args in range(2,len(list)):
            argsList.append(list[args])

        return argsList if len(argsList) > 0 else []

    def callHandler(self):
        return