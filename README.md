# Avancerad Att-Göra Lista i Python

En sofistikerad att-göra lista-applikation byggd i Python som demonstrerar avancerade programmeringskoncept och praktiska färdigheter.

## Funktioner

- **Uppgiftshantering**: Lägg till, ta bort, redigera och växla status på uppgifter
- **Prioriteter**: Tre prioritetsnivåer (Låg, Medel, Hög)
- **Kategorier**: Organisera uppgifter i anpassade kategorier
- **Förfallodatum**: Ställ in deadlines för uppgifter
- **Sökning**: Sök efter uppgifter baserat på beskrivning eller kategori
- **Filtrering**: Visa uppgifter per kategori eller endast pågående
- **Sortering**: Sortera efter skapandedatum, prioritet eller förfallodatum
- **Försenade uppgifter**: Identifiera uppgifter som har passerat deadline
- **Persistent lagring**: Uppgifter sparas automatiskt till JSON-fil

## Tekniska Färdigheter som Demonstreras

- **Objektorienterad programmering**: Klasser för `Task` och `ToDoList`
- **Datahantering**: JSON serialisering/deserialisering
- **Filhantering**: Läsning och skrivning till filer
- **Datumhantering**: Användning av `datetime` modulen
- **Enum-typer**: För prioritetsnivåer
- **List comprehension**: Effektiv datafiltrering
- **Felhantering**: Try-except block för robusthet
- **Användarinput**: Interaktiv konsollapplikation
- **Modulär kod**: Separata funktioner för olika operationer

## Installation och Körning

1. Se till att Python 3.6+ är installerat
2. Klona eller ladda ner projektet
3. Kör applikationen:
   ```bash
   python main.py
   ```
   eller på Windows:
   ```bash
   py main.py
   ```

## Användning

Applikationen startar med tre exempeluppgifter för att demonstrera funktionaliteten:

- "Lär dig Python" (Hög prioritet, Utbildning)
- "Bygg ett webprojekt" (Medel prioritet, Projekt)  
- "Öva GitHub" (Låg prioritet, Verktyg)

Använd menyn för att:
- Visa alla eller endast pågående uppgifter
- Lägga till nya uppgifter med prioritet, kategori och förfallodatum
- Redigera befintliga uppgifter
- Söka efter specifika uppgifter
- Filtrera och sortera uppgifter

## Projektstruktur

```
main.py          # Huvudapplikationen
tasks.json       # Lagrade uppgifter (skapas automatiskt)
README.md        # Denna fil
```

## Framtida Förbättringar

- GUI-gränssnitt med Tkinter eller webbaserat med Flask
- Databaslagring istället för JSON
- Användarautentisering
- Delning av uppgifter mellan användare
- Notifieringar för förfallodatum

---

Byggd med ❤️ i Python för att visa programmeringskunskaper och skapa en användbar applikation.</content>
<parameter name="filePath">c:\Users\khali\OneDrive\Skrivbord\python-project\README.md