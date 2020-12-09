# Get Title from user
Title = input("Enter a title for the data:\n")
print("You entered:",Title)

# Get column 1 header
Column1 = input("Enter the column 1 header:\n")
print("You entered:",Column1)

# Get column 2 header
Column2 = input("Enter the column 2 header:\n")
print("You entered:",Column2)

#List data structure to store our DataPoints
DataPoints = []

while True:
    # Take Input from user
    DataPoint = input("Enter a data point (-1 to strop input:)\n")

    # Condition to stop taking input
    if DataPoint == "-1":
        break
    # Code for input validation
    elif "," not in DataPoint:
        print("Error: No comma in string.")
        continue
    elif DataPoint.count(",") > 1:
        print("Error: Too many commas in input.")
        continue
    try:
        # Convert and save data in string and integer variables
        IntegerValue = int(DataPoint.split(",")[1])
        StringValue = DataPoint.split(",")[0]
        # Save the data in list
        DataPoints.append([StringValue,IntegerValue])
    except:
        print("Error: Comma not followed by an integer.")


# Print the required structure
# str.center(string,width) -> "          string           "
# str.ljust(strig,width) -> "string         "
#str.rjust(string,width) -> "         string"
print(str.center(Title,33))
print(str.ljust(Column1,20),end="|")
print(str.rjust(Column2,23))
print("-"*(len(Title)+33))

# Plot the data into structure
for data in DataPoints:
    print(str.ljust(data[0],20),end="|")
    print(str.rjust(str(data[1]),23))

print() # for a new line

# plot the hologram
for data in DataPoints:
    print(str.rjust(data[0],20),end=" ")
    print("*"*data[1])

# End of Program
