def num(n):
    try:
        x = input()
        if(x>="a" and x<="z") or (x>="A" and x<="Z"):
            return "invalid"
        else:
            return(len(x))
    except ValueError as e:
        print("invaild")
num(n)
