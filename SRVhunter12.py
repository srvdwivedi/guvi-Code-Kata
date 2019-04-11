def crestack():
    stack=[]
    return stack
def pustack(stack,item):
    stack.append(item)
    return stack
def size(stack):
    return len(stack)
def isempty(stack):
    if size(stack)==0:
        return True
def popsta(stack):
    if (isempty(stack)): return
    return stack.pop()
a=crestack()
b=input()
l=len(b)
z=[]
x=[]
count=1
for i in range(0,l):
    pustack(a,b[i])
    x.append(b[i])
for i in range(0,l):
    z.append(popsta(a))
for i in range(0,l):
    if x[i] not in z[i]:
        count=0
if count==0:
    print("NO")
else:
    print("YES")
