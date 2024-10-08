# Stats d'un calendrier ESGI

## Description

Ce script Python permet d'analyser un fichier ICS pour afficher les plages horaires spécifiques. Il catégorise les horaires par jour de la semaine et par plage horaire, puis affiche les résultats sous forme tabulaire et graphique.

## Prérequis

- Python
- Bibliothèques Python :
  - `pandas`
  - `icalendar`
  - `matplotlib`

Pour installer les dépendances nécessaires avec pip :

```bash
pip install pandas icalendar matplotlib
```

## Utilisation

1. Placez le fichier ICS que vous souhaitez analyser dans le même répertoire que le script et nommez-le `zzz.ics`.

2. Modifiez la date de début dans le script si nécessaire. La date par défaut est le 20 septembre 2024.

3. Exécutez le script.

## Résultats

Le script génère deux types de sorties principales :

1. **Résultats au format brut**
   La console affichera le nombre total d'heures par jour de la semaine et le nombre d'occurrences par plage horaire. Exemple de sortie :

   ![Figure_3](https://github.com/user-attachments/assets/07cc8b37-6ef9-4f70-97e9-641832655fc7)
   
2. **Résultats graphiques**
   Le script produira également des graphiques pour visualiser les plages horaires et les jours de la semaine.

    ![Figure_1](https://github.com/user-attachments/assets/96f76b98-b895-49dc-87f8-ac701d0e9e9b)
    ![Figure_2](https://github.com/user-attachments/assets/2df7fe1b-f9bb-4754-9305-fe539545e523)

