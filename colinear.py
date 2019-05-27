def collinear(x1, y1, x2, y2, x3, y3): 
    if ((y3 - y2)*(x2 - x1) == (y2 - y1)*(x3 - x2)): 
        print("yes")
    else:
        print("no")
x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
x3,y3 = map(int,input().split())

collinear(x1, y1, x2, y2, x3, y3)
