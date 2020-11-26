# Function To calculate the score
def Score(Correct,Student):
    # Correct is the list of correct answers
    # Student is the list of students answers
    grade = 0  
    for i in range(len(Correct)):
        # check for Answers
        if Correct[i].lower() == Student[i].lower():
            grade = grade + 1.25
    # Returns the grades of particular student
    return grade


# This is the code of the Main Function

# Reading the Input file
file = open("Input.txt","r")
content = file.read().strip().split("\n") # Split the multiple lines into list
CorrectAnswers = content[0].split() # get the list of correct answers
file.close() # Close the Input file connection

# Create a new output file
output = open("Output.txt","w+")
StudentCount = 0 # No of Students above 7 Grade

# Loop and Count the marks of each student
for i in range(1,len(content)):
    studentdata = content[i].split()[1:]  # Options chosen by a particular student
    score = Score(CorrectAnswers,studentdata) # Score generated

    # For students scoring greater then 7
    if score > 7:
        StudentCount = StudentCount + 1

    # Save the Name and Score of particular student
    output.writelines([content[i].split()[0],"   ",str(score),"\n"])

# Store the Total Student data above 7
output.writelines(["Students Above 7 score: ",str(StudentCount)])
# Close the file connection
output.close()
print("Please check the output.txt file")
    
