n=int(input())
a=[int(i) for i in input().split()]
for i in range(0,n):
    for j in range(i+1,n):
        if a[i]<a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
for i in a:
    print(i)
