OpenPS
Panic Station

Algorithme global

      Première partie : mise en place

    Plateau de jeu

* On place la salle Réacteur
* On mélange les autres cartes lieux, sauf le Nid et le Terminal
* On insère au hasard le Terminal dans la deuxième moitié grossière de la pile de cartes lieux
* On insère au hasard le Nid parmi les trois dernières cartes lieux

Cartes objets
* On isole la carte Hôte et J cartes Jerricans
* On mélange les autres cartes objets
* On ajoute les 2J-1 premières cartes objets au tas contenant lHôte et les Jerricans
* On mélange ce tas
* On le place sur la pioche des cartes objets

Joueurs

* On détermine le nombre J de joueurs
* On associe à chaque joueur une couleur, un nom et un ordre de jeu
* Tous les personnages obtiennent 4 points de vie
* Tous les androïdes obtiennent un pistolet
* Tous les soldats obtiennent un lance-flammes
* Chaque joueur pioche deux cartes
* Tant quun joueur possède une carte Parasite, on place un Parasite sur la salle de Départ, on défausse la carte Parasite et le joueur pioche une carte objet
* Le premier joueur prend le marqueur Phase des Parasites désactivé

      Deuxième partie : jeu

        En boucle :

* Si le joueur en cours a le marqueur Phase des Parasites et quil est activé, on effectue la Phase des Parasites :
- On décale le marqueur Phase des Parasites au joueur suivant et on le désactive
- Toutes les portes sont fermées
- On lance 1D4 et on déplace tous les parasites selon la direction indiquée, selon les déplacements autorisés
- Pour chaque joueur touché :
> Si le joueur possède un gilet pare-balles et au moins 6 cartes, on lui demande sil veut lutiliser pour chacun de ses personnages.
* Si ses deux personnages sont dans la même pièce, on demande sil veut lutiliser pour les deux personnages
> Chaque personnage touché perd 1 PV ou 2 PV selon la couleur du Parasite
> On enlève du plateau les personnages morts
* Si un joueur a perdu ses deux personnages, il est éliminé de la partie. Sil possédait le marqueur Phase des Parasites, il est décalé au joueur suivant, en gardant son statut
> Si les conditions de fin de partie sont réalisées, on sort de toutes les boucles
* Si le joueur en cours a le marqueur Phase des Parasites et quil est désactivé, on lactive
* On détermine le nombre PA de points daction du joueur en cours
* Tant que le joueur possède au moins 1 PA :
- On affiche les actions possibles pour ce joueur :
> Si le joueur possède au moins 6 cartes et quil possède une carte jouable, afficher « Utiliser une carte »
> Si un personnage du joueur est dans une salle qui peut être fouillée, afficher « Fouiller une pièce »
> Si un personnage du joueur est dans une salle contenant un personnage dun autre joueur ou un parasite, et que son personnage peut attaquer, afficher « Attaquer »
> Si un personnage du joueur est dans une salle Terminal et quil ne la pas encore activé, afficher « Activer le Terminal »
> Si un personnage du joueur est dans une salle Infirmerie et quil ne la pas encore activée, afficher « Se soigner à lInfirmerie »
> Si le soldat du joueur est au Nid et que le joueur possède trois Jerricans, afficher « Brûler le Nid »
> Si un personnage du joueur est dans une salle qui permet de placer la première carte du tas, ou que celle-ci ne peut être placer nulle part, afficher « Explorer »
> Si un personnage du joueur est dans une salle qui permet de se déplacer dans une autre salle, afficher « Se déplacer »
>  Sil choisit « Utiliser une carte » :
* On déterminer les cartes utilisables.

- Sil choisit « Fouiller une pièce » :
> Si les deux personnages ne sont pas dans la même pièce, choisir une pièce
> Si la pièce a déjà été fouillée, faire apparaître un Parasite à laide du 1D4. Sinon, indiquer quelle a été fouillée
> Si la pièce permet la Fouille en équipe, demander au joueur sil veut en profiter, et si oui, avec quel autre joueur
* Distribuer une carte à chacun des deux joueurs
* Pour chaque carte Parasite tirée, placer un Parasite à laide du 1D4 et défausser la carte
> Si la pièce est un entrepôt :
* Donner trois cartes au joueur actif
* Pour chaque carte Parasite tirée, placer un Parasite à laide du 1D4 et défausser la carte
> Sinon :
* Donner une carte au joueur actif
* Si la carte est un Parasite, placer un Parasite à laide du 1D4 et défausser la carte



Troisième partie : détermination des gagnants
