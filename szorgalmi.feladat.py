import random



#harom veletlenszeru szam letrehozasa, a szamok kiiratasa, a szamok osszegenek kiiratasa, a szamok osszege paros vagy paratlan -e es a legnagyobb szamok kiiratasa




szam1 = random.randint(1, 100)
szam2 = random.randint(1, 100)
szam3 = random.randint(1, 100)




#a letrehozott szamok




print("létrehozott számok:")
print(f"1. szám: {szam1}")
print(f"2. szám: {szam2}")
print(f"3. szám: {szam3}")




#a legnagyobb szamok





if szam1 >= szam2 and szam1 >= szam3:
    legnagyobb = szam1
    print(f"A legnagyobb szám: {legnagyobb}")
elif szam2 >= szam1 and szam2 >= szam3:
    legnagyobb = szam2
    print(f"A legnagyobb szám: {legnagyobb}")
else:
    legnagyobb = szam3
    print(f"A legnagyobb szám: {legnagyobb}")





#a harom szam osszege




osszeg = szam1 + szam2 + szam3
print(f"A számok összege: {osszeg}")




#ellenorzes hogy a szamok osszege paros vagy paratlan




if osszeg % 2 == 0:
    print("A számok összege páros szám.")
else:
    print("A számok összege páratlan szám.")