def buch_eingabe():
    author = input("Gib bitte einen Author an:")
    titel = input("Gib bitte einen Author an:")
    return {"author": author, "titel": titel}


def anzahl_eingabe():

    #Tipp: Du kannst diese Methode auch überschreiben damit du nicht jedes mal lokal was tippen musst, z.B. so:
    # return 1 # So wird immer nur ein Buch abgefragt

    # Todo: Dieser Input soll loopen wenn keine korrekte Zahl eingegeben wurde, aber höchstens 3 Mal.
    # Falls mehr als 3 mal versucht wird, soll die Awendung enden(Tipp: es gibt die funktion exit())
    bücher_anzahl = int(
        input(
            "Wie viele Bücher möchtest du einpflegen?(Gib bitte eine ganze Zahl ohne Komma an)"
        )
    )
    return int(bücher_anzahl)
