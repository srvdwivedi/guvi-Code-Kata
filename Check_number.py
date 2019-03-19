def number(num):
    try:
        num = int(input('Enter: '))
    except ValueError:
        print("ONLY INTERGERS ARE ALLOWED")
    else:
        print("done")
    
    if num > 0:
        print("Positive")")
    elif num == 0:
        print("Zero")
    else:
        print("Negative")
               
print(number(num))
