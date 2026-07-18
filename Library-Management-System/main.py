'''
library management system
'''
class Library:
    def __init__  (self, name) :
        self.bookList = {}
        self.bookName = name
        
    def menu(self) :
        print('''
        What do you want to do?
        1 to see available books
        2 to add book
        3 to borrow book
        4 to return book
        q to exit\n''')
        
    def availableBook(self) :
        print(f"we have following available now\n")
        found = False
        for book in self.bookList :
            if self.bookList[book]:
                print(book)
                found = True
                
        if not found:
            print("No books available.")
        
    def addBook(self) :
        n = int(input("How many books you want to add? "))
        for i in range(n) :
            book = input("Enter your book name:  ")
            self.bookList[book] = True
        
    def borrowBook(self) :
        book = input("Enter the name of book you want: ")
        if book in self.bookList:
            if self.bookList[book]:
                self.bookList[book] = False
                print("Book borrowed successfully.")
            else:
                print("Book is already borrowed.")
        else:
            print("Book not found.")
        
    def returnBook(self) :
        returning = input("Enter the name of book you want to return: ")
        if returning in self.bookList :
            self.bookList[returning] = True
            print("Book returned sucessfully")
        else :
            print("Not our Library book")
        
    def exitLibrary(self) :
        exit()
    
    def main(self):
        while True:
            self.menu()
            choice = input("Enter your choice: ")
    
            if choice == "1":
                lib.availableBook()
    
            elif choice == "2":
                lib.addBook()
    
            elif choice == "3":
                lib.borrowBook()
    
            elif choice == "4":
                lib.returnBook()
    
            elif choice.lower() == "q":
                print("Thank you!")
                break
    
            else:
                print("Invalid Choice.")


      
if  __name__ ==  '__main__' :
    lib = Library("ayush")
    
    lib.bookList["Atomic Habits"] = True
    lib.bookList["Ikigai"] = True
    lib.bookList["Harry Potter"] = True
    print(f"Welcome to {lib.bookName} library")
    lib.main()