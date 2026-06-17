def buch_eingabe():
    return []


def anzahl_eingabe():
    # Todo: Dieser Input soll loopen wenn keine korrekte Zahl eingegeben wurde.
    bücher_anzahl = int(
        input(
            "Wie viele Bücher möchtest du einpflegen?(Gib bitte eine ganze Zahl ohne Komma an)"
        )
    )
    return int(bücher_anzahl)
