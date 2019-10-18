import yagmail
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import openpyxl

sender_mail = 'piyushmittal.agarwal2@gmail.com'
#receiver_mail = ['piyushagarwal.0108@gmail.com','akshit.aashrawat@gmail.com']
subject = "Introductory of Lab Equipments"
#password = getpass()
password = ''

# Html Content
html_content='''
<html>
    <body>
    <img src='img1.png'>
    <a href='https://www.google.com'>Google</a>
    </body>
</html>
'''
message = MIMEMultipart('alternative')
content = MIMEText(html_content,'html')
message.attach(content)

yag = yagmail.SMTP(user=sender_mail,password =password)
contents = [yagmail.inline('img1.png'),'Dear Sir/Mam,','Greetings from Pap-Tech Engineers & Associates!',\
'\n','We would like to introduce ourselves 30 year experience as a Designer',\
'\n','Manufacturer and Supplier of Quality Testing Equipment.',\
'\n','\tOur CEO/Paper Technologist Mr. V.K. Agarwal passed out from IIT-Roorkee 1987 batch do all types of consultancy related to Pulp,Paper and Converting Mills.',\
'\n','We Design, Manufacture & supply the followings with Calibration & Repairing services: -',\
 '1.Quality Lab Testing Equipments used in Pulp, Paper, Printing, Packaging, Converting, Adhesives, Chemicals and others.',\
 '2.Calibration & Repairing Services.',\
 '3.AMC Services.',\
 '4. Spare Parts of Testing Equipment i.e. Aluminum Foil & Diaphragm Etc.',\
 '\n','For more information on our products & our company, kindly visit our websites given below .We are enclosing our Product Catalogue with this letter.',\
 '\n','As we are very much interested to do business with you on a long term basis, we request you to please enlist our name in your approved vendor list and send us your valued purchase inquiries from time to time so as to enable us to quote our most competitive rates and terms.',\
 '\n','We would like to welcome the queries from your end. Feel free to have any communication in this regard with us.','\n',\
 '\n','Looking forward for a business association. ','img1.png','img2.jpg','img3.jpg','img4.jpg','img5.jpg','Profile.pdf']

yag.send('piyushagarwal.0108@gmail.com',subject,contents)

#yag.send('piyushagarwal.0108@gmail.com',subject,contents)
# to send mails from excel file
#for i in range(10,row):
 #   mail_id = sheet1.cell(row=i,column=1).value
  #  try:
   #     yag.send(mail_id,subject,contents)
   # except:
    #    continue
    #print(i)

#to send mails from txt file

#with open('mails.txt') as file:
 #   mails = file.readlines()
  #  print(len(mails))
   # for i in mails:
       # i = i.rstrip()
    #    try:
     #       yag.send(i,subject,contents)
      #      print("worked")
       # except:
        #    continue
        #print('test',i)
