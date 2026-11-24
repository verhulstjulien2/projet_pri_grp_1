# Space Invaders

Jeu d’arcade développé en Python avec Pygame. Le joueur contrôle un vaisseau
et tire sur une flotte d’ennemis avant qu’ils ne descendent trop bas.
Chaque ennemi éliminé rapporte un point. Après trois éliminations, le joueur
peut effectuer un tir double.

## Installation sous Windows

1. Installer Python 3.13.
2. Sur la page GitHub du projet, cliquer sur **Code → Download ZIP**,
   puis extraire l’archive.
3. Ouvrir un terminal dans le dossier qui contient `main.py` et `requirements.txt`.
4. Installer les dépendances avec la commande suivante :

   ```powershell
   py -3.13 -m pip install -r requirements.txt
   ```

## Lancer le jeu

Dans le même terminal, exécuter :

```powershell
py -3.13 main.py
```

## Commandes

| Action | Commande |
| --- | --- |
| Déplacer le vaisseau vers la gauche | Maintenir E |
| Déplacer le vaisseau vers la droite | Maintenir D |
| Tirer | Appuyer sur S |
| Quitter le jeu | Fermer la fenêtre |
