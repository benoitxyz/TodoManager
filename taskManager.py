import sys

from helps import showHelp, showHelpInit, showHelpAdd, showHelpDelete, showHelpComplete, showHelpMove
from init import init
from list import list
from todo import add_todo, delete_todo, complete_todo, move_todo

if __name__ == "__main__" :
    if len(sys.argv) == 1 :
        showHelp()
        exit(0)

    match sys.argv[1] :
        case "help" :
            showHelp()
            exit(0)
        case "init" :
            if len(sys.argv) < 3 :
                showHelpInit()
            elif not sys.argv[2] == "help" and not sys.argv[2] == "?" :
                init(sys.argv[2])
            else: 
                showHelpInit()
                exit(1)
            exit(0)
        case "list" :
            if len(sys.argv) > 2 :
                print("Too much argument")
            else :
                list()
                exit(0)
        case "add" :
            if len(sys.argv) != 3 :
                showHelpAdd()
                exit(1)
            elif sys.argv[2] == "help" or sys.argv[2] == "?" :
                showHelpAdd()
                exit(0)
            else :
                add_todo(sys.argv[2])
        case "delete" :
            if len(sys.argv) < 3 :
                showHelpDelete()
            else :
                delete_todo(sys.argv[2])
                exit(0)
        case "complete" :
            if len(sys.argv) < 3 :
                showHelpComplete()
            else :
                complete_todo(sys.argv[2])
                exit(0)
        case "move" :
            if len(sys.argv) < 4 :
                showHelpMove()
            else :
                move_todo(sys.argv[2], sys.argv[3])
                exit(0)