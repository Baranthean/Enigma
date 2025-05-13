import random

spielfelder = {i: {"typ": "normal"} for i in range(1, 101)} # 100 Felder "Normal"

sonderfelder = random.sample(range(1, 101), 10) # 10 Zufallsfelder mit Sondereigenschaften

# Schritt 3: Weise den Sonderfeldern bestimmte Typen zu
for feld in sonderfelder:
    spielfelder[feld]["typ"] = "sonderfeld"
    "x" = random.randint (2,12)
    spielfelder[feld]["bonus"] = ("Springe x Felder nach vorne")
    

