# Function to Calculate the Similarity Value
def Similarity(s1,s2):
    Similarity = len(s1.intersection(s2))/len(s1.union(s2))
    return Similarity

# Function to Remove the Stop Words and convert the sentence to lower case
def RemoveStopWords(s):
    s.lower() # convert to lower case
    # List of Stop Words to remove
    StopWords = ["i","a","an","as","at","the","by","in","for","of","on","that"]
    sentence = set(s.split()) # Removed repeatings words
    newSentence = set()
    for word in sentence:
        if word not in StopWords:
            newSentence.add(word)  # removing the stop words
    return newSentence


# This function is to remove the Punctuations
def RemovePunctuation(s):
    # A list of all possible Punctuations
    PunctuationMarks = ["<",">",",","*","'","\\","(",")",":","{","}","_","-","...","!",".","?","/","[","]",";"]
    sentence = set()
    for word in s:
        if word not in PunctuationMarks:
            sentence.add(word)
    # Returning a punctuation free sentence
    return sentence

# Open and read the first Statement
file1 = open("S1.txt","r")
content1 = file1.read().strip()
file1.close()
sentence1 = RemoveStopWords(content1)   # remove stop words
sentence1 = RemovePunctuation(sentence1)   # remove punctuation

# Open and read the Second statement
file2 = open("S2.txt","r")
content2 = file2.read().strip()
file2.close()
sentence2 = RemoveStopWords(content2)  # remove stop words
sentence2 = RemovePunctuation(sentence2)    # remove punctuation

# Get the Similarity Value as per the formula
SimilarityValue = Similarity(sentence1,sentence2)


# Output
if SimilarityValue==0:
    print("Two Sentences are completely dissimilar")
elif SimilarityValue == 1:
    print("Two Sentences are identical")
else:
    print("Degree of Similarity is: ",SimilarityValue)


