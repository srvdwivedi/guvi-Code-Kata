def number():
    try:
        num=int(input())
           
        if(num % 2 == 0):
            print("Even")
        elif num < 0:
            print("invalid")
        else:
            print("Odd")
    except ValueError as e:
        print("invalid")
number()
