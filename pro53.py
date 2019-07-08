a01=str(input())
a01.lower()
a01.replace(" ","")
b01="abcdefghijklmnopqrstuvwxyz"
b01=list(b01)
l=[]
for i in range(len(a01)):
    if(a01[i] in b01 and a01[i] not in l):
        l.append(a01[i])
if(len(l)==26):
    print("yes")
else:
    print("no"
