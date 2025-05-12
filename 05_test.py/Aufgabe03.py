SpielerBank = [random(0,250)]
while len(SpielerBank) >=50:
    Zahlung = input("Wollen Sie zahlen?")
    if Zahlung == "Ja":
        print("Du bist Frei!")
    if Zahlung == "Nein":
        print("Du hast 3 Möglichkeiten einen Pasch zu Würfeln, ansonsten musst du Zahlen.")
        import random
        i=1
        k=1
        while i<4 and k<4:
            wuerfel1=random.randint(1,6)
            wuerfel2=random.randint(1,6)
            print(wuerfel1, wuerfel2)
            if wuerfel1 == wuerfel2:
                print("Du bist Frei!")
                break
            elif wuerfel1 != wuerfel2:
                i=i+1
                k=k+1
        if i and k > 3:
            print("Du musst Zahlen!")
            SpielerBank - 50
            

        

            
            
