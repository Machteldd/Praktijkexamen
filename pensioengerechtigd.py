#Definities van de variabelen leeftijd en werkstatuut
leeftijd = int(input ("Wat is je leeftijd? Voer het aantal jaren in:"))
werkstatuut = input ("Wat is je werkstatuut? Voer in: Medewerker, zelfstandige of ambtenaar:")

#Lijst met mogelijke waarden van de variabele werkstatuut
werkstatuut_lijst = ["Medewerker", "zelfstandige", "ambtenaar"]

#Functie die op basis van de ingevoerde leeftijd en werkstatuut berekent hoeveel geld je krijt per week óf hoeveel jaar je nog moet werken.
def bereken_pensioen (leeftijd, werkstatuut):
    if leeftijd >= 65 and leeftijd < 70:
        if werkstatuut == "medewerker": return "Je krijgt €350 per week."
        if werkstatuut == "zelfstandige": return "Je krijgt €300 per week."
        if werkstatuut == "ambtenaar": return "Je krijgt €370 per week."
    if leeftijd >=70:
        if werkstatuut == "medewerker": return "Je krijgt €370 per week."
        if werkstatuut == "zelfstandige": return "Je krijgt €310 per week."
        if werkstatuut == "ambtenaar": return "Je krijgt €395 per week."
    else: return f"Van werken word je gelukkig, je mag nog {65-leeftijd} jaar genieten van je baan."

#Aanroepen van de functie zodat er output in beeld verschijnt.
print (bereken_pensioen (leeftijd, werkstatuut))