import urllib2

response = urllib2.urlopen('http://python.org/')
f = open("httptext.html", "a")
for line in response:
    f.write(line + '\n')
f.flush()
f.close()
