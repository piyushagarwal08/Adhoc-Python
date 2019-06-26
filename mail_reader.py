import imaplib
import email

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('gmail-email','g-mail-pass')
mail.select('INBOX')
result,data = mail.search(None,"ALL")
id_list = data[0].split()
latest_mail = id_list[-1]
result,data = mail.fetch(latest_mail,"(RFC822)")
raw_mail = data[0][1]
message = email.message_from_string(raw_mail)
with open('latest_mail.txt','w+') as file:
    file.write(str(message))
print 'From: ' + message['From']
print 'To: ' + message['To']
print 'Subject: ' + message['Subject']
