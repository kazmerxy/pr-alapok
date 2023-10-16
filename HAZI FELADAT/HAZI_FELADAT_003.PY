import random

szam1 = random.randint(1,5)

szam2 = int(input("Kérem adjon meg egy számot 1 és 5 között: "))

if szam2 == szam1:
    print("Gratulálok eltaláltad a számot")
elif szam2 < szam1:
    print("A megadott számod kisebb.")
else:
    print("A megadott számod nagyobb.")
