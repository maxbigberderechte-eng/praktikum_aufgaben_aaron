
# Todo #2: Es soll überprüft werden ob das Buch "korrekt" ist.✅
    # Ein Buch ist genau dann korrekt wenn Author und Titel Wörter mindestens der Länge eins sind.

def buch_ist_korrekt(buch):
    if len(buch["author"] + buch["titel"]) >= 2:
        return True
    else:
        return False


def liste_ist_duplikat_frei(bücher_liste):
    return True
