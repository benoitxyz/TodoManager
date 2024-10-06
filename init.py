import os
from config import Config

def init(titre):

    if test_todo_file() == "OK" :
        print('Todo list already initialized')
    elif test_todo_file() == "WRONG" :
        print(f'A file with target name {Config.TODO_FILE} already exist in the directory')
    else:
        # Si le fichier n'existe pas, le créer et y ajouter le titre et le commentaire
        with open(Config.TODO_FILE, 'w') as f:
            f.write(f"# {titre}\n")
            f.write("\n")  # Ligne vide pour séparer le titre du commentaire
            f.write(Config.END_FILE_COMMENT + "\n")
        print(f"Todo file '{Config.TODO_FILE}' had been initialized")
    
def test_todo_file():
    if os.path.isfile(Config.TODO_FILE):
        # Vérifie si le commentaire est présent dans le fichier
        with open(Config.TODO_FILE, 'r') as f:
            contenu = f.read()
            if Config.END_FILE_COMMENT in contenu:
                return "OK"
            else:
                return "WRONG"
    else:
        return "MISSING"