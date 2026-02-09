def verzamel_klant():
    print("Voer de volgende gegevens in: ")
    
    klant_naam = input("Wat is uw naam? ")
    leeftijd = int(input("Wat is uw leeftijd? "))
    bestedingsniveau = int(input("Wat is uw bestedingsniveau per maand in euro's? "))
    klant_type = input("Wat is uw klanttype? Type 'nieuw', 'bestaand', of 'premium' ").lower()
    
    klant = {
        "naam": klant_naam,
        "leeftijd": leeftijd,
        "bestedingsniveau": bestedingsniveau,
        "klant_type": klant_type
    
    }
    
    return klant
def genereer_advies(klant):
    if klant_type == "premium":
        print(f"Het advieslabel voor {klant_naam} is: intensievere begeleiding (complex dossier)")
    elif leeftijd >= 67:
        print(f"Het advieslabel voor {klant_naam} is: AOW-check en extra begeleiding")
    elif bestedingsniveau > 100:
        print(f"Het advieslabel voor {klant_naam} is: check aanvullende regelingen/samenloop")
    else: 
        print(f"Het advieslabel voor {klant_naam} is: standaard dienstverlening")

def samenvatting(klanten):
    print("Samenvatting klanten")
    for klant in klanten:
        print(
            f"Naam: {klant['naam']} | "
            f"Leeftijd: {klant['leeftijd']} | "
            f"Klanttype: {klant['klant_type']} | "
            f"Advies: {klant['advieslabel']}"
        )


klanten = []
while True:

    print("Welkom bij de WerkZeker Nederland tool!\n \
    Voer de volgende gegevens in alstublieft:")
    klant_naam = input("Wat is uw naam? ")
    leeftijd = int(input("Wat is uw leeftijd? "))
    bestedingsniveau = int(input("Wat is uw bestedingsniveau per maand in euro's? "))
    klant_type = input("Wat is uw klanttype? Type 'nieuw', 'bestaand', of 'premium' ").lower()

    klant = {
        "naam": klant_naam,
        "leeftijd": leeftijd,
        "bestedingsniveau": bestedingsniveau,
        "klant_type": klant_type
    }

    klanten.append(klant)

    if klant_type == "premium":
        print(f"Het advieslabel voor {klant_naam} is: intensievere begeleiding (complex dossier)")
    elif leeftijd >= 67:
        print(f"Het advieslabel voor {klant_naam} is: AOW-check en extra begeleiding")
    elif bestedingsniveau > 100:
        print(f"Het advieslabel voor {klant_naam} is: check aanvullende regelingen/samenloop")
    else: 
        print(f"Het advieslabel voor {klant_naam} is: standaard dienstverlening")

    extra_klant = input("Wilt u nog een klant invoeren? Type 'ja' of 'nee' ")
    if extra_klant != "ja":
        break
        