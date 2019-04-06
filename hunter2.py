n=input()
if n.isalpha():
    print("invalid")
else:
    n=int(n)
    a = [int(i) for i in input().split()]

    for i in range(0,n):

        for j in range (i+1,n):
            if(a[i]<a[j]):
                temp=a[i]
                a[i]=a[j]
                a[j]=temp
    for i in a:
        print(int(i) ,end='')
