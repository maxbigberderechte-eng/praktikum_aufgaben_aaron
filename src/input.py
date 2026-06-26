def buch_eingabe():
    author = input("Gib bitte einen Author an:")
    titel = input("Gib bitte einen Titel an:")
    return {"author": author, "titel": titel}


def anzahl_eingabe():

    #Tipp: Du kannst diese Methode auch überschreiben damit du nicht jedes mal lokal was tippen musst, z.B. so:
    # return 1 # So wird immer nur ein Buch abgefragt
    # Todo: Dieser Input soll loopen wenn keine korrekte Zahl eingegeben wurde, aber höchstens 3 Mal.
    # Falls mehr als 3 mal versucht wird, soll die Anwendung enden(Tipp: es gibt die funktion exit())
    bücher_anzahl = input("Wie viele Bücher möchtest du einpflegen?(Gib bitte eine ganze Zahl ohne Komma an)")
    while bücher_anzahl != int:
        try:
            return int(bücher_anzahl)
        except ValueError:
            print(f"{bücher_anzahl} ist keine gültige angabe")
            bücher_anzahl = input("Wie viele Bücher möchtest du einpflegen?(Gib bitte eine ganze Zahl ohne Komma an)")


