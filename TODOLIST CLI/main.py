
import sys
from todo import Todo
possibleCalls ={"Create":Todo.create,"Read":Todo.readcsv}


def checkcall():

    if not sys.argv[1] in possibleCalls:
        return
    if sys.argv[1] == "Read":
        list = possibleCalls[sys.argv[1]]()
        print(list[3].status)
        #print all todos
        return
    todo = possibleCalls[sys.argv[1]](sys.argv[2],sys.argv[3],sys.argv[4])
    todo.save()


if __name__ =="__main__":
    checkcall()