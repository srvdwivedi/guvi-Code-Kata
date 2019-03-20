def check():
    try: 
        a=int(input())
        if(a>0):
            print("Positive")
        elif(a==0):
            print("zero")
        else:
            print("Negative")
    except ValueError:
            print("invalid")
check()
