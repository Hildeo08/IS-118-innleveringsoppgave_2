
print("Erling leder en prosjektgruppe som jobber med utviklingen av kommunens nye digitale "
      "medborgerportal. Prosjektgruppen består av følgende medlemmer: \n"
      "Erling   - Prosjektleder \n"
      "Sivert   - IT-rådgiver fra kommunen \n"
      "Silje    - Ekstern UX-designer \n"
      "Hamdi    - Representant fra kulturavdelingen \n"
      "Hallgeir - Politisk rådgiver \n"
      "Noa      - Sikkerhetsekspert \n"
      "Jabir    - Brukerrepresentant \n \n"
      "De er nå seks uker inn i arbeidet og har kommet inn i storming-fasen "
      "der det har begynt å blusse opp konflikter, og Erling står overfor tre ulike situasjoner "
      "der han må ta noen valg. \n \n"
      "Du skal nå hjelpe Erling med å ta valg i disse tre situasjonene. \n")

Valg = []  # Liste som skal lagre valgene

# Funksjon for å hente gyldig input
def hent_valg(spørsmål):
    while True:
        svar = input(spørsmål)
        if svar in ["1", "2"]:
            return svar
        else:
            print("Du har skrevet noe feil, prøv på nytt (skriv 1 eller 2).")


# Situasjon 1
print("\nSituasjon 1: \n"
      "Silje og Sivert er uenige om teknologivalg og design, og konflikten har utviklet seg "
      "fra en sakskonflikt til en personkonflikt. \n"
      "Erling kan velge mellom: \n"
      "1: Å ha individuelle samtaler.\n"
      "2: Å ta opp konflikten i fellesskap \n")

Valg1 = hent_valg("Velg 1 eller 2: ")
Valg.append(Valg1)

if Valg1 == "1":
    print("\nVed å velge alternativ 1 kan Erling få forståelse for uenighetene og hjelpe "
          "med å sette fokus på felles mål fremfor personlige meninger.")
    
elif Valg1 == "2":
    print("\nVed å velge alternativ 2 kan det bidra til åpenhet og normalisering av uenighet, men "
          "det innebærer også risiko for at Silje og Sivert føler seg eksponert og det kan "
          "forverre konflikten.")

# Situasjon 2
print("\nSituasjon 2: \n"
      "Hamdi og Jabir er uenige om hvordan innbyggerne skal kunne delta i digitale folkemøter. "
      "Uenigheten er foreløpig lavmælt, men frustrasjonen øker og kommunikasjonen er hakkete. \n"
      "Erling kan velge mellom: \n"
      "1: Å invitere til et møte for å snakke om konflikten \n"
      "2: Å avvente og håpe at konflikten løser seg.\n")

Valg2 = hent_valg("Velg 1 eller 2: ")
Valg.append(Valg2)

if Valg2 == "1":
    print("\nVed å velge alternativ 1 kan det bidra til å hindre at misforståelsen "
          "vokser og konflikten utvikler seg. På den andre siden kan de oppleve dette "
          "som overdrevent og at konflikten blir blåst større enn den er.")
    
elif Valg2 == "2":
    print("\nVed å velge alternativ 2 kan det føre til at de selv finner en løsning og bygger "
          "opp relasjonen. Men det er også en risiko for at konflikten eskalerer.")

# Situasjon 3
print("\nSituasjon 3: \n"
      "I en fase preget av frustrasjon og økende tidspress kan motivasjonen i teamet få seg en "
      "knekk. Erling må velge mellom: \n"
      "1: Å sette av tid til relasjonsbygging \n"
      "2: Å prioritere struktur og fremdrift. \n")

Valg3 = hent_valg("Velg 1 eller 2: ")
Valg.append(Valg3)

if Valg3 == "1":
    print("\nVed å velge alternativ 1 kan det bidra til å dempe spenningene og styrke "
          "felleskapsfølelsen, som gjør det lettere å komme videre til norming-fasen.")
    
elif Valg3 == "2":
    print("\nVed å velge alternativ 2 kan det bidra til å skape en felles retning "
          "og dempe behovet for å diskutere forskjeller. Men det kan også bidra til "
          "at konfliktene blir liggende latent og kan blusse opp igjen senere.")

# Avslutning
print("\n----- Sluttresultat -----")
if Valg == ["1", "1", "1"]:
    print(f"\nVed å velge {Valg} vil teamet gjenopprette tilliten og gå videre til norming-fasen.")
    
elif Valg.count("1") >= 2:
    print(f"\nVed å velge {Valg} vil konfliktene løses delvis, men relasjonene er fortsatt sårbare.")
    
else:
    print(f"\nVed å velge {Valg} vil prosjektet miste samhold og forsinkes.")



