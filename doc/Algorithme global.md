OpenPS
Panic Station

Algorithme global

      Premi�re partie�: mise en place

		Plateau de jeu

* On place la salle R�acteur
* On m�lange les autres cartes lieux, sauf le Nid et le Terminal
* On ins�re au hasard le Terminal dans la deuxi�me moiti� grossi�re de la pile de cartes lieux
* On ins�re au hasard le Nid parmi les trois derni�res cartes lieux

Cartes objets
* On isole la carte H�te et J cartes Jerricans
* On m�lange les autres cartes objets
* On ajoute les 2J-1 premi�res cartes objets au tas contenant l�H�te et les Jerricans
* On m�lange ce tas
* On le place sur la pioche des cartes objets

Joueurs

* On d�termine le nombre J de joueurs
* On associe � chaque joueur une couleur, un nom et un ordre de jeu
* Tous les personnages obtiennent 4 points de vie
* Tous les andro�des obtiennent un pistolet
* Tous les soldats obtiennent un lance-flammes
* Chaque joueur pioche deux cartes
* Tant qu�un joueur poss�de une carte Parasite, on place un Parasite sur la salle de D�part, on d�fausse la carte Parasite et le joueur pioche une carte objet
* Le premier joueur prend le marqueur Phase des Parasites d�sactiv�

      Deuxi�me partie�: jeu
      
      	En boucle�:
      
* Si le joueur en cours a le marqueur Phase des Parasites et qu�il est activ�, on effectue la Phase des Parasites�:
- On d�cale le marqueur Phase des Parasites au joueur suivant et on le d�sactive
- Toutes les portes sont ferm�es
- On lance 1D4 et on d�place tous les parasites selon la direction indiqu�e, selon les d�placements autoris�s
- Pour chaque joueur�touch� :
> Si le joueur poss�de un gilet pare-balles et au moins 6 cartes, on lui demande s�il veut l�utiliser pour chacun de ses personnages.
* Si ses deux personnages sont dans la m�me pi�ce, on demande s�il veut l�utiliser pour les deux personnages
> Chaque personnage touch� perd 1 PV ou 2 PV selon la couleur du Parasite
> On enl�ve du plateau les personnages morts
* Si un joueur a perdu ses deux personnages, il est �limin� de la partie. S�il poss�dait le marqueur Phase des Parasites, il est d�cal� au joueur suivant, en gardant son statut
> Si les conditions de fin de partie sont r�alis�es, on sort de toutes les boucles
* Si le joueur en cours a le marqueur Phase des Parasites et qu�il est d�sactiv�, on l�active
* On d�termine le nombre PA de points d�action du joueur en cours
* Tant que le joueur poss�de au moins 1 PA�:
- On affiche les actions possibles pour ce joueur�:
> Si le joueur poss�de au moins 6 cartes et qu�il poss�de une carte jouable, afficher ��Utiliser une carte��
> Si un personnage du joueur est dans une salle qui peut �tre fouill�e, afficher ��Fouiller une pi�ce��
> Si un personnage du joueur est dans une salle contenant un personnage d�un autre joueur ou un parasite, et que son personnage peut attaquer, afficher ��Attaquer��
> Si un personnage du joueur est dans une salle Terminal et qu�il ne l�a pas encore activ�, afficher ��Activer le Terminal��
> Si un personnage du joueur est dans une salle Infirmerie et qu�il ne l�a pas encore activ�e, afficher ��Se soigner � l�Infirmerie��
> Si le soldat du joueur est au Nid et que le joueur poss�de trois Jerricans, afficher ��Br�ler le Nid��
> Si un personnage du joueur est dans une salle qui permet de placer la premi�re carte du tas, ou que celle-ci ne peut �tre placer nulle part, afficher ��Explorer��
> Si un personnage du joueur est dans une salle qui permet de se d�placer dans une autre salle, afficher ��Se d�placer��
>  S�il choisit ��Utiliser une carte���:
* On d�terminer les cartes utilisables��.

- S�il choisit ��Fouiller une pi�ce���:
> Si les deux personnages ne sont pas dans la m�me pi�ce, choisir une pi�ce
> Si la pi�ce a d�j� �t� fouill�e, faire appara�tre un Parasite � l�aide du 1D4. Sinon, indiquer qu�elle a �t� fouill�e
> Si la pi�ce permet la Fouille en �quipe, demander au joueur s�il veut en profiter, et si oui, avec quel autre joueur
* Distribuer une carte � chacun des deux joueurs
* Pour chaque carte Parasite tir�e, placer un Parasite � l�aide du 1D4 et d�fausser la carte
> Si la pi�ce est un entrep�t�:
* Donner trois cartes au joueur actif
* Pour chaque carte Parasite tir�e, placer un Parasite � l�aide du 1D4 et d�fausser la carte
> Sinon�:
* Donner une carte au joueur actif
* Si la carte est un Parasite, placer un Parasite � l�aide du 1D4 et d�fausser la carte

      

Troisi�me partie�: d�termination des gagnants

