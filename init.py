import os

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