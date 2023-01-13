grille={
        'a':[None,None,None],
        'b':[None,None,None],
        'c':[None,None,None]
}

# afficher la grille
def afficher_grille(grille):  
    print("{}|{}|{}".format(grille['a'][0],grille['a'][1],grille['a'][2]))
    print("{}|{}|{}".format(grille['b'][0],grille['b'][1],grille['b'][2]))
    print("{}|{}|{}".format(grille['c'][0],grille['c'][1],grille['c'][2]))

afficher_grille(grille)

# voir si c'est possible de jouer
def jeu_terminer(grille):
    for values in grille.items():
        if values == None:
            return ("au joueur suivant")
        else:
            return("le jeu est terminé")
print(jeu_terminer(grille))

# vérifier si la grille est gagnante
def grille_gagnate(grille,joueur):
    if (grille['a'][0]) == joueur and grille['a'][1]==joueur and grille['a'][2]== joueur or (grille['b'][0]) == joueur and grille['b'][1]==joueur and grille['b'][2]== joueur or (grille['c'][0]) == joueur and grille['c'][1]==joueur and grille['c'][2]== joueur :
        return True
    else:
        return False
print(grille_gagnate(grille))