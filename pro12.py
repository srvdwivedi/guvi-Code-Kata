m,r=input().split()
m=int(m)
r=int(r)
ar=[int(i) for i in input().split()]

x=[]
y=[]
for i in range(0,r):
    a,b=input().split()
    x.append(a)
    y.append(b)


for i in range(0,r):
    sum=0
    s=int(x[i])-1

    t=int(y[i])-1
    for j in range(s,t+1):
        sum=sum+ar[j]
    print(sum)
