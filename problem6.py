#!/usr/bin/python3

print('''
1. to show contents of single file
2. to show contents of multiple file
3. insert using cat
4. display line numbers in file -n
''')
option = input('Select an option: ')
if option == '1':
	file_name = input('Enter file name: ')
	fhand = open(file_name)
	print(fhand.read())
	fhand.close()
elif option == '2':
	file_name = input('Enter file names: ').split()
	for i in file_name:
		fhand = open(i)	
		print(fhand.read())
		fhand.close()
elif option == '3':
	file_name = input('Enter file name: ')
	fhand = open(file_name,'a')
	text = input('Enter what you want to write: ')
	fhand.write(text)
	fhand.close()
elif option == '4':
	file_name = input('Enter file name: ')
	fhand = open(file_name)
	text = fhand.readlines()
	for i in range(1,len(text)+1):
		print(i,text[i-1])
else:
	print('command not found')
