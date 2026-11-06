shaharlar = {"Toshkent": 3000000, "Farg‘ona": 300000, "Samarqand": 600000}

kop = []
for shahar, aholi in shaharlar.items():
    if aholi > 500000:
        kop.append(shahar)

eng_kop = max(shaharlar, key=shaharlar.get)

print("500 000 dan ko‘p:", *kop)
print("Eng ko‘p aholi:", eng_kop)
