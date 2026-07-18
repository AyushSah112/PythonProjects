import time
while True :
        n = int(input("Enter your time in seconds: "))
        i = 0
        while (i < n):
            		i = i+1
            		if i == n:
            		    		print (i, "BOOM!")
            		else:
            		    print (i)
            		    time.sleep(1)
        choice = input("Do you want to continue? (y/n): " )
        if choice.lower() == "n" :
            print("program closed")
            break
        elif choice.lower() == "y":
            continue 
        elif choice.lower() != "n" or choice.lower !="y" :
            print("Invalid choice (Auto switch off)" )
            break
        