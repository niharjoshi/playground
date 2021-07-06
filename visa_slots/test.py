from pandas import DataFrame

final = []

with open("HYD.txt", encoding="utf-8") as f:
    s = f.read().lower()
    a = s.count("approved")
    r = s.count("reject")
    final.append(["hyd", a, r, a/(a+r)])

a1 = 0
a2 = 0
r1 = 0
r2 = 0

with open("MUMBAI1.txt", encoding="utf-8") as f:
    s = f.read().lower()
    a1 = s.count("approved")
    r1 = s.count("reject")

with open("MUMBAI2.txt", encoding="utf-8") as f:
    s = f.read().lower()
    a2 = s.count("approved")
    r2 = s.count("reject")

final.append(["mum", (a1 + a2), (r1 + r2), (a1 + a2)/(a1 + a2 + r1 + r2)])

with open("DELHI.txt", encoding="utf-8") as f:
    s = f.read().lower()
    a3 = s.count("approved")
    r3 = s.count("reject")
    final.append(["del", a3, r3, a3/(a3+r3)])

with open("KOL.txt", encoding="utf-8") as f:
    s = f.read().lower()
    a4 = s.count("approved")
    r4 = s.count("reject")
    final.append(["kol", a4, r4, a4/(a4+r4)])

with open("CHE.txt", encoding="utf-8") as f:
    s = f.read().lower()
    a5 = s.count("approved")
    r5 = s.count("reject")
    final.append(["che", a5, r5, a5/(a5+r5)])

final = DataFrame(final, columns=["c", "a", "r", "%"])
print(final.to_string(index=False))
