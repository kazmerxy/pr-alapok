print("Zupkó Kázmér")

jegy = int(input("Kérek egy jegyet 1 és 5 között: "))

if jegy == 5:
    print(f"{jegy} a jegyed 5 - jeles")
if jegy == 4:
        print(f"{jegy} a jegyed 4 - jó")
if jegy == 3:
      print(f"{jegy} a jegyed 3 - közepes")
if jegy == 2:
      print(f"{jegy} a jegyed 2 - elégséges")
if jegy == 1:
      print(f"{jegy} a jegyed 1 - elégtelen")
if jegy > 5:
      print(f"a jegyed: {jegy} ami nem megfelelő")