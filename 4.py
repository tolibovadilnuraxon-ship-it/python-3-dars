son = int(input("Sonni kiriting: "))
raqamlar_soni = 0

while son>0:
    son//=10
    raqamlar_soni+=1

print(raqamlar_soni)
