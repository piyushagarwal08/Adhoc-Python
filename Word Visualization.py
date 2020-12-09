import string


def DataVisualization(sortedcounts):
    # counter to check that only 4 columns are printed
    colcount = 0
    for word,count in sortedcounts:
        colcount = colcount + 1

        # Using String formatting to print the desired structure
        # str.ljust(string,width) -> "string<----width---->"
        OutputString = str(count)+":"+word
        print(str.ljust(OutputString,30),end="")

        # print new line after 4 columns
        if colcount % 4 == 0:
            print("\n")
    # to hold the screen for an enter
    print()
    while True:
        enter = input("\nPlease type enter to exit...")
        if len(enter) > 0:
            break
    return

filename = input("Please enter the file name: ") #ask the user which file do he/she wants to open

openfile = open(filename, "r") #open the file

readfile = openfile.read() #read the file

words = readfile.split() #split the file

wordlist = [] #make a counter

for text in words:

   striptext = text.strip()

   puncstrip = striptext.strip(string.punctuation)

   wordlist.append(puncstrip)

#for the stopwords

dictionary = dict()

stopfile = open("stopwords.txt")

readstopfile = stopfile.read()

stopword = readstopfile.split()

counts = {} #accumulator for empty dictionary

for y in wordlist:

   y = y.strip()

   y = y.lower()

   if y in counts and y not in stopword:

      counts[y] += 1

   elif y not in counts and y not in stopword:

      counts[y] = 1

sortedcounts = sorted(counts.items(), key = lambda i: i[1], reverse=True)[:56]

print(len(sortedcounts), "words in frequency order as (count:word) pairs")



#print(sortedcounts)
print()
# The function i have added
DataVisualization(sortedcounts)
