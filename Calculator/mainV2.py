'''
Calculator V2
'''
def instruction():
    print('''
    Welcome to My calculator v2
    Enter:
    add for addition
    sub for substraction
    mul for multiplication
    div for division
    rem for getting remainder
    exp for exponents
    
    ''')


def addition_opr () :
    c = 0
    n = int(input("How many numbers you want to add:  "))
    for i in range(n):
        b = int(input("Enter your number: "))
        c += b
        print(c)
    
def substraction_opr () :
    p = int(input("Enter the number you want to substract from: "))
    n = int(input("How many numbers you want to substract: "))
    for i in range(n):
        b = int(input("Enter your number: "))
        p -= b
        print(p)
        
def multiplication_opr () :
    c = 1
    n = int(input("How many nunbers you wnat to multiply: "))
    for i in range(n) :
        q = int(input("Enter your nunber: "))
        c *= q
        print(c)
    
def division_opr () :
    r = int(input("Enter the number you want to divide from: "))
    n = int(input("How many numbers you want to divide: "))
    for i in range(n):
        b = int(input("Enter your number: "))
        if b == 0 :
            print("invalid input")
            continue
        else:
            r /= b
            print(r)
        
def remainder_opr():
    s = int(input("Enter the number you want to divide from: "))
    while True:
        r = int(input("Enter your dividing number: "))
        if r == 0:
            print("Invalid input. Divisor cannot be 0.")
            continue
        print(f"Remainder: {s % r}")
        break
    
def exponents_opr () :
    t = int(input("Enter the number you want to raise degree of: "))
    n = int(input("Enter the exponent: "))
    print(t**n)
    
def main () :
    while True:
        a = input("Enter your OPERATION :  ")

        if a == "add" :
            addition_opr ()
            print()
        
        elif a == "sub":
            substraction_opr ()
            print()
        
        elif a == "mul" :
            multiplication_opr ()
            print()
        
        elif a == "div" :
            division_opr ()
            print()
        
        elif a == "rem" :
            remainder_opr()
            print()
            
        elif a == "exp" :
            exponents_opr ()
            print()
            
        elif a == "quit" :
            print("Closing....")
            break
        
        else:
            print("Invalid Input")

if __name__ == '__main__' :
    instruction ()
    main()