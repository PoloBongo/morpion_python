a = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
def morpion():
    for row in a:
        for elem in row:
            print(elem, end=' ')
        print()

morpion()

joueur1_joue = True
joueur2_joue = False
parti_en_cours = True

x = 0

while parti_en_cours :

    while joueur1_joue :
        joueur1 = int(input(("choiser la case joueur 1 : ")))
        nb_colonne = 3
        nb_ligne = 3
        for i in range(nb_ligne):
            for j in range(nb_colonne):
                if joueur1 == a[i][j]:
                    a[i][j] = 'X'
                    joueur1_joue = False
                    joueur2_joue = True
                    x = x + 1
        morpion()

    if x == 9:
        print('Match Null')
        parti_en_cours = False
        joueur2_joue = False

    if a[0][0] == 'X' and a[0][1]  == 'X' and a[0][2]  == 'X' or a[1][0] == 'X' and a[1][1]  == 'X' and a[1][2]  == 'X' or a[2][0] == 'X' and a[2][1]  == 'X' and a[2][2]  == 'X':
        print('La partie à était gagné par Joueur 1')
        parti_en_cours = False
        joueur2_joue = False
    if a[0][0] == 'X' and a[1][0]  == 'X' and a[2][0]  == 'X' or a[0][1] == 'X' and a[1][1]  == 'X' and a[2][1]  == 'X' or a[0][2] == 'X' and a[1][2]  == 'X' and a[2][2]  == 'X':
        print('La partie à était gagné par Joueur 1')
        parti_en_cours = False
        joueur2_joue = False
    if a[0][0] == 'X' and a[1][1]  == 'X' and a[2][2]  == 'X' or a[0][2] == 'X' and a[1][1]  == 'X' and a[2][0]  == 'X':
        print('La partie à était gagné par Joueur 1')
        parti_en_cours = False
        joueur2_joue = False

    while joueur2_joue :
        joueur2 = int(input(("choiser la case joueur 2 : ")))
        nb_colonne = 3
        nb_ligne = 3
        for i in range(nb_ligne):
            for j in range(nb_colonne):
                if joueur2 == a[i][j]:
                    a[i][j] = 'O'
                    joueur2_joue = False
                    joueur1_joue = True
                    x = x + 1
        morpion()

    if x == 9:
        print('Match Null')
        parti_en_cours = False
        joueur2_joue = False

    if a[0][0] == 'O' and a[0][1]  == 'O' and a[0][2]  == 'O' or a[1][0] == 'O' and a[1][1]  == 'O' and a[1][2]  == 'O' or a[2][0] == 'O' and a[2][1]  == 'O' and a[2][2]  == 'O':
        print('La partie à était gagné par Joueur 2')
        parti_en_cours = False
        joueur2_joue = False
    if a[0][0] == 'O' and a[1][0]  == 'O' and a[2][0]  == 'O' or a[0][1] == 'O' and a[1][1]  == 'O' and a[2][1]  == 'O' or a[0][2] == 'O' and a[1][2]  == 'O' and a[2][2]  == 'O':
        print('La partie à était gagné par Joueur 2')
        parti_en_cours = False
        joueur2_joue = False
    if a[0][0] == 'O' and a[1][1]  == 'O' and a[2][2]  == 'O' or a[0][2] == 'O' and a[1][1]  == 'O' and a[2][0]  == 'O':
        print('La partie à était gagné par Joueur 2')
        parti_en_cours = False
        joueur2_joue = False