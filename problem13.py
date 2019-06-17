import pyttsx3
import time
import os

def speak(x):
    tts = pyttsx3.init()
    tts.say(x)
    tts.runAndWait()
speak('Welcome Pykid')

def greet(x):
    if hour < 12:
        return 'good morning'
    elif hour < 16 and hour >= 12:
        return 'good afternoon'
    elif hour <20 and hour >= 16:
        return "good evening"
    else:
        return "good night"
hour=time.localtime().tm_hour
wish = greet(hour)
speak(wish)
print('''
1. type add(4,5,3,6) to add any amount of numbers
2. type sort_num(4,5,3,5,2,4) to sort list of numbers
3. type module() to list installed modules
''')

def add(*x):
    return sum(x)


def sort_num(*x):
    return sorted(x)

def module():
    os.system('pip3 list')
