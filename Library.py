def Menu():
    print("Library Management System")
    print("-"*30)
    print("-"*30)
    print('''    1.Print books info
    2. Search a book
    3. Add new book
    4. Remove a book
    5. Borrow a book
    6. Return a book
    7. Exit
    ''')
    print("-"*30)
    print("-"*30)
    choice = input("Enter your choice: ")
    return choice


def LoadBooksData():
    file = open("booksinfo.txt","r")
    context = file.read().strip().split("\n")
    books = []
    for each in context:
        books.append(each.split(","))
    return books

def PrintBooksInfo():
    books = LoadBooksData()
    print(books)
    for book in books:
        print("S.No:",book[0])
        print("Title:",book[1])
        print("Number of authors:",len(book[2].split(":")))
        print("Price:",book[3])
        print("Total number of copies:",int(book[4])+int(book[5]))
        print()
    return

def SearchBook(search):
    books = LoadBooksData()
    for book in books:
        if search.lower() in book[1].lower():
            print("S.No:",book[0])
            print("Title:",book[1])
            print("Author:",",".join(book[2].split(":")))
            print("Price:",book[3])
            print("Total number of copies:",int(book[4])+int(book[5]))
            print()
        authors = book[2].split(":")
        for author in authors:
            if search.lower() in author.lower():
                print("S.No:",book[0])
                print("Title:",book[1])
                print("Author:",",".join(book[2].split(":")))
                print("Price:",book[3])
                print("Total number of copies:",int(book[4])+int(book[5]))
                print()
                break
    return

def GetSerialNumber(Serial):
    books = LoadBooksData()
    serialNumber = [i[0].lower() for i in books]
    if Serial.lower() in serialNumber:
        return False
    else:
        return True


def AddNewBook(NewBook):
    print(NewBook)
    try:
        
        file = open("booksinfo.txt","a+")
        for i in range(len(NewBook)):
            NewBook[i] = NewBook[i]+","
            
        file.writelines(NewBook)
        
        file.close()
        return NewBook[1]+" has been added Successfully"
    except:
        return NewBook[1]+" has not been added due to some error"

def DisplayBook(SerialNumber):
    books = LoadBooksData()
    for book in books:
        if book[0].lower() == SerialNumber.lower():
            print("S.No:",book[0])
            print("Title:",book[1])
            print("Author:",",".join(book[2].split(":")))
            print("Price:",book[3])
            print("Total number of copies:",int(book[4])+int(book[5]))
            print()
    return


def RemoveBook(SerialNumber):
    file = open("booksinfo.txt","rw")
    context = file.read().strip().split("\n")
    books = []
    for each in context:
        books.append(each.split(","))
    for book in books:
        if book[0]==SerialNumber and book[-1]=="0":
            continue
        else:
            for i in range(len(book)):
                book[i] = book[i]+","
            file.writelines(book)
    file.close()

def BorrowBook(UID,SerialNumber):
    file = open("borrowedinfo.txt","wr")
    context = file.read().strip().split("\n")
    if [UID,SerialNumber] in context:
        return "You cannot borrow the same book again"
    borrow = 0
    for borrow in context:
        if SerialNumber.lower() in borrow[0].lower():
            borrow = borrow +1
    if borrow >=3:
        return "You cannot borrow more then 3 books"

    if checkAvailableBooks(SerialNumber):
        file.writelines([UID+",",SerialNumber])
        return "Book has been borrowed successfully"
    else:
        return "Book is not borrowed successfully"
    

def checkAvailableBooks(SerialNumber):
    books = LoadBooksData()
    for book in books:
        if SerialNumber.lower() == book[0].lower() and int(books[-2])-int(books[-1]) >0:
            availableBook = int(books[-2])-1
            borrowedBook = int(books[-1]) + 1
            book[-2] = availableBok
            book[-1] = borrowedBook
        file = open("booksinfo.txt","a+")
        for i in range(len(books)):
                books[i] = books[i]+","
        for book in books:
            file.writelines(books)
        flag = True
    if flag:
        return True
    else:
        False
            
            
    

choice = ""
while choice != "7":
    choice = Menu()
    if choice == "1":
        PrintBooksInfo()
    elif choice == "2":
        search = input("Enter Title or Author Name: ")
        SearchBook(search)
    elif choice =="3":
        SerialNumber = input("Enter a 5 digit S.No: ")
        Title = input("Enter the title of book: ")
        author = input("Enter authors name (Separate multiple names using comma)").split(",")
        try:
            price = float(input("Enter the price: "))
        except:
            print("Invalid Price format, it should be in float value")
        try:
            Copies = int(input("Enter number of copies"))
        except:
            print("Enter only integer value")
            
        if len(SerialNumber) != 5 and GetSerialNumber(SerialNumber):
            print("Invalid Serial Number")
        if len(Title)<1:
            print("Invalid Title")
        if len(author)<1:
            print("Enter atleast one author name")
        if Copies<1:
            print("Atleast one copy should be added")
        else:
            NewBook = [SerialNumber,Title,':'.join(author),str(price),str(Copies),"0"]
            message = AddNewBook(NewBook)
            print(message)        
    elif choice == "4":
        SerialNumber = input("Enter an valid Serial Number: ")
        if len(SerialNumber) != 5 and not GetSerialNumber(SerialNumber):
            DisplayBook(SerialNumber)
            while(True):
                remove = input("Are you Sure you want to remove: Y/N")
                if remove=="Y" or remove=="N":
                    break
            if remove=="Y":
                RemoveBook(SerialNumber)
        else:
            print("Such Book does not exist in system")

    elif choice == "5":
        SerialNumber = input("Enter the Serial Number: ")
        if not GetSerialNumber(SerialNumber):
            UID = input("Enter your User ID: ")
            print(BorrowBook(UID,SerialNumber))
        else:
            print("There is no such book in out records")
    elif choice == "6":
        SerialNumber = input("Enter Serial Number : ")
        UID = input("Enter your Serial Number")
        file = open("borrowedinfo.txt","r")
        context = file.read().strip().split("\n")
        if [SerialNumber,UID] not in context:
            print("You have not borrowed such an book")
        else:
            print("Book has been returned successfully")
    elif choice == "7":
        break
    else:
        print("Invalid Menu Option")
            
        
    
