
while True:
    n = int(input("How many rows do you want?  "))
    
    sys = input("which side do want tha base? \nEnter 1 for up \nEnter 0 for down")
    
    if sys == "0":
        for i in range(n):
            print("❤️"*i)
            print("")
         
    elif sys == "1":
        for i in range(n):
            print("❤️"*(n-i))
            print("")      
        
    choice = input("Do you want to continue?  y/n   ")
    if choice == 'y':
        continue
    else:
        exit()