import boto3
import re
# Document
documentName = "test.jpg"

# Read document content
with open(documentName, 'rb') as document:
    imageBytes = bytearray(document.read())

# Amazon Textract client
textract = boto3.client('textract',region_name='us-west-2',aws_access_key_id='access-key-id',aws_secret_access_key='access-key')

# Call Amazon Textract
response = textract.detect_document_text(Document={'Bytes': imageBytes})

#print(response)
card = ' '
# Print detected text
for item in response["Blocks"]: # blocks categorize the text and our text is stored in line
    if item["BlockType"] == "LINE":
        
        x = '\033[94m' +  item["Text"] + '\033[0m'
        card = card + x[5:len(x)-4] +' '
card = card.split()
number=['1','2','3','4','5','6','7','8','9','0','-','+']
num=[]
stre=''


for item in card:
    for n in item:
        if n in number :
            stre+=n
        else:
            if stre not in num:
                num.append(stre)
            stre=''

for i in num:
    if len(i)>=10:
        mobile = i
    

email=[]
website = []
for item in card:
    if 'website' in item.lower():
        website.append(item)

    x=re.match(r'[\w\.-]+@[\w\.-]+',item)
    if x!= None:
        x=x.group(0)
        email.append(x)
'''
email = email[0]
print(mobile)
print(email)
if len(website)>0:
    print(website[0])
'''

print(card)
