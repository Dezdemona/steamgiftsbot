import lxml.html
import requests

fo = open('cookie.txt',"r+")
fo = fo.read()

address = ('http://www.steamgifts.com')

cookies = dict(PHPSESSID=fo)

r = requests.post(address, cookies=cookies)

pageReady = r.text
xmldata = lxml.html.document_fromstring(pageReady)

links = xmldata.xpath('//div[@class="ajax_gifts"]//div[@class="title"]/a/@href')
nav = xmldata.xpath('//div[@id="navigation"]/ol/li/a/text()')

nav1 = nav[2]
points = int(nav1[9:-2])

print ("Points before entering: " + str(points))

r = requests.post(address + links[1], cookies = cookies)

pageReady = r.text
xmldata = lxml.html.document_fromstring(pageReady)

form_key = xmldata.xpath('//input[@name ="form_key"]/@value')

form_key = form_key[0]

payload = {"form_key": form_key, "enter_giveaway":"1"}

r = requests.post(address + links[0], cookies = cookies, data = payload)

for i in range (40):
    r = requests.post(address + links[i], cookies=cookies, data = payload)
    pageReady = r.text
    xmldata = lxml.html.document_fromstring(pageReady)
    nav = xmldata.xpath('//div[@id="navigation"]/ol/li/a/text()')
    nav1 = nav[2]
    points = int(nav1[9:-2])
    if points < 10:
        print ("Not enough points!")
        break
    else:
        print (str(links[i]))

print ("Points after entering: ", points)

name = input('Type something for exit...')
