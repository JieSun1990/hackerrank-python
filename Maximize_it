a = input()
k, m = a.split()
k = int(k)
m = int(m)

#1. change everything to be i^2
ll = [] #list of str(numbers)
nn = [] #list of numbers^2
for i in range(k):
    ll.append(input())
    ll[i] = list(ll[i].split(' ')[1:])
    nn.append([int(e)**2 for e in ll[i]])

#2. get combinations using itertools
import itertools
aa = list(itertools.product(*nn)) #all possible combinations

#3. calculate the number of possibilities
print(max([sum(ee)%m for ee in aa]))
