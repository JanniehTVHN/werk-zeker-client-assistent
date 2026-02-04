import json

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
    if klant["klant_type"] == "premium":
        return "intensievere begeleiding (complex dossier)"
    elif klant["leeftijd"] >= 67:
        return "AOW-check en extra begeleiding"
    elif klant["bestedingsniveau"] > 100:
        return "check aanvullende regelingen/samenloop"
    else:
        return "standaard dienstverlening"

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
print("Welkom bij de WerkZeker Nederland tool!")

while True:
    klant = verzamel_klant()
    advies = genereer_advies(klant)
    klant["advieslabel"] = advies 
    
    klanten.append(klant)
    
    print(f"Het advieslabel voor {klant['naam']} is: {advies}")

    extra_klant =  input("Wilt u nog een klant invoeren? Type 'ja' of 'nee' ").lower()
    if extra_klant != "ja":
        break

samenvatting(klanten)

with open("klanten.json", "w", encoding="utf-8") as bestand:
    json.dump(klanten, bestand, ensure_ascii=False, indent=4)

print("Alle klantgegevens zijn opgeslagen!")