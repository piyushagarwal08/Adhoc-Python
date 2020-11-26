# required to check the mobile and email
# please install in system using pip install re
# please create two files donations.txt and blood.txt (empty or filled)


import re

# It Includes the main function
def Main():
    # display Message
    while True:
        print('''------------------------------------------------------------
1. Add new donor
2. Display information for All donors
3. Display information for a specific donor (update - delete)
4. Receive blood
5. Display available blood packets
6. Exit
-------------------------------------------------------------''')
        choice = input("Choose an option: ")
        if choice == "1":
            AddNewDonor()
        elif choice == "2":
            DisplayAll()
        elif choice =="3":
            DonorId = input("Enter Donor ID: ")
            if DonorIdExists(DonorId):
                DisplayInfo(DonorId)
            else:
                print("Invalid Donor ID")
        elif choice == "4":
            ReceiveBlood()
        elif choice == "5":
            DisplayAvailableBloodPackets()
        elif choice == "6":
            print("Thank You")
            break
        else:
            print("Invalid Option")
    
# Display all Blood Bank Data
def DisplayAll():
    BloodData = LoadData()
    for data in BloodData:
        print("  ".join(data))
    return

# Load the Blood Bank Data
def LoadData():
    file = open("Blood.txt","r")
    content = file.read().strip().split("\n")
    file.close()
    BloodData = []
    for i in content:
        BloodData.append(i.split())
    if len(BloodData)>0:
        return BloodData
    return False

# For adding data in proper format
def AddSpace(Data):
    NewData = []
    for i in Data:
        NewData.append(i+"  ")
    return NewData

#Validate all mobile numbers
def MobileValid(s):
    Pattern = re.compile("(0/91)?[7-9][0-9]{9}")
    return Pattern.match(s)

# Validate email 
def EmailValid(s):
    Pattern = re.compile("^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$")
    return Pattern.match(s)

# Check if Donor Id exists
def DonorIdExists(s):
    BloodData = LoadData()
    if not BloodData:
        return False
    for i in BloodData:
        if i[0] == s:
            return True
    return False
    
# Add new donor details
def AddNewDonor():
    while True:
        DonorID = input("Enter Donor Identification Number: ")
        if not DonorIdExists(DonorID):
            break
        else:
            print("Donor ID Exists")
    Name = input("Enter Donor's Name: ")
    DOB = input("Enter DOB (dd/MM/yyyy): ")
    while True:
        BloodGroup = input("Enter Blood Group: ")
        if len(BloodGroup)<=3:
            break
        else:
            print("Invalid Blood group")
    Address = input("Enter Address: ")
    while True:
        Mobile = input("Enter Mobile Number: ")
        if MobileValid(Mobile):
            break
        else:
            print("Incorrect Mobile Number")
    while True:
        Email = input("Enter Email Address: ")
        if EmailValid(Email):
            break
        else:
            print("Invalid Email Address")
    while True:
        Gender = input("Enter your gender(M/F/O): ")
        if Gender in ["M","F","O"]:
            break
        else:
            print("Please enter only M/F/O")
    City = input("Enter your City: ")
    file = open("Blood.txt","a+")
    file.writelines([DonorID," ",Name," ",Gender," ",BloodGroup.upper()," ",City," ",DOB," ",Address," ",Mobile," ",Email])
    file.close()

# Displat info
def DisplayInfo(DonorId):
    print('''1 Sort by ID
2 Sort by Name
3 Sort by Gender
4 Sort by Blood Group
5 Sort by City
''')
    BloodData = LoadData()
    for i in BloodData:
        if i[0] == DonorId:
            Data = i
    
    choose = input("Please choose an option: ")
    Data.sort(key = lambda BloodData: BloodData[int(choose)-1])
    print("   ".join(Data))
    choose1 = input('''1. Update donor information
2. Delete donor information
0. Back to the main menu''')
    if choose1 == "1":
        UpdateDonorInfo(DonorId)
    elif choose1 == "2":
        DeleteDonorInfo(DonorId)
    return

# update donor data
def UpdateDonorInfo(DonorId):
    BloodData = LoadData()
    file = open("Blood.txt","w")
    for data in BloodData:
        if data[0] == DonorId:
            index = BloodData.index(data)
            print("Name:",data[1])
            update = input("New Name: ")
            if len(update)>0:
                BloodData[index][1] = update
                
            print("City:",data[4])
            update = input("New City: ")
            if len(update)>0:
                BloodData[index][4] = update
                
            print("Name:",data[6])
            update = input("New Address: ")
            if len(update)>0:
                BloodData[index][6] = update

            print("Name:",data[7])
            update = input("New Mobile: ")
            if len(update)>0 and MobileValid(update):
                BloodData[index][7] = update

            print("Name:",data[8])
            update = input("New Email: ")
            if len(update)>0 and EmailValid(update):
                BloodData[index][8] = update

    for data in BloodData:
        file.writelines(Data)
    print("Information Updated Successfully")

# delete donor data
def DeleteDonorInfo(DonorId):
    option = print("You wish to delete your data(Y/N): ")
    if option.lower() == "y":
        BloodData = LoadData()
        file = open("Blood.txt","w+")
        for data in BloodData:
            if data[0] == DonorId:
                index = BloodData.index(data)
                break
        BloodData.pop(index)
        for data in BloodData:
            file.writelines(AddSpace(data))
        file.close()
    else:
        print("You wish not to delete")
        
    return

# load data for donated data
def LoadDonatedData():
    file = open("donations.txt","a+")
    content = file.read().strip().split("\n")
    DonatedData = []
    for each in content:
        DonatedData.append(each.split())
    if len(DonatedData)>0:
        return DonatedData
    return False

# receive donor data
def ReceiveBlood():
    DonatedData = LoadDonatedData()
    file = open("donations.txt","a+")
    DonorId = input("Enter your DonorId: ")
    DonationDate = input("Enter the Donation Date (dd/MM/yyyy): ")
    PacketSize = input("Enter packet size: ")
    file.writelines(AddSpace([DonorId,DonationDate,PacketSize]))
    file.close()
    print("Date Added Successfully")
    return

# display all blood packets
def DisplayAvailableBloodPackets():
    DonatedData = LoadDonatedData()
    for data in DonatedData:
        print("  ".join(data))
    return
        
# This is executing the Main Function
Main()
