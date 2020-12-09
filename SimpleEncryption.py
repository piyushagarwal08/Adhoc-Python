# Required Modules Imported
import sys  # To close the program with incorrect Values such as non existing text files
from collections import Counter as C # for frequency count

# Encryption Function
def Encrypt(InputString,ShiftValue):
    # Converting given string in an list for easy maipulation
    result = list(InputString)

    # Iterate over List and encrypt each character
    for i in range(len(InputString)):
        OrdValue = ord(result[i]) # Current ascii value, a = 97 b = 98
        newValue = OrdValue - ShiftValue  # New ascii value
        # manipulating if new value is not in b/w a-z
        if newValue < 97:
            cal = 97 - newValue
            result[i] = chr(123 - cal)
        else:
            result[i] = chr(newValue)
    #return the encrypted text
    return ''.join(result)

# Decryption Function
def Decrypt(InputString,ShiftValue):
    # Converting given string in an list for easy maipulation
    result = list(InputString)

    # Iterate over List and decrypt each character
    for i in range(len(InputString)):
        OrdValue = ord(result[i])   # Current ascii value, a = 97 b = 98
        newValue = OrdValue + ShiftValue  # New ascii value
        # manipulating if new value is not in b/w a-z
        if newValue > 122:
            cal = newValue - 122
            result[i] = chr(96 + cal)
        else:
            result[i] = chr(newValue)
    # return the decrypted text
    return ''.join(result)
    
# Function to calculate the Shift Value
def CalShiftValue(InputString,CharacterCount):
    wordCount = [] # List to count, repeating words
    wordlist = InputString.split()
    for i in wordlist:
        if i not in wordCount:
            wordCount.append([i,InputString.count(i)])
    
    list1 = [] # List to contain (word,repeating-count,sum-of-characters)
    for i in wordCount:
        sum1 = 0
        for j in i[0]:
            sum1 = sum1 + CharacterCount[j]
        list1.append([i[0],i[1],sum1])

    maxValue = -1 # default max value

    # find the max possible shift value
    for i in list1:
        if i[1]*i[2] > maxValue:
            maxValue = i[1]*i[2]
            
    # return the calculated Shift Value as per the formula given
    return maxValue%26

# Main Function
# To make sure user can only input d - decryption or e - encryption
while True:
    choose = input("Please choose 'e' for encryption and 'd' for decryption ")
    if choose == 'e' or choose == 'd':
        break
    else:
        print("Invalid Input")

# Code for Encyption Process
if choose == "e":
    # Get the File Name, make sure the complete name is given with extension
    FileName = input("Please input the name of the plain text file: ")
    # In case Input File is not found, the program will stop with error message
    try:
        with open(FileName,"r") as file:
            content = file.read().strip()
    except:
        print("No Such File Found")
        sys.exit() # to stop the program

    #Manipulating File Content to remove non-alpha characters including " "(space)
    InputString = []
    for i in content:
        if i.isalpha():
            InputString.append(i)
    content = ''.join(InputString)

    # Set the string to lower case
    content.lower()
    # Calculate the frequency count of each character
    CharacterCount = dict(C(content))
    # Calulate the Shift Value using function
    ShiftValue = CalShiftValue(content,CharacterCount)

    # Print the Values as Asked in Question
    print("Frequencies of each character",CharacterCount)
    print("Shift Value: ",ShiftValue)

    # Get the encrypted text
    EncryptedText = Encrypt(content,ShiftValue)

    # Get the output file name with .txt extension
    CipherTextFile = input("Input the name of the Cipher Text File: ")
    with open(CipherTextFile,"w") as file:
        file.write(EncryptedText) # write the output in file

# For Decryption    
else:
    #  The process is completely similar in reverse order
    CipherTextFile = input("Input the name of the Cipher Text File: ")
    try:
        with open(CipherTextFile,"r") as file:
            content = file.read().strip()
    except:
        print("No Such File Found")
        sys.exit()
    
    CharacterCount = dict(C(content))
    ShiftValue = CalShiftValue(content,CharacterCount)
    
    print("Frequencies of each character",CharacterCount)
    print("Shift Value: ",ShiftValue)
    
    FileName = input("Please input the name of the plain text file: ")
    with open(FileName,"w") as file:
        # Decrypt(content,ShiftValue) will get the decrypted text and save in file
        file.write(Decrypt(content,ShiftValue)) # Output Saved
    
# The End, hope it would be helpful
