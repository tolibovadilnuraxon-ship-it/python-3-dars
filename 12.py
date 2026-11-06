kodlar = ["A12", "B15", "A12", "C20", "B15", "D10"]


noyob_kodlar = []


for kod in kodlar:
    if kod not in noyob_kodlar:  
        noyob_kodlar.append(kod)  

print(f"Noyob kodlar soni: {len(noyob_kodlar)}")
print(f"Kodlar: {', '.join(noyob_kodlar)}")
