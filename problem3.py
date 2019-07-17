#!/usr/bin/python3
adhoc = [1,2,3,1,4,5,66,22,2,6,0,9]
five = [i for i in adhoc if i > 5]
two = [i for i in adhoc if i <= 2]
print('Numbers greater then 5')
for i in five:
	print(i)
print(five)
print('Numbers less than or equals to 2')
for i in two:
	print(i)
print(two)

