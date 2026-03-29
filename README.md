# Avancerad Att-Gora Lista i Python

En mer avancerad att-gora-lista byggd i Python for att visa praktiska programmeringskunskaper i en enkel konsolapplikation.

## Funktioner

- Lagga till, ta bort, redigera och markera uppgifter som klara
- Tre prioritetsnivaer: lag, medel och hog
- Kategorier for att organisera uppgifter
- Forfallodatum for planering och uppfoljning
- Sokning pa beskrivning eller kategori
- Filtrering av pagaende eller kategoribaserade uppgifter
- Sortering efter skapad tid, prioritet eller forfallodatum
- Automatisk lagring i `tasks.json`

## Teknik som visas

- Objektorienterad programmering med `Task` och `ToDoList`
- JSON-serialisering och filhantering
- Datumhantering med `datetime`
- `Enum` for prioritet
- List comprehensions for filtrering
- Enkel felhantering med `try` och `except`
- Interaktiv kommandoradsinput

## Korning

1. Installera Python 3.6 eller senare.
2. Starta programmet:

```bash
python main.py
```

Pa Windows fungerar ocksa:

```bash
py main.py
```

## Exempel pa innehall

Programmet skapar exempeluppgifter forsta gangen det startas, bland annat:

- "Lar dig Python"
- "Bygg ett webprojekt"
- "Ova GitHub"

## Projektstruktur

```text
main.py      # huvudprogrammet
tasks.json   # sparade uppgifter
tasks.txt    # enkel textfil i projektet
README.md    # projektbeskrivning
```

## Mojliga forbattringar

- Grafiskt granssnitt med Tkinter
- Databas i stallet for JSON
- Anvandarhantering
- Delning av uppgifter mellan flera personer
- Notiser for uppgifter med deadline
