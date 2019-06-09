#Problem Statement: Search on google and take out top 5 links in a list.Again search these links and take out
#		    their top 5 links in a list and print the 5 lists.



# Solution : 

from googlesearch import search

#Take Input
data=input("Enter your search query : ")

#Create Empty Lists
mylist1=[]
mylist2=[]
mylist3=[]
mylist4=[]
mylist5=[]
mylist6=[]
    
#First_Search
for i in search(data,tld="co.in",lang='en',num=5,start=0,stop=5,pause=2):
    mylist1.append(i)

#print(mylist1)

#Search the first link of First_Search and append the results in a list
for i in search(mylist1[0],tld="co.in",lang='en',num=5,start=0,stop=5,pause=2):
    mylist2.append(i)

#Search the Second link of First_Search and append the results in a list
for i in search(mylist1[1],tld="co.in",lang='en',num=5,start=0,stop=5,pause=2):
    mylist3.append(i)

#Search the Third link of First_Search and append the results in a list
for i in search(mylist1[2],tld="co.in",lang='en',num=5,start=0,stop=5,pause=2):
    mylist4.append(i)

#Search the Fourth link of First_Search and append the results in a list
for i in search(mylist1[3],tld="co.in",lang='en',num=5,start=0,stop=5,pause=2):
    mylist5.append(i)

#Search the Fifth link of First_Search and append the results in a list
for i in search(mylist1[4],tld="co.in",lang='en',num=5,start=0,stop=5,pause=2):
    mylist6.append(i)

#Print all the lists
print(mylist2)
print( )
print(mylist3)
print( )
print(mylist4)
print( )
print(mylist5)
print( )
print(mylist6)
