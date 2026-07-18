print("Welcome\n\n\nfor operators use:\na for addition \ns for substraction \nm for multiplication \nd for division\n\n\n")
    
 #for infinit execution
while True:
    n1 = int(input("your first number: "))
    n2 = int(input("your second number: "))
    opr = input("select operation: ")
    
#main body 
    if opr == "a" :
    	print("sum: ",n1 + n2)
    elif opr == "s":
    	print("difference: ",n1 - n2)
    elif opr == "m":
    	print("product: ",n1 * n2)
    elif opr == "d":
    	if n2== "0" :
    		print("invalid")
    	else:
    		print("division: ",n1 / n2)
    else:
        print("invalid choice")
    
#choice to continue or not
    choice = input("\nDo you want to use calculator: y/n: ")
    if choice.lower() == "y":
        continue
    elif choice.lower() == "n" :
        break

print("Thank you for using me")