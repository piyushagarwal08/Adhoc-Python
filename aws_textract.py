import boto3

# Document
documentName = "test.jpg"

# Read document content
with open(documentName, 'rb') as document:
    imageBytes = bytearray(document.read())

# Amazon Textract client
textract = boto3.client('textract',region_name='us-west-2',aws_access_key_id='enter - access- key',aws_secret_access_key='enter- secret - key')

# Call Amazon Textract
response = textract.detect_document_text(Document={'Bytes': imageBytes})

#print(response)

# Print detected text
for item in response["Blocks"]:
    if item["BlockType"] == "LINE":
        x = '\033[94m' +  item["Text"] + '\033[0m'
        print(x[5:len(x)-4])