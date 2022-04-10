# Tiny Fight

## Concept:
Tiny Fight est un jeu de stratégie en duel.
2 joueurs ont 3 minutes pour placer des unités sur un 
plateau similaire à un jeu d'échec.

Le jeu se divise en 2 temps qui se répètent jusqu'à la victoire d'un des joueurs :
  - Tout d'abord, une phase de préparation où chaque joueur positionne ses troupes dans une zone prédéfinie. Chaque unité ne peut avancer que sur la colonne où elle est placée, il faut donc les placer intelligement.
  - Ensuite, la bataille commence, les deux joueurs n'ont aucun contrôle sur le jeu pendant cette phase.  Les troupes avancent sur leur colonne et combattent les ennemis qu'elles rencontrent en route. 

Si l'unité tombe au combat, elle est définitivement perdue mais si elle atteint l'autre bout du plateau, elle gagne un bonus pour pouvoir être placée de nouveau.

Il y a 2 conditions de victoire :
  - Un des 2 joueurs gagne si l'autre n'a plus d'unités
  - Il n'a pas placé de troupes pendant 3 tours

## Les objectifs:

### partie presque sérieuse:
  - Concurencer TeamfightTactics
  - Gagner beaucoup de moula
  - Eventuellement s'amuser
  - Faire un online pour multiplier les gains par 2
  - Rentabiliser la future année de NSI
  - Quitter la NSI avec un bon souvenir
  - Se rendre compte qu'on a atteint le programme post-BAC en première sans faire exprès
  - Création d'une méta Tiny Fights
  - Création d'une unité admin pour être sûrs de remporter chaque partie et briser la méta
  - Création d'un esport
  - Utilisation de l'unité admin pour remporter l'esport et gagner plus d'argent

### partie sérieuse: 
  - faire un jeu fonctionnel et sans bugs
  - Un jeu permissif pour pouvoir être créatifs dans la création d'unités
  - Des unités créatives (dans la limite du réalisable dans un tableau de tableau et pour des premières spé NSI) jeu tiny fights : "paint.exe" qui utilisera la coloration de grilles
  - Un jeu amusant
  - Possibilité d'utiliser des sorts en jeu pour rompre avec les codes du genre
  - Un système de contrôle d'unité totalement indépendant des joueurs
  - Experience pour avoir des unités plus fortes (max level 3)

### Les Spécificités du jeu
  - Le système de levelling:
    - Une unité gagne des effets quand elle traverse le terrain sans mourir
    - Ces effets rajoutent des statistiques au choix (MAX : 3)
    - Au bout de 3 effets, le joueur peut choisir d'augmenter la troupe d'un niveau. Cette amélioration est spécifique à chaque troupe.
  - La participation en plein match:
    - Chaque troupe possède un tiny move utilisable en plein combat quand le joueur l'active, cette attaque possède un temps de chargement
    - Le joueur possède des sorts activables avec des effets uniques

### Troupes (La partie VRAIMENT amusante)
  - Le chevalier:
    - Troupe légèrement plus puissante que la moyenne
    - Tiny move: Lance une attaque plus puissante
  - La valkyrie:
    - Troupe plus faible que la moyenne qui frappe devant et les deux cases côté d'elle
    - Tiny move: Lance une attaque plus puissante
  - L'archer:
    - Troupe d'attaque à portée de 2 cases ou sur la même colonne
    - Tiny move: flèche coup critique pour tous les ennemis
  - Le lancier:
    - Troupe d'attaque à vitesse, PV, et vittesse d'attaque médiocre 
    - Tiny move: La troupe avance plus vite et lance une attaque très puissante sur le premier ennemi rencontré
  - Le bouclier:
    - Troupe de défense avec beaucoup de PV
    - Tiny move: Réduit l'attaque sur un cercle de rayon 2 cases
  - Nécromancien:
    - Troupe plus faible que la moyenne, invoque des Squelettes devant lui
    - Tiny move: rend les squelettes plus puissants
  - Squelette:
    - Troupe faible mais attaque à peine plus faible que la moyenne
  - Hana (healer):
    - Troupe de soin qui guérit sur la même ligne
    - Tiny move: change d'état (soin <==> attaque)

### Pour l'avenir:
  - Des animations
  - Un menu
  - Des explications détaillées sur chaque troupe (avec image)
  - Des troupes supplémentaires (environ 5)
 