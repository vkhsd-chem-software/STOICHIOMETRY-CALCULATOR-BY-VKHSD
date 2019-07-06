from chempy import Substance
from chempy import balance_stoichiometry
import sys
from pprint import pprint
from chempy import mass_fractions

print("PLEASE CAPITALIZE ELEMENTS RESPECTFULLY/CORRECTLY")

e1 = input('Reagent compound 1: ')
e2 = input('Reagent compound 2: ')
e3 = input('Product compound 1: ')
e4 = input('Product compound 2: ')

s1 = Substance.from_formula(e1)
s2 = Substance.from_formula(e2)
s3 = Substance.from_formula(e3)
s4 = Substance.from_formula(e4)

print(e1, "=", round(s1.molar_mass(), 3))
print(e2, "=", round(s2.molar_mass(), 3))
print(e3, "=", round(s3.molar_mass(), 3))
print(e4, "=", round(s4.molar_mass(), 3))

reac, prod = balance_stoichiometry({e1, e2}, {e3, e4})

pprint(reac)
pprint(prod)

for fractions in map(mass_fractions, [reac, prod]):
    pprint({k: '{0:.3g} wt%'.format(v * 100) for k, v in fractions.items()})

if input("Solve for limiting reagent? (Y/N)") == "N":
    sys.exit()

masse1 = input(f"Grams of {e1}? ")
masse2 = input(f"Grams of {e2}? ")

mole1 = input(f"Moles of {e1}? ")
mole2 = input(f"Moles of {e2}? ")
mole3 = input(f"Moles of {e4}? ")
mole4 = input(f"Moles of {e3}? ")

limitingrcheck1 = float(masse1) * (1 / float(s1.mass)) * (int(mole3) / int(mole1)) * (float(s3.mass) / 1)

print(e1, "=", round(limitingrcheck1, 3), e3)

limitingrcheck2 = float(masse2) * (1 / int(s2.mass)) * (int(mole3) / int(mole2)) * (float(s3.mass) / 1)

print(e2, "=", round(limitingrcheck2, 3), e3)

if limitingrcheck1 > limitingrcheck2:
    limr1 = s2  # x2
    limr1mass = masse2  # x2g
    limr2 = s1  # x1
    limr2mass = masse1  # x1g
    limr1moles = mole2  # yx2
    limr2moles = mole1  # yx1
    print(e2, "is the limiting reagent")
else:
    limr1 = s1
    limr1mass = masse1
    limr2 = s2
    limr2mass = masse2
    limr1moles = mole1
    limr2moles = mole2
    print(e1, "is the limiting reagent")

excessp1 = (float(limr1mass) * (1 / float(limr1.mass) * (float(limr2moles)) / float(limr1moles)) * (float(limr2.mass) / 1))
print(round(float(excessp1), 3), "of", limr2, "would be used in synthesis")
print(round(round(float(limr2mass), 3)-round(float(excessp1), 3), 3), "of", limr2, "remaining")