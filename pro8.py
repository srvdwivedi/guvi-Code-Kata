m,r=input().split()
m=int(n)
r=int(q)
ar=[int(i) for i in input().split()]

w=[]
z=[]
for i in range(0,q):
    a,b=input().split()
    w.append(a)
    z.append(b)


for i in range(0,q):
    s=int(w[i])-1

    t=int(z[i])-1


    for j in range(1,ar[s]+1):
        if (ar[s]%j==0 and ar[t]%j==0):
            gcd=j
    print(gcd)
