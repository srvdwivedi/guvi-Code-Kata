fis=str(input())
a=len(f[::-1])
li=[]
vi=[]
wi=[]
for i in range(0,a):
    li.append([fis[i+1:],len(fis[i+1:])])
    vi.append([len(fis[i+1:]),fis[i+1:]])
li.sort()
vi.sort()
li=max(l)
vi=max(v)
wi.append(li[0])
wi.append(vi[1])
wi.append(fis[0])
l=[]
for i in wi:
    if(i[0]>fis[0]):
        l.append(i)
print(sorted(l)[0])
