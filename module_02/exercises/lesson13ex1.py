zbior_3 = set()
zbior_5 = set()

for x in range(1, 1001):
    if x % 3 == 0:
        zbior_3.add(x)
    if x % 5 == 0:
        zbior_5.add(x)

same = zbior_3 & zbior_5

print(sorted(same))

