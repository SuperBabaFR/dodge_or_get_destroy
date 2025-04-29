# 🕹️ Dodge or Get Destroy

**Dodge or Get Destroy** est un petit jeu développé en **Python** inspiré d'un TP d'informatique de L1. Le principe est simple : esquiver les obstacles pour survivre le plus longtemps possible.

## 🎯 Objectif du jeu

Le joueur contrôle un personnage qui doit éviter des obstacles apparaissant à l'écran. Le but est de rester en vie le plus longtemps possible en esquivant ces dangers.

## 🧱 Structure du projet

Le projet est organisé comme suit :

- `main.py` : Point d'entrée du jeu.
- `config.py` : Fichier de configuration contenant les paramètres du jeu.
- `assets/` : Contient les ressources graphiques utilisées dans le jeu.
- `data/` : Données du jeu, telles que les scores ou les paramètres sauvegardés.
- `effects/` : Effets visuels ou sonores du jeu.
- `entities/` : Définition des entités du jeu, comme le joueur ou les obstacles.
- `hud/` : Interface utilisateur affichée à l'écran.
- `scenes/` : Différentes scènes du jeu (menu, jeu, game over, etc.).
- `util/` : Fonctions utilitaires utilisées dans le projet.
- `.idea/` : Fichiers de configuration de l'IDE (peut être ignoré).
- `__pycache__/` : Dossiers de cache Python (peut être ignoré).

## 🛠️ Technologies utilisées

- **Python 3.x** : Langage de programmation principal.
- **Pygame** : Bibliothèque utilisée pour la gestion des graphismes et des événements du jeu.

## 🚀 Lancer le jeu

1. Assurez-vous d'avoir Python 3.x installé sur votre machine.
2. Installez les dépendances requises (si nécessaire) :
   ```bash
   pip install pygame
   ```
3. Exécutez le jeu :
   ```bash
   python main.py
   ```

## 📄 Licence

Ce projet est réalisé dans un but éducatif dans le cadre d'un TP universitaire. Aucune licence spécifique n'est associée.
