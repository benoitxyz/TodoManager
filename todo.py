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

def delete_todo(numeros):
    try:
        # Lire le contenu existant du fichier
        with open(Config.TODO_FILE, 'r', encoding='utf-8') as f:
            lignes = f.readlines()

        if test_todo_file() != "OK":
            print('You need to initialize the todoManager first.')
            exit(1)

        # Créer une liste pour conserver les lignes restantes
        lignes_a_conserver = []

        # Extraire les lignes de tâches
        lignes_taches = [ligne for ligne in lignes if ligne.strip().startswith('- [ ]') or ligne.strip().startswith('- [x]')]

        # Traiter les numéros fournis
        numeros_a_supprimer = set()  # Utiliser un ensemble pour éviter les doublons

        for numero in numeros.split(','):
            numero = numero.strip()
            if '-' in numero:  # Si c'est une plage
                start, end = map(int, numero.split('-'))
                numeros_a_supprimer.update(range(start, end + 1))
            else:  # Si c'est un numéro simple
                numeros_a_supprimer.add(int(numero))

        # Ajouter le titre et le commentaire de fin et supprimer les lignes de tâches demandées
        index_tache = 0
        for index, ligne in enumerate(lignes):
            # Si la ligne est une tâche
            if index_tache < len(lignes_taches) and ligne == lignes_taches[index_tache]:
                if (index_tache + 1) in numeros_a_supprimer:
                    # Ignorer la ligne à supprimer
                    index_tache += 1
                    continue
                else:
                    # Conserver la tâche
                    lignes_a_conserver.append(ligne)
                    index_tache += 1
            else:
                # Conserver le titre et le commentaire de fin
                lignes_a_conserver.append(ligne)

        # Écrire le contenu mis à jour dans le fichier
        with open(Config.TODO_FILE, 'w', encoding='utf-8') as f:
            f.writelines(lignes_a_conserver)

        print(f"Tâches supprimées : {', '.join(map(str, numeros_a_supprimer))}")

    except FileNotFoundError:
        print(f"Erreur : Le fichier '{Config.TODO_FILE}' n'existe pas.")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")

def complete_todo(numeros):
    try:
        # Lire le contenu existant du fichier
        with open(Config.TODO_FILE, 'r', encoding='utf-8') as f:
            lignes = f.readlines()

        if test_todo_file() != "OK":
            print('You need to initialize the todoManager first.')
            exit(1)

        # Créer une liste pour conserver les lignes mises à jour
        lignes_a_conserver = []

        # Extraire les lignes de tâches
        lignes_taches = [ligne for ligne in lignes if ligne.strip().startswith('- [ ]') or ligne.strip().startswith('- [x]')]

        # Traiter les numéros fournis
        numeros_a_completer = set()  # Utiliser un ensemble pour éviter les doublons

        for numero in numeros.split(','):
            numero = numero.strip()
            if '-' in numero:  # Si c'est une plage
                start, end = map(int, numero.split('-'))
                numeros_a_completer.update(range(start, end + 1))
            else:  # Si c'est un numéro simple
                numeros_a_completer.add(int(numero))

        # Marquer les tâches comme terminées
        index_tache = 0
        for index, ligne in enumerate(lignes):
            if index_tache < len(lignes_taches) and ligne == lignes_taches[index_tache]:
                if (index_tache + 1) in numeros_a_completer:
                    # Marquer la tâche comme terminée
                    ligne = ligne.replace('- [ ]', '- [x]')
                lignes_a_conserver.append(ligne)
                index_tache += 1
            else:
                # Conserver le titre et le commentaire de fin
                lignes_a_conserver.append(ligne)

        # Écrire le contenu mis à jour dans le fichier
        with open(Config.TODO_FILE, 'w', encoding='utf-8') as f:
            f.writelines(lignes_a_conserver)

        print(f"Tâches marquées comme terminées : {', '.join(map(str, numeros_a_completer))}")

    except FileNotFoundError:
        print(f"Erreur : Le fichier '{Config.TODO_FILE}' n'existe pas.")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")

def move_todo(task_number, new_position):
    try:
        # Lire le contenu existant du fichier
        with open(Config.TODO_FILE, 'r', encoding='utf-8') as f:
            lignes = f.readlines()

        if test_todo_file() != "OK":
            print('You need to initialize the todoManager first.')
            exit(1)

        # Extraire les lignes de tâches
        lignes_taches = [ligne for ligne in lignes if ligne.strip().startswith('- [ ]') or ligne.strip().startswith('- [x]')]

        # Vérifier que le numéro de tâche et la nouvelle position sont valides
        task_number = int(task_number)
        new_position = int(new_position)

        if task_number < 1 or task_number > len(lignes_taches):
            print(f"Erreur : Le numéro de tâche {task_number} est invalide.")
            return

        if new_position < 1 or new_position > len(lignes_taches):
            print(f"Erreur : La position {new_position} est invalide.")
            return

        # Déplacer la tâche
        task_to_move = lignes_taches[task_number - 1]
        lignes_taches.remove(task_to_move)
        lignes_taches.insert(new_position - 1, task_to_move)

        # Écrire le contenu mis à jour dans le fichier
        lignes_a_conserver = []

        # Conserver le titre et le commentaire de fin, et réécrire les tâches
        index_tache = 0
        for index, ligne in enumerate(lignes):
            if index_tache < len(lignes_taches) and ligne.strip().startswith('- [ ]') or ligne.strip().startswith('- [x]'):
                lignes_a_conserver.append(lignes_taches[index_tache])
                index_tache += 1
            else:
                # Conserver le titre et le commentaire de fin
                lignes_a_conserver.append(ligne)

        # Écrire le contenu mis à jour dans le fichier
        with open (Config.TODO_FILE, 'w', encoding='utf-8') as f:
            f.writelines(lignes_a_conserver)

        print(f"Tâche {task_number} déplacée à la position {new_position}.")

    except FileNotFoundError:
        print(f"Erreur : Le fichier '{Config.TODO_FILE}' n'existe pas.")
    except ValueError:
        print("Erreur : Veuillez entrer des numéros valides pour la tâche et la position.")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")

def is_todo_exist(position, task_lines):
    try:

        # Vérifier si la position est valide
        position = int(position)

        if position < 1 or position > len(task_lines):
            return False

        # If everything is valid, return true
        return True

    except ValueError:
        print("Error : Please enter a valid number.")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")

    return False