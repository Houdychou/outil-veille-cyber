# Outil de Veille Cyber

Application Flask qui affiche les derniers avis et alertes du CERT-FR.

## Présentation

Ce projet a été réalisé pour me permettre de m'informer sur les dernières actualités en matière de cybersécurité, en particulier les avis et alertes publiés par le CERT-FR. L'application récupère automatiquement les 50 derniers avis et alertes, et les affiche de manière claire et lisible. Il utilise également une deuxième source d'information, les articles de BleepingComputer, pour compléter la veille.

## Fonctionnalités

- Récupération des 50 derniers avis et des 50 dernières alertes du CERT-FR
- Récupération des derniers articles de BleepingComputer (15)
- Affichage du titre, de la référence, de la date de révision et du lien vers chaque publication
- Recherche dans les titres
- Filtre Tous / Avis / Alertes
- Tri par date (plus récent ou plus ancien)
- Compteur de résultats et message « Aucun résultat trouvé »
- Bouton de réinitialisation
