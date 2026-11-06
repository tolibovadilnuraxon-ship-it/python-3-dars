harorat = (18, 20, 17, 23, 25, 21, 19)

yuqori = []
for t in harorat:
    if t > 20:
        yuqori.append(t)

print("Haroratlar:", *yuqori)
print("Kunlar soni:", len(yuqori))
