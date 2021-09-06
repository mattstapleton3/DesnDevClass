import urllib.request, urllib.error, urllib.parse

url = 'https://developers.google.com/tech-writing/becoming'

response = urllib.request.urlopen(url)
webContent = response.read()

print(webContent[0:1000])

f = open('scrape.html', 'wb')
f.write(webContent)
f.close()