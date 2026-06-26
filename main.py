from unittest import skip

from src.input import anzahl_eingabe, buch_eingabe
from src.validierungen import buch_ist_korrekt, liste_ist_duplikat_frei


# Manche der Todos sind nummeriert, bitte in genau dieser Reihenfolge
# abarbeiten! Es gibt auch Todos in anderen Dateien! Die anderen Todos sind eher optional/später falls noch Zeit ist zu machen, in einer Reihenfolge die dir sinnvoll erscheint/die dich interesiert.
# Versuch bitte für jedes Todo erstmal nur eine minimale Lösung zu bauen
# und dann ein neues Todo zu beginnen, wenn die Lösung falsch/unvollständig ist kann man das immer nochmal später fixen.
# Es ist gefordert und gewünscht das du den Code der existiert umbaust,
# was hier steht ist nur das Gerüst und muss nicht bestehen bleiben.
# Leg außerdem bitte für jedes todo einen Branch an und bearbeite dieses # Todo ausschließlich auf diesem Branch.
def main():
    bücher_zahl = anzahl_eingabe()

    bücher_liste = []
    bücher_korrekt = []
    bücher_falsch = []

    for i in range(0, bücher_zahl):
        momentanes_buch = buch_eingabe()

        print(momentanes_buch)
        bestätigung = input("Bestätigen sie die eingaben mit ja:")

        if bestätigung == "ja":
            if buch_ist_korrekt(momentanes_buch):
                bücher_liste.append(momentanes_buch)
                bücher_korrekt.append(momentanes_buch)
                print(f"eingabe {i + 1} erfolgreich abgeschlossen")
            else:
                bücher_liste.append(momentanes_buch)
                bücher_falsch.append(momentanes_buch)
                print(f"eingabe {i + 1} konnte nicht erfolgreich abgeschlossen werden")


    print("Alle eingaben abgeschlossen")
    print(f"bücher korrekt: {bücher_korrekt}, Bücher nicht korrekt {bücher_falsch}")

    if liste_ist_duplikat_frei(bücher_liste):
        print("Duplikate gefunden")
        # Todo: Der Nutzer soll anzeigt bekommen das seine Liste keine Duplikate enthält
        pass
    else:
        print("kein Duplikate gefunden")

if __name__ == "__main__":
    main()
