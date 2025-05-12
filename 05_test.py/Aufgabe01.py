import random

i=1
while i <= 3:
    wurf = random.randint(1,6)
    print (wurf)
    if i==1 and wurf==6:
        wurf = random.randint(1,6)
        print (wurf)
        i=i+2
    if wurf != 6:
           i=i+1
    else:
        if i==2 and wurf==6:
         wurf = random.randint(1,6)
         i=i+1
        if wurf !=6:
            i=i+1
    if i==3 and wurf==6:
        print ("Keine Würfe mehr!")
        break
if i>3:
    print("Keine Würfe mehr!")