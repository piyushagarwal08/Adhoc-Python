#!/usr/bin/python3
import time
name = input('Enter your name: ')
age = int(input('Enter your age: '))
years = 95 - age
print(f'{name} you will turn 95 in year',time.localtime().tm_year+years)

          
