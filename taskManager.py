import sys

from helps import showHelp, showHelpInit
from init import init
from list import list

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