#import random

#spielfelder = {i: {"typ": "normal"} for i in range(1, 101)} # 100 Felder "Normal"

#sonderfelder = random.sample(range(1, 101), 10) # 10 Zufallsfelder mit Sondereigenschaften

# Schritt 3: Weise den Sonderfeldern bestimmte Typen zu
#for feld in sonderfelder:
#    spielfelder[feld]["typ"] = "sonderfeld"
#    "x" = random.randint (2,12)
#    spielfelder[feld]["bonus"] = ("Springe x Felder nach vorne")
import.random
leiterspiel_dict = {
    3: 10,
    5: -3,
    8: 22,
    10: -5,
    20: 15,
    24: -10,
    40: 20,
    45: -20,
    98: -20,
}
anzahl_wuerfe = 0
position = 0

while position < 100 :
    anzahl_wuerfe +=1
    wurf = random.randint(1,6)
    print(f"Der Wurf war eine: {wurf}")
    position = position + wurf + leiterspiel_dict.get(position + wurf, 0)
    print("Du bist auf der Position: {position}")
    
print("Spiel nach {anzahl_wuerfe} zuende")
