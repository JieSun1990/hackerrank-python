from itertools import combinations
N = int(input())
p = input().split(' ')
k = int(input())

y = 0
x = 0
t = combinations(p,k)
for tt in t:
    x += 1 #count
    if 'a' in tt: 
        y += 1
print(y/x)
