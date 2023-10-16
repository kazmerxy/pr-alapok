import math

sugar = float(input("Kérem adja meg a kör sugarát: "))

terulet = math.pi * sugar ** 2

kerulet = 2 * math.pi *sugar

print(f"A kör területe: {terulet}")
print(f"A kör kerülete: {kerulet}")