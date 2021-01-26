# Enter your code here. Read input from STDIN. Print output to STDOUT
a = input()
x1 = [] #lower
x2 = [] #upper
x3 = [] #odd
x4 = [] #even

for w in a:
    if w.islower():
        x1.append(w)
    elif w.isupper():
        x2.append(w)
    elif w.isdigit():
        if int(w)%2 == 0:
            x4.append(w)
        else:
            x3.append(w)
print(''.join(sorted(x1) + sorted(x2) + sorted(x3) + sorted(x4)))
