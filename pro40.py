strin=str(input())
lis=['d','h','o','n','i']
cut=0
for i in range(len(strin)):
    if(strin[i] in lis):
        cut=cut+1
if(cut-len(strin)==0):
    print("yes")
else:
    print("no")
