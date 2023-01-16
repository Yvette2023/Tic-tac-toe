grille=[["_","_","_"],["_","_","_"],["_","_","_"]]


# afficher la grille
def afficher_grille(grille): 
    separateur="|" 
    for ligne in grille:
        print("|", end="")
        print("|".join(ligne), end="")
        print("|")

# jouer un coup puis mettre à jour la grille
def jouer(grille):
    joueur_1 = "x"
    joueur_2 = "o"
    joueur_en_cours = joueur_1
    nombre_cases_vides = 9
    
    print("c'est au tour du joueur suivant")
    afficher_grille(grille)
    
    while nombre_cases_vides > 0:
   
        ligne = int(input("Entrez le numéro de ligne (1, 2, ou 3) : "))
        colonne = int(input("Entrez le numéro de colonne (1, 2, ou 3) : "))
        if ligne < 1 or ligne > 3 or colonne < 1 or colonne > 3:
            print("case inexistante, veuillez réessayer.")
            continue
        if grille[ligne-1][colonne-1] != "_":
            print("Case déjà jouée, veuillez en choisir une autre." + grille[ligne-1][colonne-1])
            continue
        grille[ligne-1][colonne-1] = joueur_en_cours
        if joueur_en_cours == joueur_1:
            joueur_en_cours = joueur_2
            print("c'est au tour du joueur suivant:"+joueur_en_cours)
        else:
            joueur_en_cours = joueur_1
            print("c'est au tour du joueur suivant:"+joueur_en_cours)
        afficher_grille(grille)
        if grille_gagnante(grille):
            break
        nombre_cases_vides -= 1
    print("La partie est terminée.")

# vérifier si la grille est gagnante
def grille_gagnante(grille):

    # Vérifie les lignes
    for i in range(3):
        if grille[i][0] == grille[i][1] == grille[i][2] and grille[i][0] != "_":
            return True

    # Vérifie les colonnes
    for i in range(3):
        if grille[0][i] == grille[1][i] == grille[2][i] and grille[0][i] != "_":
            return True

    # Vérifie les diagonales
    if grille[0][0] == grille[1][1] == grille[2][2] and grille[0][0] != "_":
        return True
    if grille[0][2] == grille[1][1] == grille[2][0] and grille[0][2]!= "_":
        return True
    return False

# Exemple d'utilisation
jouer(grille)
if grille_gagnante(grille):
    print("Grille gagnante!")
else:
    print("Aucun gagnant.")


# Vérifier si la grille est pleine
def est_pleine(grille):
    for elt in grille:
        for case in grille[elt]:
            if case == "_":
                return False
    return True
