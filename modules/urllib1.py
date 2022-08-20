import urllib.request, urllib.parse, urllib.error

lst = list()
fhand = urllib.request.urlopen('http://bitcointalk.com')
for line in fhand :
	print(line.strip().decode())