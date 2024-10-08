from config import Config
from init import test_todo_file

def list() :
    if test_todo_file() != "OK":
        print('Error : You need to initialiase the todoManager first.')
        exit(1)

    try:
        with open(Config.TODO_FILE, 'r', encoding='utf-8') as f:
            content = f.readlines()
            num_tache = 1  # Compteur pour les tâches

            # Show each line with it's number by only numbering tasks
            for line in content:
                # test if line is a task (start with '- [ ]' or '- [x]')
                if line.strip().startswith('- [ ]') or line.strip().startswith('- [x]'):
                    print(f"{num_tache}: {line.rstrip()}")  # show numbered line
                    num_tache += 1  # Increments count
                else :
                    print(f"{line.rstrip()}")

    except Exception as e:
        print(f"Une erreur est survenue : {e}")
