from config import Config
from init import test_todo_file

def list() :
    if test_todo_file() != "OK":
        print('You need to initialiase the todoManager first.')
        exit(1)

    try:
        with open(Config.TODO_FILE, 'r', encoding='utf-8') as f:
            contenu = f.readlines()
            num_tache = 1  # Compteur pour les tâches

            # Afficher chaque ligne avec son numéro, en ne numérotant que les tâches
            for ligne in contenu:
                # Vérifier si la ligne contient une tâche (indiquée par '- [ ]' ou '- [x]')
                if ligne.strip().startswith('- [ ]') or ligne.strip().startswith('- [x]'):
                    print(f"{num_tache}: {ligne.rstrip()}")  # Afficher la ligne numérotée
                    num_tache += 1  # Incrémenter le compteur pour la tâche
                else :
                    print(f"{ligne.rstrip()}")

    except FileNotFoundError:
        print(f"Erreur : Le fichier '{Config.TODO_FILE}' n'existe pas.")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")
