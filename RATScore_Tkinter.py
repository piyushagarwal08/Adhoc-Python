from tkinter import *
from tkinter import ttk
import random # to generate random RAT Score

# Function to display the summary of RAT Score File
def ScoreSummarize(RATScore,Count):
    # Convert all RAT Score values to integer
    RATScore = list(map(int,RATScore))
    # Create another window
    window1 = Tk()
    window1.title("Output")
    window1.configure(background="grey")

    # The labels
    b = Label(window1,text = "Number of Scores added: "+str(Count)).grid(row = 0, column= 0)
    b = Label(window1,text = "Number of Scores in file: "+str(len(RATScore))).grid(row = 1,column = 0)
    b = Label(window1,text = "Average RAT Score: "+str(sum(RATScore)/len(RATScore))).grid(row = 2, column = 0)
    # A button to close the Screen
    btn1 = ttk.Button(window1 ,text="Close",command=window1.destroy).grid(row=4,column=0)
    return


window = Tk()

#Your name - Objective
Title = "Chegg Expert - TO Solve the Assignment"

window.title(Title)
window.geometry('400x400') # configure to change the window size
window.configure(background = "grey"); # color of background

# Label as asked in question
a = Label(window ,text = "Student ID").grid(row = 0,column = 0)
a1 = Entry(window)
a1.grid(row = 0,column = 1)

# If Submit button is clicked
def clicked():
    # Get user-StudentId
    StudentId = a1.get()
    # If no input then no action required
    if len(StudentId)==0:
       return
    # check if file exists or not
    try:
        file = open(StudentId+".txt","r+")
        RATScore = file.read().strip().split("\n") # read the content
    # if not then just create the file
    except:
        file = open(StudentId+".txt","a+")
        RATScore = []

    # if already entered 5 RAT Scores, just print summary
    if len(RATScore) == 5:
        ScoreSummarize(RATScore,0)
    # if not 5 entries
    else:
        Score = random.randrange(0,10) # generate random RAT Score between 0 and 10
        file.write(str(Score)+"\n")  # write it in file
        RATScore.append(str(Score)) 
        ScoreSummarize(RATScore,1)  # Print the summary
    file.close() # close the file
    return     

# button to re-submit entry
btn = ttk.Button(window ,text="Submit", command=clicked).grid(row=1,column=0)
btn2 = ttk.Button(window,text="Close",command=window.destroy).grid(row=1,column=1)
window.mainloop()
