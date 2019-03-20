def number():
    try:
        num = int(input('Enter:'))
    except TypeError as e:
        return ("Invalid")
        pass
    except ValueError as f:
        return ("Invalid")
        pass
    if (num > 0):
        return ("Positive")
    elif (num == 0):
        return ("Zero")
    else:
        return ("Negative") 

print(number())
