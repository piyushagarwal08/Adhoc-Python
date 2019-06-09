from bs4 import BeautifulSoup
import webbrowser
import urllib.request, urllib.error, urllib.parse


search = input('Enter text you wish to search for: ')
url = 'https://www.duckduckgo.com/?q='+search
webbrowser.open_new_tab(url)

fhand = urllib.request.urlopen(url)

#print(fhand.getcode())
file = fhand.read()
soup = BeautifulSoup(file,'html.parser')
tag = soup('a')
print(len(tag))
for tags in tag:
    print(tags)
