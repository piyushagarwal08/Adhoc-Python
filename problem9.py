#!/usr/bin/python3

from collections import Counter

text = input('Enter some text: ')
if len(text) > 500:
	text = text[0:500]
text_dict = dict(Counter(text))
print('No of repeated characters: ')
for i in sorted(text_dict,key=text_dict.get,reverse=True):
	print(i,text_dict[i])

