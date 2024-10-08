def showHelp():
    help_text = """
    Manage Totos with totoManager :

    USAGE :
        python todoManager.py [commands] [Options]

    COMMANDS :
        help                Show this help
        init                Initialise le fichier todo
        add                 Ajout de la tache à la liste
        done                Indique la tache comme terminé

    DESCRIPTION :
        This script is made to manage totos in your projects

    EXAMPLES :
        python mon_script.py init "Tasks list name"
        python mon_script.py list

    """
    print(help_text)

def showHelpInit():
    help_text = """
    todoManager Init:

    Used to initialise your todo list.

    Usage :
        python todoManager.py help "Tasks List Name"
    """
    print(help_text)

def showHelpAdd():
    help_text = """
    todoManager Add:

    Used to add todo to your list.

    Usage :
        python todoManager.py add "task to do"
    """
    print(help_text)

def showHelpDelete():
    help_text = """
    todoManager Delete:

    Used to delete todo to your list.

    Usage :
        python todoManager.py delete <todo number or range>
    
    Example :
        python todoManager.py delete 3
        python todoManager.py delete 1-3
    """
    print(help_text)

def showHelpComplete():
    help_text = """
    todoManager Complete:

    Used to complete todo on your list.

    Usage :
        python todoManager.py complete <todo number or range>
    
    Example :
        python todoManager.py complete 3
        python todoManager.py complete 1-3
        python todoManager.py complete 1,4

    """
    print(help_text)

def showHelpMove():
    help_text = """
    todoManager Move:

    Used to move todo on your list.

    Usage :
        python todoManager.py move <todo number or range>
    
    Example :
        python todoManager.py move 3 2 # move from position 3 to 2

    """
    print(help_text)