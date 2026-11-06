baholar = {"Ali": 85, "Vali": 72, "Madina": 96, "Jasur": 68}

eng_yuqori_ism = max(baholar, key=baholar.get)
eng_yuqori_ball = baholar[eng_yuqori_ism]
ortacha_ball = sum(baholar.values()) / len(baholar)

print(f"Yuqori ball olganlar: {eng_yuqori_ism} — {eng_yuqori_ball}")
print(f"O‘rtacha ball: {ortacha_ball}")
