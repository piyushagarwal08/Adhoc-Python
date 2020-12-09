# A Dictionary of List of Product Names
ProductList = {"1":"Red-Hot Spicy Doritos","2":"Cool Ranch Doritos",\
               "3":"Coke","4":"Diet Coke","5":"Pepsi","6":"Five Hour Energy",
               "7":"Sunflower Seeds","8":"Peanuts","9":"Mac Book Chargers",\
               "10":"Dell Chargers"}

# A Dictionary of cost of products
ProductCost = {"Red-Hot Spicy Doritos":2.99,"Cool Ranch Doritos":2.99,\
               "Coke":0.99,"Diet Coke":0.99,"Pepsi":0.99,"Five Hour Energy":3.99,
               "Sunflower Seeds":0.99,"Peanuts":0.99,"Mac Book Chargers":120,\
               "Dell Chargers":50}

# A List to store all the users purchases to be displayed at the end of the program
DataBase = []
TotalAmount = {}

print("Welcome to the Start of program:")
ProductsPurchased = []  # List to store the names of purchased products
Quantity = []   # Amount of each product purchased

# Function to display the user slip
# User is an list of list [[list of Products Purchased],[Quantity of each product]]
def Display(User):
    TotalCost = 0
    ProductsPurchased = User[0]  
    Quantity = User[1]
    # Creating the slip structure
    print("Here is your order list")
    print("="*60)
    print(str.ljust("Product Name",20),end="")
    print(str.ljust("Quantity",30),end="")
    print(str.ljust("Price",20))
    print("="*60)

    # Print each slip for user                                 
    for index in range(len(ProductsPurchased)):
        print(str.ljust(ProductsPurchased[index],20),end="")  # product name
        print(str.ljust(str(Quantity[index]),30),end="")   # Product quantity 
        print(str.ljust(str(Quantity[index]*ProductCost[ProductsPurchased[index]]),20))   # Total Price
        TotalCost = TotalCost + Quantity[index]*ProductCost[ProductsPurchased[index]]
    print(str.ljust("Total Amount",50),end="")
    print(TotalCost)
    print("="*60)
    return

# Main Program
while True:
    print("Choose any product to purchase:")
    # List of menu card
    product = input('''1. Red-Hot Spicy Doritos
2. Cool Ranch Doritos
3. Coke
4. Diet Coke
5. Pepsi
6. Five Hour Energy
7. Sunflower Seeds
8. Peanuts
9. Mac Book Chargers
10. Dell Chargers
0. New User
-1. Show Complete Receipts
''')
    # 0 to indicate a new user
    # Before asking input for new user -> show slip of current user
    if product == '0':
        DataBase.append([ProductsPurchased,Quantity])
        Display([ProductsPurchased,Quantity])  # current user slip displayed
        ProductsPurchased = []
        Quantity = []
        print("="*60)
        print("Enter entry for new user")

    # At the end of day, to get slip of every user
    elif product == "-1":
        # if its the last user of day show his slip as well first
        if len(ProductsPurchased) != 0:
            DataBase.append([ProductsPurchased,Quantity])
            Display([ProductsPurchased,Quantity])

        print("Complete Order list of Today")
        count = 0  # no of users
        for i in DataBase:
            if len(i[0]) == 0:
                continue
            count = count + 1
            print("Customer:",count)
            for product in range(len(i[0])):
                if TotalAmount.get(i[0][product],0):
                    TotalAmount[i[0][product]] = TotalAmount[i[0][product]] + i[1][product]
                else:
                    TotalAmount[i[0][product]] = i[1][product]
            Display(i)
        break
    elif product in ["1","2","3","4","5","6","7","8","9","10"]:
        NoOfItems = int(input("Enter no of items you would like to purchase for the same: "))
        ProductsPurchased.append(ProductList[product])
        Quantity.append(NoOfItems)
    else:
        print("Invalid Input")

# Total Sales of the day
GrandTotal = 0
print("Amount Sold for Each item")

# Print the required values
for item,quantity in TotalAmount.items():
    print(str.ljust(item,20),end="")  # product name
    print(str.ljust(str(quantity),30))   # Product quantity
    GrandTotal = GrandTotal + ProductCost[item]*quantity
print("Grand Total: ",GrandTotal)

