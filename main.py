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

    for i in range(0, bücher_zahl):
        momentanes_buch = buch_eingabe()

        # Todo #4: Der Nutzer soll das Buch bestätigen müssen, in einem
        # Schritt. Wenn der Nutzer das Buch verwirft soll
        # er erneut gefragt werden, das alte aber verworfen werden.
        # In einem ersten Schritt ist es ok wenn sein Versuch als
        # Buch Eintrag zählt.

        if buch_ist_korrekt(momentanes_buch):
            bücher_liste.append(momentanes_buch)

        # Todo #3: Der Nutzer sollte gewarnt werden falls sein Buch
        # falsch ist. Es soll aber weiterhin in die Liste aufgenohmen werden.

    # Todo #1: Der Nutzer soll angezeigt bekommen das die Eingabe abgeschlossen ist.

    # Todo #4: Der Nutzer soll gesagt bekommen wie viele der Bücher in seiner Liste korrekt sind und welche Bücher falsch sind.

    if liste_ist_duplikat_frei(bücher_liste):
        # Todo: Der Nutzer soll anzeigt bekommen das seine Liste keine Duplikate enthält
        pass


if __name__ == "__main__":
    main()
