def vowelOrConsonant(x): 
    if (x == 'a' or x == 'e' or x == 'i' or 
        x == 'o' or x == 'u' or x == 'A' or 
        x == 'E' or x == 'I' or x == 'O' or 
        x == 'U'): 
        print("Vowel") 
    elif (x>="a" and x<="z") or (x>="A" and x<="Z"):
        print("Consonant")
    else:
        print("invalid")
        
x = input()
vowelOrConsonant(x) 
