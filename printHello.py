def loop():
    try:
        n = int(input())
        for i in range(n):
            print("HELLO")
    except ValueError as e:
        print("invalid")
loop()
