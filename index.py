import pandas as pd
from icalendar import Calendar
from datetime import datetime, time, timedelta
import matplotlib.pyplot as plt
import locale

# Config la biblio locale
locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')

# Lit le fichier ics
fichier_ics = 'zzz.ics'
with open(fichier_ics, 'r') as fichier:
    calendrier = Calendar.from_ical(fichier.read())

# Date de début
date_debut = datetime(2024, 9, 20)

P_H = {
    "8h00-9h30": (time(8, 0), time(9, 30)),
    "9h45-11h15": (time(9, 45), time(11, 15)),
    "11h30-13h00": (time(11, 30), time(13, 0)),
    "14h00-15h30": (time(14, 0), time(15, 30)),
    "15h45-17h15": (time(15, 45), time(17, 15)),
    "17h30-19h00": (time(17, 30), time(19, 0)),
    "19h15-20h45": (time(19, 15), time(20, 45))
}

# Décalage horaire : UTC/GMT +2h
decalage_horaire = timedelta(hours=2)

# Extraction des événements
evenements = []
for composant in calendrier.walk():
    if composant.name == "VEVENT":
        debut = composant.get('dtstart').dt
        
        # Convertis les dates en offset-naive et ajuste le décalage horaire
        if debut.tzinfo is not None:
            debut = debut.replace(tzinfo=None)
        debut = debut + decalage_horaire

        if debut >= date_debut:
            # Trouver la plage horaire correspondante
            ajoute = False
            for plage, (heure_debut, heure_fin) in P_H.items():
                if heure_debut <= debut.time() <= heure_fin:
                    evenements.append({
                        'debut': debut,
                        'Jour semaine': debut.strftime('%A'),
                        'Plage horaire': plage
                    })
                    ajoute = True
            
            # On sait jamais 
            if not ajoute:
                print(f"Événement hors plage horaire: {debut.time()}")

df_evenements = pd.DataFrame(evenements)
ordre_J_S = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi']
df_evenements['Jour semaine'] = pd.Categorical(df_evenements['Jour semaine'], categories=ordre_J_S, ordered=True)

# Assure que les plages horaires sont dans le bon ordre
ordre_P_H = list(P_H.keys())
df_evenements['Plage horaire'] = pd.Categorical(df_evenements['Plage horaire'], categories=ordre_P_H, ordered=True)

# Compte le nombre d'occurrences par jour de la semaine et par plage horaire
occ_J = df_evenements.groupby(['Jour semaine', 'Plage horaire']).size().unstack(fill_value=0)

# Calcule les heures totales par jour
heure_J = occ_J * 1.5

# Résultats format brut
print("Nombre total d'heures par jour de la semaine :")
print(heure_J)
print("\nNombre d'occurrences par plage horaire :")
print(occ_J)

# Visu 1
heure_J.plot(kind='bar', stacked=True, title='Heures totales par jour de la semaine et plages horaires utilisées')
plt.ylabel('Heures')
plt.show()

# Visu 2 
occ_J.sum().reindex(ordre_P_H).plot(kind='bar', title="Nombre d'occurrences par plage horaire")
plt.ylabel('Nombre de fois')
plt.show()
