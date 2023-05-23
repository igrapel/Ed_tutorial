a1 = ["Mark", "Johnson", 1990, 102300.23]
a2 = ["Marla", "Allis", 1940, 202330.33, 30100.12]

a1 = {
    'first': 'Mark',
    'last': 'johnson',
    'yob': 1990,
    'saving': 103300.23,
}

a2 = {
    'first': 'Marla',
    'last': 'Allis',
    'yob': 1940,
    'saving': 202330.33,
    'retirement': 30100.12
}

a2['retirement'] += 10000
a2['investment'] = 5000
del a2['saving']

keys = a2.keys()
print(keys)
vals = a2.values()
for v in vals:
    print(v)

a2_i = "investment" in a1
print("A1 has investment account: ", a2_i)