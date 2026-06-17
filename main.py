from src.input import anzahl_eingabe


def main():
    bücher_zahl = anzahl_eingabe()

    for i in range(0, round(bücher_zahl / 2)):
        print(i)
    pass


if __name__ == "__main__":
    main()
