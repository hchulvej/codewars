from itertools import product
d1 = list(range(1, 5))
d2 = list(range(1, 7))
d3 = list(range(1, 4))
d4 = list(range(1, 9))
ps = product(d1, d2, d3, d4)

cnt = {i : 0 for i in range(4, 22)}

for p in ps:
    cnt[sum(p)] += 1
print(cnt)