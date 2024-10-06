import sys

from helps import showHelp, showHelpInit, showHelpAdd, showHelpDelete
from init import init
from list import list
from todo import add_todo, delete_todo

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
            if len(sys.argv) < 3 :
                showHelpAdd()
            else :
                add_todo(sys.argv[2])
        case "delete" :
            if len(sys.argv) < 3 :
                showHelpDelete()
            else :
                delete_todo(sys.argv[2])
                exit(0)