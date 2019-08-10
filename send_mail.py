#!/usr/bin/python3
import smtplib
s = smtplib.SMTP('smtp.gmail.com',535)
s.ehlo()
s.starttls()
message = 'Enter any message in this'
s.login('piyushmittal.agarwal2@gmail.com','gorfotes')
s.sendmail('piyushmittal.agarwal2@gmail.com','piyushagarwal.0108@gmail.com',message)
s.quit()

