import time

# Account Bank Menu
def Menu(cardNumber,currentPIN,transactions):
    while True:
        print("Bank Account Program")
        print("="*50)
        print('''1. Show account information
2. Change PIN number
3. Withdraw amount of money
4. Deposit amount of money
5. Pay bills
6. View the last transactions
7. Terminate a program
''')
        print("="*50)
        choice = input("Enter Your Feature: ")
        if choice == "1":
            transactions.append(1)
            Show("cardNumber.txt",cardNumber)
        elif choice == "2":
            transactions.append(2)
            changePINFun(currentPIN,cardNumber,"cardNumber.txt")
        elif choice == "3":
            money = float(input("Enter Amount: "))
            transactions.append(3)
            withdrawFun(money,cardNumber,"Balance.txt")
        elif choice == "4":
            transactions.append(4)
            nMoney = float(input("Enter Amount: "))
            depositFun("Balance.txt",nMoney,cardNumber)
        elif choice == "5":
            transactions.append(5)
            nMoney = float(input("Enter the Value of bill: "))
            payBillFun("Balance.txt",nMoney,cardNumber)
        elif choice == "6":
            transactions.append(6)
            viewTransactionFun(cardNumber)
        elif choice == "7":
            transactions.append(7)
            val =  terminateFun(transactions,cardNumber)
            if val == 1:
                break
       
           
    

def LoadData(file):
    with open(file,"r") as file:
        data = file.read().strip().split("\n")
    CustomerData = []
    for i in data:
        CustomerData.append(i.split())
    return CustomerData

# Create account and save information in cardNumber.txt
def create():
    print("="*50)
    print("SIGN-UP")
    print("="*50)
    while True:
        CardNumber = input("Enter Card Number XXXX: ")
        if len(set(CardNumber)) == 4 and sum([1 for i in list(CardNumber) if i.isnumeric()])==4:
            break
        else:
            print("Invalid Card Number")
    while True:
        PIN = input("Enter PIN XXXX: ")
        if len(set(PIN)) == 4 and sum([1 for i in list(PIN) if i.isnumeric()])==4:
            break
        else:
            print("Invalid PIN Number")
    
    while True:
        email = input("Enter your email ")
        if "kfupm.edu.sa" in email.split("@")[1].lower():
            break
        else:
            print("Only KFUPM email is allowed")

    with open("cardNumber.txt","a+") as file:
        file.writelines([str.ljust(CardNumber,10),str.ljust(PIN,10),str.rjust(email,10)+"\n"])
    with open("Balance.txt","a+") as file:
        file.writelines([str.ljust(CardNumber,10),str.ljust('0',10)])
    time.sleep(5)
    
    login()


# Allows the user to login to his saved account
def login():
    print("="*50)
    print("LOGIN")
    print("="*50)
    CustomerData = LoadData("cardNumber.txt")
    transactions = []
    while True:
        CardNumber = input("Enter Card Number XXXX: ")
        if len(set(CardNumber)) == 4 and CardNumber in [i[0] for i in CustomerData]:
            break
        else:
            print("Card Number not found in Customer Data")
    
    while True:
        PIN = input("Enter PIN XXXX: ")
        if len(set(PIN)) == 4 and PIN in [i[1] for i in CustomerData]:
            break
        else:
            print("PIN Number not found in Customer Data")

    Menu(CardNumber,PIN,transactions)

#Will develop later
def Show(file,cardNumber):
    CustomerData = LoadData(file)
    BalanceData = LoadData("Balance.txt")
    data = [i for i in CustomerData if i[0] == cardNumber][0]
    BalanceAmount = [ i for i in BalanceData if i[0] == cardNumber][0]
    print("Card Number: ",cardNumber)
    print("PIN: ",data[1])
    print("Email: ",data[2])
    print("Balance: ",BalanceAmount[1])
    time.sleep(5)
    return


#Change pin feature
def changePINFun(currentPIN,cardNumber,file):
    CustomerData = LoadData(file)
    for data in CustomerData:
        if data[0] == cardNumber and data[1] == currentPIN:
            while True:
                PIN = input("Enter new PIN XXXX: ")
                if len(set(PIN)) == 4 and sum([1 for i in list(PIN) if i.isnumeric()])==4:
                    break
                else:
                    print("Invalid PIN Number")
            index = CustomerData.index(data)
            break
    CustomerData[index][1] = PIN
    with open(file,"w+") as fileHandle:
        for data in CustomerData:
            fileHandle.writelines([str.ljust(data[0],10),str.ljust(data[1],10),str.rjust(data[2],10)+"\n"])
    print("PIN changed successfully")
    time.sleep(5)
    return

# Withdraw Feature
def withdrawFun(money,cardNumber,file):
    CustomerMoneyData = LoadData(file)
    index = -1
    for data in CustomerMoneyData:
        if data[0] == cardNumber and float(data[1]) >= money:
            print("Withdraw for money Rs.",money,"was successful")
            index = CustomerMoneyData.index(data)
            break
    
    if index>-1:
        CustomerMoneyData[index][1] = str(float(CustomerMoneyData[index][1]) - money)
        fileobject = open(file,"w+")
        for data in CustomerMoneyData:
            fileobject.writelines([str.ljust(data[0],10),str.rjust(data[1],10)+"\n"])
    else:
        print("Insufficient Balance in Account")
    time.sleep(5)
    return

# deposit feature
def depositFun(file,nMoney,cardNumber):
    CustomerMoneyData = LoadData(file)
    index = -1
    for data in CustomerMoneyData:
        if data[0] == cardNumber:
            index = CustomerMoneyData.index(data)
            break
    
    if index>-1:
        CustomerMoneyData[index][1] = str(float(CustomerMoneyData[index][1]) + nMoney)
        fileobject = open(file,"w+")
        for data in CustomerMoneyData:
            fileobject.writelines([str.ljust(data[0],10),str.rjust(data[1],10)+"\n"])
        print("Money deposited successfully")
    else:
        print("Invalid Card Number")
    time.sleep(5)
    return

            
            
# Bills Feature
def payBillFun(file,nMoney,cardNumber):
    Bill = input("Enter the name of the bill: ")
    AccountNumber = input("Enter the account number of bill: ")
    
    CustomerMoneyData = LoadData(file)
    index = -1
    for data in CustomerMoneyData:
        if data[0] == cardNumber and float(data[1]) >= nMoney:
            print("Payment of",nMoney,"was successful")
            index = CustomerMoneyData.index(data)
            break
    
    if index>-1:
        CustomerMoneyData[index][1] = str(float(CustomerMoneyData[index][1]) - nMoney)
        fileobject = open(file,"w+")
        for data in CustomerMoneyData:
            fileobject.writelines([str.ljust(data[0],10),str.rjust(data[1],10)+"\n"])
    else:
        print("Invalid Card Number or Insufficient Money")
    time.sleep(5)
    return



# Transaction Feature
def viewTransactionFun(cardNumber):
    file = "Balance.txt"
    try:
        BalanceData = LoadData(file)
    except:
        print("No such file exists")
        return
    index = True
    for i in BalanceData:
        if i[0] == cardNumber:
            print("Card Number:",cardNumber,end="  ")
            print("Balance:",i[1])
            index = False
    if index:
        print("no transactions")
    time.sleep(5)
    return

# Terminate Feature
def terminateFun(file,cardNumber):
    Events = {1:"Show account information",2:"Change PIN number",3:"Withdraw amount of money",4:"Deposit amount of money",5:"Pay bills",6:"View the last transactions",7:"Terminate a program"}
    print("\nEvents occurred\n")
    for i in file:
        print(Events[i])
    return 1


while True:
    val = input("Login (L) or Sign-Up (S) [q to Quit]:")
    with open("Balance.txt","a+") as file:
        pass
    with open("cardNumber.txt","a+") as file:
        pass
    if val.upper()=="L":
        login()
    elif val.upper() == "S":
        create()
    elif val.lower == "q":
        break
    else:
        print("Invalid Input")
    
