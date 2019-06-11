#!/usr/bin/python3

import os
import text_to_speech as say
no_repeat = []
for i in range(3):

	command = input('Enter a command: ')
	if command in no_repeat:
		say.speak("Don't Repeat the command again")
	else:
		no_repeat.append(command)
		os.system(command+' 2>error.txt')
		os.system(command+' &> command.txt')
	os.system('rm -r error.txt')
