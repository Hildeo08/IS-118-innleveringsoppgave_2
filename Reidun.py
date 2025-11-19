print("Erling leder en prosjektgruppe som jobber med utviklingen av kommunens nye digitale" 
      "medborgerportal. Prosjektgruppen består av følgende medlemmer: \n"
      "Erling   - Prosjektleder \n"
      "Sivert   - IT-rådgiver fra kommunen \n"
      "Silje    - Ekstern UX-designer \n"
      "Hamdi    - Representant fra kulturavdelingen \n"
      "Hallgeir - Politisk rådgiver \n"
      "Noa      - Sikkerhetsekspert \n"
      "Jabir    - Brukerrepresentant \n \n"
      "De er nå seks uker inn i arbeidet og har kommet inn i storming-fasen"
      "der det har begynt å blusse opp konflikter, og Erling står overfor tre ulike situasjoner"
      "der har må ta noen valg. \n \n"
      "Du skal nå hjelpe Erling med å ta valg i disse tre situasjonene. \n")


#------------ SITUASJON 1 ------------

print("---------------------------------------------------------")

print("\nSituasjon 1: Silje og Sivert er uenige om teknologivalg og design, og "
      "konflikten har utviklet seg fra en sakskonflikt til en personkonflikt. \n"
      "Erling kan velge mellom å ta opp konflikten i fellesskap eller å ha individuelle samtaler.\n")

Situasjon_1 = input("Hva vil du anbefale Ering å gjøre, ta det opp i plenum eller individuelt? ").strip().lower()

if Situasjon_1 == "plenum":
    print(f"\nVed å velge {Situasjon_1} kan det bidra til åpenhet og normalisering av uenighet, men "
          f"det innebærer også risiko for at Silje og Sivert føler seg eksponert og det kan "
          f"forverre konflikten.")

elif Situasjon_1 == "individuelt":
    print(f"\nVed å snakke med dem {Situasjon_1} kan Erling få forståelse for uenighetene og hjelpe "
          f"med å sette fokus på felles mål fremfor personlige meninger.")
    
else:
    print("\nDu har skrevet noe feil, prøv på nytt.")
    

#------------ SITUASJON 2 ------------

print("---------------------------------------------------------")

print("\nSituasjon 2: Hamdi og Jabir er uenige om hvordan innbyggerne skal kunne delta "
      "i digitale folkemøter. Uenigheten er foreløpig lavmælt, men frustrasjonen øker og "
      "kommunikasjonen er hakkete. \n"
      "Erling kan velge mellom å invitere til et møte for å snakke om konflikten,"
      "eller avvente og håpe at konflikten løser seg.\n")

Situasjon_2 = input("Hva vil du anbefale Erling å gjøre, møte eller avvente? ").strip().lower()

if Situasjon_2 == "møte":
    print(f"\nVed å velge å innkalle dem til et {Situasjon_2} kan det bidra til å hindre "
          "at misforståelsen vokser og konflikten utvikler seg. På den andre siden kan "
          "de oppleve dette som overdrevent og at konflikten blir blåst større enn den er.")
    
elif Situasjon_2 == "avvente":
    print(f"\nVed å {Situasjon_2} kan det føre til at de selv finner en løsning og bygger "
          "opp relasjonen. Men det er også en risiko for at konflikten eskalerer. ")

else:
    print("\nDu har skrevet noe feil, prøv på nytt")
    

#------------ SITUASJON 3 ------------

print("---------------------------------------------------------")

print("\nSituasjon 3: I en fase preget av frustrasjon og økende tidspress kan motivasjonen "
      "i teamet få seg en knekk. Erling må velge om han skal sette av tid til relasjonsbygging "
      "eller prioritere struktur og fremdrift. \n")

Situasjon_3 = input("Hva vil du anbefale Erling å prioritere, relasjonsbygging eller fremdrift? ").strip().lower()

if Situasjon_3 == "relasjonsbygging":
    print(f"\nVed å prioritere {Situasjon_3} kan det bidra til å dempe spenningene og styrke "
          f"felleskapsfølelsen, som gjør det lettere å komme videre til norming-fasen.")
    
elif Situasjon_3 == "fremdrift":
    print(f"\nVed å prioritere {Situasjon_3} kan det bidra til å skape en felles retning "
          f"og dempe behovet for å diskutere forskjeller. Men det kan også bidra til "
          f"at konfliktene blir liggende latent og kan blusse opp igjen senere.")

else:
    print("\nDu har skrevet noe feil, prøv på nytt")
    

#------------ AVSLUTNING ------------

print("---------------------------------------------------------\n")

if Situasjon_1 == "individuelt" and Situasjon_2 == "møte" and Situasjon_3 == "relasjonsbygging":
    print(f"\nVed å velge {Situasjon_1}, {Situasjon_2} og {Situasjon_3} i de tre situasjonene "
          f"fører det til at teamet gjenoppretter tilliten og går videre til norming-fasen.")
    
elif Situasjon_1 == "individuelt" or Situasjon_2 == "møte" or Situasjon_3 == "relasjonsbygging":
    print(f"\nVed å velge {Situasjon_1}, {Situasjon_2} og {Situasjon_3} i de tre situasjonene "
          f"løses konfliktene delvis, men relasjonene er fortsatt sårbare.")
    
else:
    print(f"\nVed å velge {Situasjon_1}, {Situasjon_2} og {Situasjon_3} i de tre situasjonene "
          f"mister prosjektet samhold og forsinkes.")
