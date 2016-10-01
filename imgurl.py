import re
import urllib

url="http://www.pokemon.com/us/"
a=urllib.urlopen(url)
b=a.read()

pattern=re.compile('<img src="(.*)" a')
c=re.findall(pattern,b)

#print '\n'.join(str(p) for p in c) 

fileptr=open("newfile.txt","w")
for item in c:
	fileptr.write("%s\n" % item)

fileptr.close()

print "The links of the images successfully stored in the file 'newfile.txt'\nOpen the file to access the images\nThank You!\n"