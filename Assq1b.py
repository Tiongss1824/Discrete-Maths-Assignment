from fractions import Fraction

ls = [4, 5, 6, 7, 8, 9, 10, 12, 12, 14, 15, 18, 20, 21, 24, 28, 30, 35, 36, 40, 42, 45, 56, 60, 63, 70, 72]

ans = 0
n = len(ls)
the_sum = Fraction(1, 2) - Fraction(1, 4) - Fraction(1, 9)
l, r = ls[:n // 2], ls[n // 2:]
mp = {}
for i in range(1 << len(l)):
    s = Fraction(0)
    for j in range(len(l)):
        if i >> j & 1:
            s += Fraction(1, l[j] * l[j])
    if s <= the_sum:
        if s not in mp.keys():
            mp[s] = 0
        mp[s] += 1
for i in range(1 << len(r)):
    s = Fraction(0)
    for j in range(len(r)):
        if i >> j & 1:
            s += Fraction(1, r[j] * r[j])
    t = the_sum - s
    if t in mp.keys():
        ans += mp[t]
print(ans)