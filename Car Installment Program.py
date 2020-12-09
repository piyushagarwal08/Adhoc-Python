def Menu():
    print("CAR INSTALLMENTS PROGRAM")
    print("-"*50)
    print("-"*50)
    print('''1. Add New Customer
2. Display Information for All Customers
3. Display Information for a Customer
4. Eligibility of a Customer
5. Compute Monthly Payment Amount
6. Display Amortization Table
7. Exit
''')
    print("-"*50)
    print("-"*50)
    choice = input("Enter Your Choice: ")
    return choice

def LoadData():
    with open("customer.txt","r") as file:
        content = file.read().strip().split("\n")
    LoadData = []
    for data in content:
        LoadData.append(data.split())
    return LoadData

def CustomerIdExists(CustomerId):
    CustomerData = LoadData()
    for data in CustomerData:
        if CustomerId == data[0]:
            return True
    return False

def FormatStringInput(DataRow):
    DataRow[0] = DataRow[0]+"   "
    DataRow[1] = DataRow[1]+ "   "
    DataRow[2] = DataRow[2]+"\n"
    return DataRow
        
def AddNewCustomer():
    CustomerId = input("Enter Customer ID: ")
    if CustomerIdExists(CustomerId):
        print("This Customer ID already Exists in the system")
    else:
        Salary = input("Enter Salary: ")
        Age = input("Enter Age: ")
        with open("customer.txt","a+") as file:
            file.writelines(FormatStringInput([CustomerId,Salary,Age]))
        print("Customer Successfully Added")
    print()
    return

def DisplayInformationAll():
    print(str.ljust("Customer ID",15),end="")
    print(str.rjust("Salary",5),end="")
    print(str.rjust("Age",5))
    print("-"*50)
    CustomerData = LoadData()
    for data in CustomerData:
        print(str.ljust(data[0],15),end="")
        print(str.rjust(data[1],5),end="")
        print(str.rjust(data[2],5))
    print()
    return

def DisplayCustomerData():
    CustomerId = input("Enter Customer Id: ")
    if CustomerIdExists(CustomerId):
        CustomerData = LoadData()
        print(str.ljust("Customer ID",15),end="")
        print(str.rjust("Salary",5),end="")
        print(str.rjust("Age",5))
        print("-"*50)
        for data in Customer:
            if data[0] == CustomerId:
                print(str.ljust(data[0],15),end="")
                print(str.rjust(data[1],5),end="")
                print(str.rjust(data[2],5))
                break
    else:
        print("Invalid Customer ID")
    return

def CustomerIsEligible(CustomerId):
    if CustomerIdExists(CustomerId):
        CustomerData = LoadData()
        for data in CustomerData:
            if data[0] == CustomerId and int(data[2])<63 and float(data[1]) > 2999:
                print("Customer",CustomerId,"is Eligible")
                print()
                return True
        else:
            print("Customer",CustomerId,"is Not Eligible")
    else:
        print("Invalid Customer ID")
    print()
    return False

def MonthlyPaymentAmount(Loan,Rate,Year):
    NumOfPayment = Year*12
    MonthlyInterestRate = Rate/12
    Term = 1 + MonthlyInterestRate
    MonthlyPaymentAmount = (Loan*MonthlyInterestRate*Term)/(Term-1)
    print("Monthly Payment: SR",MonthlyPaymentAmount)
    print()
    return MonthlyPaymentAmount
        
def DisplayAmortizationTable():
    CustomerID = input("Enter Customer ID: ")
    if CustomerIDExists(CustomerID):
        try:
            Loan = float(input("Loan: "))
            # Loan == Balance
            AnnualRate = float(input("Annual Rate: "))
            Year = int(input("Years: "))
            Data = []
            Months = Year*12
            for i in range(Months):
                MonthlyInterestRate = AnnualRate/12
                MonthlyInterest = MonthlyInterestRate * Loan
                if i == Months-1:
                    Principal = MonthlyPaymentAmount(Loan,AnnualRate,Year) - MonthlyInterest
                else:
                    Principal = Loan
                    MonthlyPayment = Loan + MonthlyInterest
                Balance = Loan - Principal
                Data.append(i+1,MonthlyInterest,Principal,Balance)
        except:
            print("Invalid Input")
    else:
        print("Invalid Customer ID")

    print("Month Interest Principal Balance")
    print("-"*50)
    for data in Data:
        print(str.ljust(data[0],5),end="")
        print(str.rjust(data[1],5),end="")
        print(str.rjust(data[2],5),end="")
        print(str.rjust(data[3],5),end="")

    print()
    return 
                
                    
        
    
while True:
    choice = Menu()
    if choice == "7":
        break
    elif choice == "1":
        AddNewCustomer()
    elif choice == "2":
        DisplayInformationAll()
    elif choice == "3":
        DisplayCustomerData()
    elif choice == "4":
        CustomerId = input("Enter Customer ID: ")
        CustomerIsEligible(CustomerId)
    elif choice == "5":
        CustomerID = input("Enter Customer ID: ")
        if CustomerIsEligible(CustomerID):
            try:
                Loan = int(input("Loan: "))
                Rate = float(input("Annual Rate: "))
                Year = int(input("Years: "))
                MonthlyPaymentAmount(Loan,Rate,Year)
            except:
                print("Invalid Input")
            
        else:
            print("Inavlid Customer ID")
    elif choice == "6":
        DisplayAmortizationTable
    else:
        print("Please enter an valid option [1-7]")


# END of Program
        
