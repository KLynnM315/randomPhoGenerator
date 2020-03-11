from bs import beautifulsoup
import urllib2

url = "https://www.pythonforbeginners.com"

content = urllib2.urlopen(url).read()

soup = BeautifulSoup(content)

print (soup.prettify())

print (soup.title.string)

print (soup.p)

print (soup.a)
