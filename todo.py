from config import Config
from init import test_todo_file

def add_todo(new_task):
    
    try:
        # Lire le contenu existant du fichier
        with open(Config.TODO_FILE, 'r', encoding='utf-8') as f:
            lignes = f.readlines()

        # Vérifier si le commentaire est présent
        if test_todo_file() != "OK":
            print('You need to initialiase the todoManager first.')
            exit(1)

        # Trouver l'index du commentaire pour insérer la nouvelle tâche avant
        index_commentaire = lignes.index(Config.END_FILE_COMMENT + "\n") -1

        # Ajouter la nouvelle tâche avant le commentaire
        lignes.insert(index_commentaire, f"- [ ] {new_task}\n")  # Format de tâche Markdown

        # Écrire le contenu mis à jour dans le fichier
        with open(Config.TODO_FILE, 'w', encoding='utf-8') as f:
            f.writelines(lignes)

        #print(f"La tâche '{new_task}' a été ajoutée avec succès.")

    except FileNotFoundError:
        print(f"Erreur : Le fichier '{Config.TODO_FILE}' n'existe pas.")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")