boshlangich_pul = 120000
haftalik_qoshimcha = 80000

jami_pul = boshlangich_pul
hafta = 0

while jami_pul <= 500000:
    jami_pul += haftalik_qoshimcha
    hafta += 1

print(f"Kerakli hafta: {hafta}")
