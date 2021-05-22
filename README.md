# TIPE-2021 - microfluidique
Programmation dans le cadre de mon TIPE (CPGE)

* Théotime Fehr-Delude

## Étude et contrôle du comportement de l'écoulement dans un système microfluidique

### Motivation

La microfluidique est un domaine de recherche récent de la physique qui trouve des applications dans de nombreux domaines scientifiques

### Justification de l'ancrage dans le thème

La microfluidique permet de miniaturiser et d'automatiser des analyses chimiques et biologiques
permettant des tests sur des cellules (détection de cellules cancéreuses dans le sang)
séparation d'espèces chimiques.

C'est un enjeu sociétal de pouvoir automatiser et miniaturiser des analyses à moindre coût

## MCOT: Mise en Cohérence des Objectifs du TIPE

### Positionnement thématique et mots-clés

Positionnement: Dynamique des fluides, Chimie

Mots-clés: Microfluidique, Ecoulement des fluides, Ecoulement laminaire, Nombre de Reynolds, Contrôle de l'écoulement, Plastique rétrécissant

Keywords: Microfluidics, Fluid flow, Laminar flow, Reynolds number, Flow control, Shrinky Dink plastic


### Bibliographie commentée

La microfluidique est un domaine de recherche récent qui a de nombreuses applications notamment dans la chimie analytique et la biologie [1]

Cette discipline étudie et utilise le comportement de fluides dans des canaux d'échelle micrométrique afin de miniaturiser et d'automatiser des systèmes d'analyse.
Elle est caractérisée par un écoulement laminaire des fluides, dû à un faible nombre de Reynolds caractéristique de l'échelle des systèmes [2]

La réalisation de tels systèmes n'est d'ordinaire pas à la portée de tous car elle requiert des techniques de fabrication élaborées comme la lithographie ou d'autres 
techniques de moulage [3] à cause de la taille des canaux.
En revanche, un papier de 2008 met en avant une technique de fabrication de canaux microfluidiques à l'aide de plastiques rétrecissant [4] où il suffit de graver 
les canaux à la surface du plastique, puis de chauffer ce plastique à environ 150° pendant quelques secondes pour qu'il rétrécisse d'un facteur 2 environ.

Il s'agit ensuite d'étudier les propriétés de l'écoulement de fluides dans de tels canaux, notamment le fait qu'il s'agisse d'un écoulement laminaire. Typiquement,
dans un tel régime, deux fluides circulant parallèlement et côte à côte ne vont pas se mélanger.
Il est aussi possible de controler le flux en influant sur certains paramètres [5] comme le débit du fluide

Du fait du faible nombre de Reynolds caractéristique de ces circuits, les équations de Navier-Stokes qui décrivent le mouvement des fluides peuvent être grandement simplifiées [2]
pour donner l'équation de Stokes.
Il est donc possible de modéliser les écoulements dans ces systèmes et d'établir une équivalence avec les circuits électriques [6] ; 
il existe une résistance hydraulique analogue à la résistance éléctrique, ainsi qu'un équivalent à la loi d'ohm.


## Problématique retenue

Comment prédire et contrôler différentes propriétés de l'écoulement d'un fluide dans des canaux microfluidiques ?

## Objectifs du TIPE

1. Prédire un écoulement laminaire avec le nombre de reynold
2. Réaliser un canal d'échelle micrométrique
3. Mettre un évidence l'écoulement laminaire dans ce canal
4. arriver a faire un canal assez petit
5. Etude du cas particulier d'un intersection de deux canaux en forme de Y
6. Etude des équivalences entre circuits microfluidiques et circuits électriques

## Liste des références bibliographiques

[1] https://www.elveflow.com/microfluidic-reviews/microfluidic-flow-control/flow-control-in-microfluidics-device/ Applications de la microfluidique en fin de page

[2] ens cachan - définition de la microfluidique et caractérisation de l'écoulement à l'aide du nombre de Reynolds, équivalences avec circuits électriques
https://eduscol.education.fr/sti/sites/eduscol.education.fr.sti/files/ressources/pedagogiques/7111/7111-la-microfluidique-principe-physique-et-mise-en-oeuvre-decoulements-continues-ensps.pdf

[3] GALE, Bruce K., JAFEK, Alexander R., LAMBERT, Christopher J., et al. A review of current methods in microfluidic device fabrication and future commercialization prospects. Inventions, 2018, vol. 3, no 3, p. 60.

[4] CHEN, Chi-Shuo, BRESLAUER, David N., LUNA, Jesus I., et al. Shrinky-Dink microfluidics: 3D polystyrene chips. Lab on a Chip, 2008, vol. 8, no 4, p. 622-624

[5] Brian Kirby - Cornell University Mechanical Engineering 6240 - Physics of Micro- and Nanoscale Fluid Mechanics - 5 Sep 2012.
https://www.youtube.com/watch?v=UUkWnFfcOTk à 18:22 - diviseur de tension

[6] OH, Kwang W., LEE, Kangsun, AHN, Byungwook, et al. Design of pressure-driven microfluidic networks using electric circuit analogy. Lab on a Chip, 2012, vol. 12, no 3, p. 515-545.


