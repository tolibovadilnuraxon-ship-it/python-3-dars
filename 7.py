A = (3, 7)
B = (8, 2)


yigindi_a = sum(A)
yigindi_b = sum(B)

print(f"A yig‘indisi: {yigindi_a}")
print(f"B yig‘indisi: {yigindi_b}")


if yigindi_a > yigindi_b:
    print("A yig‘indisi katta")
elif yigindi_b > yigindi_a:
    print("B yig‘indisi katta")
else:
    print("Yig‘indilar teng")
