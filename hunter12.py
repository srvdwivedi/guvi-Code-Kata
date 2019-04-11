n,x=input().split()
n=int(n)
x=int(x)
a=[int(i) for i in input().split()]
b = sorted(a)
print(b[-x])
