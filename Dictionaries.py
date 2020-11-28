
# This function is used to create your first dictionary
def TeamWinCountDict():
    file = open("Data.txt","r")  # Please change the file path as per your input file
    content = file.read().strip().split("\n") # loading the data in program
    file.close()
    TeamWinCount = dict() # initializing variable
    for i in content:
        if TeamWinCount.get(i,False):
            TeamWinCount[i] = TeamWinCount[i] + 1
        else:
            TeamWinCount[i] = 1
    # return a dictionary with {"Team name": Win Count"} format
    return TeamWinCount

# This function is used to create your second dictionary
def YearBasedDict():
    file = open("Data.txt","r")  # Please change the file path as per your input file
    content = file.read().strip().split("\n")  # loading the data in program
    file.close()
    YearDict = dict()  # initializing variable
    year = 1903   # The year is to start from 1903 as in question
    for i in content:
        if year == 1904 or year == 1994:
            year = year + 1
            continue
        YearDict[year] = i
        year = year + 1
    # returning year based dictionary is ready {year:"team name"}
    return YearDict

# Function to take input from user
def Input():
    # checks for proper year value taken as user input
    while True:
        try:
            year = int(input("Enter year value in the range of 1903 and 2018: "))
        except:
            print("Invalid Year")
            continue
        if year == 0:
            break
        # if year is 1904 or 1994, re ask user for input as no match was played
        if year == 1904 or year == 1994:
            print("No match was played in this year")
        elif year>=1903 and year <= 2018:
            break
        else:
            print("Invalid Year")
    return year

# Function to give output to user
def Output(year):
    # calling above functions to retrieve required data
    YearBasedData = YearBasedDict()
    TeamWinData = TeamWinCountDict()
    # Get function returns a default value if key not found
    TeamName = YearBasedData.get(year,"No Data Found")
    # print the output to user
    print("The Team that won:",TeamName,"with a total win count:",TeamWinData.get(TeamName,"No Data Found"))
    return

# this is your main function
def Main():
    while True:
        # calling the input function
        year = Input()
        if year == 0:
            print("Program ended successfully")
            break
        # calling the output function
        Output(year)
Main()
'''
------------------------------------------------
Developer Info
------------------------------------------------

This area can be used to give your personal info as comment



-------------------------------------------------
'''
