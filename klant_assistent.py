"""
—
CODE KICKSTART — KlantAssistent
—

Context:
Dit project is onderdeel van de training Code Kickstart.
Je bouwt een eenvoudige Python applicatie die klantgegevens verwerkt
en op basis daarvan een advies genereert.

Doel:
- Oefenen met Python fundamentals
- Denken in iteraties
- Vertalen van pseudocode naar Python

Spelregels:
- Werk stap voor stap
- Test elke iteratie
- Houd de code leesbaar
- Werk toe naar een werkende terminal-applicatie
"""


def verzamel_klant():
    """
    Vraagt gegevens van één klant en retourneert een dictionary.

    Verwachte keys in de dictionary:
    - naam (str)
    - leeftijd (int)
    - besteding (float)
    - klanttype (str: 'nieuw', 'bestaand', 'premium')

    Denkstappen (pseudocode):
    1. Vraag de naam
    2. Vraag de leeftijd
    3. Vraag het bestedingsniveau
    4. Vraag het klanttype
    5. Stop alles in een dictionary
    6. Return de dictionary
    """
    # TODO: implementeer deze functie
    pass


def genereer_advies(klant):
    """
    Ontvangt één klant (dictionary) en retourneert een advies (string).

    Beslisregels:
    - Leeftijd > 65 → 'Aanbieden seniorvoordeel'
    - Besteding > 100 → 'Gericht upsell-moment'
    - Klanttype == 'premium' → 'Dankbericht + premium retention check'
    - Anders → 'Standaard serviceflow'

    Denkstappen:
    1. Lees waarden uit de dictionary
    2. Gebruik if / elif / else
    3. Return één advies
    """
    # TODO: implementeer deze functie
    pass


def samenvatting(klanten):
    """
    Print een samenvatting van alle klanten en adviezen.

    Verwachting:
    - Print het aantal klanten
    - Print per adviescategorie hoe vaak deze voorkomt

    Denkstappen:
    1. Loop over de lijst met klanten
    2. Bepaal per klant het advies
    3. Tel de adviezen
    4. Print het overzicht
    """
    # TODO: implementeer deze functie
    pass


def main():
    """
    Hoofdprogramma van de applicatie.

    Programmaflow (pseudocode):
    1. Print startbericht
    2. Vraag hoeveel klanten worden ingevoerd
    3. Maak een lege lijst voor klanten
    4. Gebruik een loop om klanten te verzamelen
    5. Print per klant het advies
    6. Toon een samenvatting
    """
    print("KlantAssistent gestart")

    # TODO: implementeer de hoofdlogica
    pass


if __name__ == "__main__":
    main()
