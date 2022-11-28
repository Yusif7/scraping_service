import requests
import codecs
from bs4 import BeautifulSoup as BS

url = 'https://rabota.ua/zapros/python/%D0%BA%D0%B8%D0%B5%D0%B2'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Accept': 'text/html, application/xhtml+xml, application/xml;q=0.9,*/*;q=0.8'
}
resp = requests.get(url, headers=headers)


h = codecs.open('test.html','w','utf-8')
# Write incoming information to html 
h.write(str(resp.text))
h.close()        