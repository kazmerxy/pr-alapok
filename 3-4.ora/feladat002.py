#feladat002
'''
kérjünk be a billentyűzetről két egész számot, és írassuk ki a képernyőre a két szám összegét!
'''

'''
név = input('kérem a nevedet: ')

print(f"itt lesz a név kiiratása:", ' ')

print(f'A megadott név a következő: {név}')
'''

szam1 = input('kérek egy egész számot: ')

szam1 = int(szam1)

szam2 = int(input('kérek egy újabb egész számot: '))

szam3 = float(szam1)

összeg = szam1 + szam2



#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



print(f"a két egész szám összege:  {szam1+szam2}")

print(f"a két egész szám összege:  {összeg}")

print(f"az első változó szám típusa {type(szam1)}")

print(f"a második változó szám típusa {type(szam2)}")

print(f"az összeg változó típusa {type(összeg)}")

print(f"a harmadik változó szám típusa {type(szam3)}")

print(f'a szam3 értéke: {szam3}')


