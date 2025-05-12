kartenStapel = ["gr7", "gl2", "+4", "bl3"]
while len(kartenStapel) != 0:
    print(kartenStapel)
    aktuelleKarte = kartenStapel.pop(0)

    if aktuelleKarte == "+4" :
        print("+4 kann gespielt werden.")
        break
        print("Stapel ist leer")
        
#variante 2
# if len(kartenStapel) != 0:
#     aktuelleKarte = kartenStapel.pop(0)
#     while aktuelleKarte != "+4" and len(kartenStapel) !=0:
#         print(kartenStapel)
#         aktuelleKarte = kartenStapel.pop(0)
#     print("karte gefunden")
# if len(kartenStapel) == 0:
#     print("Stapel ist leer")