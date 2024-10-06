from config import Config
from init import test_todo_file

def list() :
    if test_todo_file() != "OK":
        print('You need to initialiase the todoManager first.')
        exit(1)

    try:
        with open(Config.TODO_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{Config.TODO_FILE}' n'existe pas.")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")