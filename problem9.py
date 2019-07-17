#!/usr/bin/python3

from collections import Counter

text = input('Enter some text: ')
if len(text) > 500:
	text = text[0:500]

text_dict = dict(Counter(text))
print('No of repeated characters: ')
for i in sorted(text_dict,key=text_dict.get,reverse=True):
	print(i,text_dict[i])

word_dict = {}
word_text = text.split()
for i in word_text:
	if i in word_dict:
		word_dict[i] = word_dict[i] + 1
	else:
		word_dict[i] = 1
for i in sorted(word_dict,key=word_dict.get,reverse=True):
	print(i,word_dict[i])

for i in word_dict.keys():
	if word_dict[i] >5:
		texts = text.split()
		for j in range(word_dict[i]):
			text.remove(i)
		print(text)
	if word_dict[i] == 1:
		length = len(i)
		if len(text)+length > 500:
			text = text[0:500-length]
			text = text + ' ' + i
		else:
			text = text + ' ' + i
	print(text)

