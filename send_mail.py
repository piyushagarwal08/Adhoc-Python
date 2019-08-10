#!/usr/bin/python3
import smtplib
s = smtplib.SMTP('smtp.gmail.com',535)
s.ehlo()
s.starttls()
message = 'Enter any message in this'
s.login('sender mail','passeord')
s.sendmail('sender mail','recievermail',message)
s.quit()

