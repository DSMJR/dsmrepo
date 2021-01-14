import urllib.request
url = input('Enter - ')
fhand = urllib.request.urlopen(url.strip())
for line in fhand:
    print(line.decode().strip())
input('')
