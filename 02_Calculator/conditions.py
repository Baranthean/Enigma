dayofweek = input("Bitte geben Sie den Wochentag ein: ")
time = int(input("Bitte geben Sie die Uhrzeit ein (Stunde im 24-Stunden-Format): "))

if dayofweek == "Montag":
    print("Heute ist Montag")
    if time < 15 and time >= 12:
        print("Frohes Arbeiten!")
        if time < 12:
            print("Guten Morgen!")

else:
    print("Heute ist nicht Montag!")
