import statistics as st
ana=int(input())
l=list(map(int,input().split()))
cac=0
for i in range(1,ana):
    l1=l[0:i]
    l2=l[i:ana]
    if(st.mean(l1)==st.mean(l2)):
        cac=cac+1
if(cac>=1):
    print("yes")
else:
    print("no")
