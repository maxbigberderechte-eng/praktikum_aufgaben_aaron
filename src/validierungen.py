
# Todo #2: Es soll überprüft werden ob das Buch "korrekt" ist.✅
    # Ein Buch ist genau dann korrekt wenn Author und Titel Wörter mindestens der Länge eins sind.

def buch_ist_korrekt(buch):
    if len(buch["author"]) >= 1 and len(buch["titel"]) >= 1:
        return True
    else:
        return False


def liste_ist_duplikat_frei(bücher_liste):

    for i in range(0, len(bücher_liste) -1):
        print(i)
        if bücher_liste[i] == bücher_liste[i + 1] :
            return True
        else:
            return False