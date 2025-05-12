import random

i=1
while i <= 3:
    wurf = random.randint(1,6)
    print (wurf)
    i = i+1
    if wurf == 6 and i<=2:
        wurf = random.randint(1,6)
        print (wurf)
        i+1
if i>3:
    print("Keine Würfe mehr!")