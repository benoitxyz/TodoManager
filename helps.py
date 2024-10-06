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