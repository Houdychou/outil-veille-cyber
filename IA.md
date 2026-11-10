## 2026-11-01 · Claude Code · amélioration du style de l'interface

Demande : amélioration du design de l'outil de veille cybersécurité.

## 2026-11-04 · Claude Code · CSS non appliqué et refonte du style

Demande : le style ne s'affichait pas, puis amélioration du CSS.

- Réécriture de `static/main.css` : avis affichés en cartes, barre de recherche stylisée, lien « Accéder à l'avis » transformé en bouton, espacements harmonisés.


## 2026-11-06 · Claude Code · style des alertes

Demande : ajouter du style pour les alertes.

- Ajout du style `.alerte` dans `static/main.css` : même carte que les avis mais en rouge (bordure, bouton, survol), fond légèrement teinté et badge « ⚠ ALERTE » devant le titre.
- Règles communes `.avis` / `.alerte` regroupées, la couleur passe par la variable `--couleur-carte`.

## 10/11 · Claude · refonte complète du CSS

Demande : changer tout le style de la page
Gardé   : Tout a été gardé
Corrigé : Rien n'a été corrigé
Rejeté  : Rien n'a été rejeté
Commit  : à compléter
