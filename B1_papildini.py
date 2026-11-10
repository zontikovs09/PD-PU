skaits = {}

with open("sistema.log", encoding="utf-8") as f:
    for rinda in f:
        limenis = rinda.split()[2]
        skaits[limenis] = skaits.get(limenis, 0) + 1

print("Limenu kopsavilkums")

for limenis, skaits_rindu in sorted(skaits.items(), key=lambda x: x[1], reverse=True):
    print(limenis, skaits_rindu)
