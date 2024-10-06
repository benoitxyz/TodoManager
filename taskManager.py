import os
import sys

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

def init(titre):
    fichier_todo = 'task.todo'
    commentaire_attendu = "<!-- File managed by TodoManager version=1 -->"

    if os.path.isfile(fichier_todo):
        # Vérifie si le commentaire est présent dans le fichier
        with open(fichier_todo, 'r') as f:
            contenu = f.read()
            if commentaire_attendu in contenu:
                print(f"Todo file '{fichier_todo}' is already present.")
            else:
                print(f"A todo file with target name '{fichier_todo}' already existe but this not seems to be manage by todoManager.")
    else:
        # Si le fichier n'existe pas, le créer et y ajouter le titre et le commentaire
        with open(fichier_todo, 'w') as f:
            f.write(f"# {titre}\n")
            f.write("\n")  # Ligne vide pour séparer le titre du commentaire
            f.write(commentaire_attendu + "\n")
        print(f"Todo file '{fichier_todo}' had been initialized")

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
        