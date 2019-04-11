m=int(input())
c=[int(i) for i in input().split()]
for i in range(0,m):
    for j in range(i+1,m):
        if c[i]<c[j]:
            temp=c[i]
            c[i]=c[j]
            c[j]=temp
for i in c:
    print(i)
