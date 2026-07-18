"""
Expense tracker
""" 
import datetime

def time() :
    """Returns the current date and time as a string."""
    return str(datetime.datetime.now())

def menu():
    """Displays the main menu options to the user."""
    print("\n===== Expense Tracker =====")
    print("MENU")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")
    
def add_expense() :
    """Asks the user for one or more expenses and saves them to a file."""
    a = 0
    b = int(input("How many you need to add: "))
    while a < b:
        a += 1
        item = input(f"Enter your Item {a} : ")
        value = input(f"Enter item {a} Value : " )
        with open("expense_tracker.txt" , "a") as file:
            file.write(f"{item},{value},{time()}\n")
            
def view_expense() :
     """Reads and prints all saved expenses from the file."""
     try:
         with open("expense_tracker.txt" , "r") as file:
             print(file.read())
     except FileNotFoundError:
         print("No expenses found yet. Add one first!")
         
def total_expense() :
    """Calculates and prints the total of all saved expenses."""
    total = 0
    try:
        with open("expense_tracker.txt", "r") as file:
            for line in file:
                print(line)
                data = line.strip().split(",")
                total += int(data[1])
                
        print(f"Total Expense = ₹{total}")
    except FileNotFoundError:
         print("No expenses found yet. Add one first!")
    
def main() :
    """Runs the menu loop and calls the right function based on user choice."""
    menu()
    while True:
        try: 
            choice = int(input("Enter From Menu: "))
            
            if choice == 1:
                add_expense()
            elif choice == 2:
                view_expense()
            elif choice == 3:
                total_expense()
            elif choice == 4:
                break
            else:
                print("invalid choice")            
                continue
                
            except Exception as e:
                print(e)

if __name__ == "__main__" :
    main()