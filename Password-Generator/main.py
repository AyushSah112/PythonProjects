# Password Generator

import random

#Material for password creation
lowercase = [
    "a","b","c","d","e","f","g","h","i","j","k","l","m",
    "n","o","p","q","r","s","t","u","v","w","x","y","z"
    ]

uppercase = [
    "A","B","C","D","E","F","G","H","I","J","K","L","M",
    "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
    ]

numbers = [
    "0","1","2","3","4","5","6","7","8","9"
    ]

symbols = [
    "!","@","#","$","%","^","&","*","(",")",
    "_","-","+","=","<",">","?","/","{","}",
    "[","]","|",":",";"
    ]
#for multiple attempts 
while True:
   
    password_created = "" 
    # To handle invalid options
    try:
        a = int(input("Enter\n1 for weak\n2 for medium\n3 for strong password" ))
        
        if a == 1:
            for _ in range(5):
                password_created += random.choice(lowercase)
            for _ in range(3):
                password_created += random.choice(numbers)
            
        elif a == 2:
            for _ in range(5):
                password_created += random.choice(uppercase)
            for _ in range(5):
                password_created += random.choice(lowercase)
            for _ in range(3):
                password_created += random.choice(numbers)
                
        elif a == 3:
            for _ in range(5):
                password_created += random.choice(uppercase)
            for _ in range(5):
                password_created += random.choice(lowercase)
            for _ in range(3):
                password_created += random.choice(numbers)
            for _ in range(3):
                password_created += random.choice(symbols)
            
        else:
            print("Invalid choice")
            continue
    
    except Exception  as e:
        print(e)
        continue
    
    password = list(password_created)
    random.shuffle(password)
    password_created = "".join(password)
    
    print(password_created)
    
    choice = input("Do you want to continue? y/n   ")
    
    if choice.lower() == "y" :
        continue
    else:
        break