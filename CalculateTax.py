# Code for Single
def Single(TotalIncome):
    TaxIncome = TotalIncome - 12200
    if 0<TaxIncome<=9700:
        Tax = 0.1*TaxIncome
    elif 9700 < TaxIncome <= 39475:
        Tax = 970 + 0.12 * (TaxIncome-9700)
    elif 39475 < TaxIncome <= 84200:
        Tax = 4543 + 0.22*(TaxIncome - 39475)
    elif 84200 < TaxIncome <= 160725:
        Tax = 14382 + 0.24*(TaxIncome - 84200)
    elif 160725 < TaxIncome <= 204100:
        Tax = 32748 + 0.32*(TaxIncome - 160725)
    elif 204100 < TaxIncome <= 510300:
        Tax = 46628 + 0.35*(TaxIncome - 204100)
    else:
        Tax = 153798 + 0.37*(TaxIncome - 510300)
    return TotalIncome-Tax

# code for married filling jointly
def JointMarried(TotalIncome):
    TaxIncome = TotalIncome - 24400
    if 0<TaxIncome<=19400:
        Tax = 0.1*TaxIncome
    elif 19400 < TaxIncome <= 78950:
        Tax = 1940 + 0.12 * (TaxIncome-19400)
    elif 78950 < TaxIncome <= 168400:
        Tax = 9068 + 0.22*(TaxIncome - 78950)
    elif 168400 < TaxIncome <= 321450:
        Tax = 28765 + 0.24*(TaxIncome - 168400)
    elif 321450 < TaxIncome <= 408200:
        Tax = 65497 + 0.32*(TaxIncome - 321450)
    elif 408200 < TaxIncome <= 612350:
        Tax = 93257 + 0.35*(TaxIncome - 408200)
    else:
        Tax = 164709 + 0.37*(TaxIncome - 612350)
    return TotalIncome-Tax

# Code for married filling separately
def SeparateMarried(TotalIncome):
    TaxIncome = TotalIncome - 24400
    if 0<TaxIncome<=9700:
        Tax = 0.1*TaxIncome
    elif 9700 < TaxIncome <= 39475:
        Tax = 970 + 0.12 * (TaxIncome-9700)
    elif 39475 < TaxIncome <= 84200:
        Tax = 4543 + 0.22*(TaxIncome - 39475)
    elif 84200 < TaxIncome <= 160725:
        Tax = 14382.50 + 0.24*(TaxIncome - 84200)
    elif 160725 < TaxIncome <= 204100:
        Tax = 32748.50 + 0.32*(TaxIncome - 160725)
    elif 204100 < TaxIncome <= 306175:
        Tax = 46628.50 + 0.35*(TaxIncome - 204100)
    else:
        Tax = 82354.75 + 0.37*(TaxIncome - 306175)
    return TotalIncome-Tax

# code for single head of household
def HeadOfHousehold(TotalIncome):
    TaxIncome = TotalIncome - 18350
    if 0<TaxIncome<=13850:
        Tax = 0.1*TaxIncome
    elif 13850 < TaxIncome <= 52850:
        Tax = 1385 + 0.12 * (TaxIncome-13850)
    elif 52850 < TaxIncome <= 84200:
        Tax = 6065 + 0.22*(TaxIncome - 52850)
    elif 84200 < TaxIncome <= 160700:
        Tax = 12962 + 0.24*(TaxIncome - 84200)
    elif 160700 < TaxIncome <= 204100:
        Tax = 31322 + 0.32*(TaxIncome - 160700)
    elif 204100 < TaxIncome <= 510300:
        Tax = 45210 + 0.35*(TaxIncome - 204100)
    else:
        Tax = 152380 + 0.37*(TaxIncome - 510300)
    return TotalIncome-Tax

# get user total income
while True:
    try:
        TotalIncome = int(input("What is your total income?\n"))
        break
    except:
        print("please enter only integer value")
# Get user relation
choice = input('''1. Are you single
2. Single head of house
3. Married-FillingSeparately
4. Married-FillingJointly\n''')

# basic if else to print TotalIncome - Tax
if choice == "1":
    print("You will get",Single(TotalIncome),"dollars back")
elif choice == "2":
    print("You will get",HeadOfHousehold(TotalIncome),"dollars back")
elif choice == "3":
    print("You will get",SeparateMarried(TotalIncome),"dollars back")
elif choice == "4":
    print("You will get",JointMarried(TotalIncome),"dollars back")
else:
    print("Invalid Input, please choose(1,2,3,4)")
