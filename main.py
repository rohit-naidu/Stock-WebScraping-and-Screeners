import requests
import json
from urllib.request import urlopen
from lxml import etree

def get_symbol(symbol):
    url = "http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&region=1&lang=en".format(symbol)

    result = requests.get(url).json()

    for x in result['ResultSet']['Result']:
        if x['symbol'] == symbol:
            return x['name']

ib = input("Ticker: ")
#break
get_symbol(ib)
company = get_symbol(ib)

get_symbol(ib)
company = get_symbol(ib)
url = 'https://www.macrotrends.net/stocks/charts/'+ib+'/apple/revenue'
headers = {'Content-Type': 'text/html',}
response = requests.get(url, headers=headers)
html = response.text
with open ('star_wars_html', 'w') as f:
    f.write(html)
      #currentQ2
response = urlopen(url)
htmlparser = etree.HTMLParser()
tree = etree.parse(response, htmlparser)
currentEarningsQ2 = tree.xpath('//*[@id="style-1"]/div[2]/table/tbody/tr[1]/td[2]/text()')
if (str(currentEarningsQ2) == '[]'):
  raise SystemExit
currentEarningsQ2 = str(currentEarningsQ2)
currentEarningsQ2 = currentEarningsQ2.replace("]","") 
currentEarningsQ2 = currentEarningsQ2.replace("[","") 
currentEarningsQ2 = currentEarningsQ2.replace("'","") 
currentEarningsQ2 = currentEarningsQ2.replace("$","") 
currentEarningsQ2 = currentEarningsQ2.replace(",","") 
currentEarningsQ2 = float(currentEarningsQ2)
      #pastQ2
response = urlopen(url)
htmlparser = etree.HTMLParser()
tree = etree.parse(response, htmlparser)
pastEarningsQ2 = tree.xpath('//*[@id="style-1"]/div[2]/table/tbody/tr[5]/td[2]/text()')
if (str(pastEarningsQ2) == '[]'):
  raise SystemExit
pastEarningsQ2 = str(pastEarningsQ2)
pastEarningsQ2 = pastEarningsQ2.replace("]","") 
pastEarningsQ2 = pastEarningsQ2.replace("[","") 
pastEarningsQ2 = pastEarningsQ2.replace("'","") 
pastEarningsQ2 = pastEarningsQ2.replace("$","") 
pastEarningsQ2 = pastEarningsQ2.replace(",","") 
pastEarningsQ2 = float(pastEarningsQ2)
      #pastQ1
response = urlopen(url)
htmlparser = etree.HTMLParser()
tree = etree.parse(response, htmlparser)
pastEarningsQ1 = tree.xpath('//*[@id="style-1"]/div[2]/table/tbody/tr[6]/td[2]/text()')
if (str(pastEarningsQ1) == '[]'):
  raise SystemExit
pastEarningsQ1 = str(pastEarningsQ1)
pastEarningsQ1 = pastEarningsQ1.replace("]","") 
pastEarningsQ1 = pastEarningsQ1.replace("[","") 
pastEarningsQ1 = pastEarningsQ1.replace("'","") 
pastEarningsQ1 = pastEarningsQ1.replace("$","") 
pastEarningsQ1 = pastEarningsQ1.replace(",","") 
pastEarningsQ1 = float(pastEarningsQ1)
      #currentQ1
response = urlopen(url)
htmlparser = etree.HTMLParser()
tree = etree.parse(response, htmlparser)
currentEarningsQ1 = tree.xpath('//*[@id="style-1"]/div[2]/table/tbody/tr[2]/td[2]/text()')
if (str(currentEarningsQ1) == '[]'):
  raise SystemExit
currentEarningsQ1 = str(currentEarningsQ1)
currentEarningsQ1 = currentEarningsQ1.replace("]","") 
currentEarningsQ1 = currentEarningsQ1.replace("[","") 
currentEarningsQ1 = currentEarningsQ1.replace("'","") 
currentEarningsQ1 = currentEarningsQ1.replace("$","") 
currentEarningsQ1 = currentEarningsQ1.replace(",","") 
currentEarningsQ1 = float(currentEarningsQ1)


url = 'https://www.macrotrends.net/stocks/charts/'+ib+'/apple/eps-earnings-per-share-diluted'
headers = {'Content-Type': 'text/html',}
response = requests.get(url, headers=headers)
html = response.text
with open ('star_wars_html', 'w') as f:
        f.write(html)
      #currentQ2
response = urlopen(url)
htmlparser = etree.HTMLParser()
tree = etree.parse(response, htmlparser)
currentEPSQ2 = tree.xpath('//*[@id="style-1"]/div[2]/table/tbody/tr[1]/td[2]/text()')
if (str(currentEPSQ2) == '[]'):
  raise SystemExit
currentEPSQ2 = str(currentEPSQ2)
currentEPSQ2 = currentEPSQ2.replace("]","") 
currentEPSQ2 = currentEPSQ2.replace("[","") 
currentEPSQ2 = currentEPSQ2.replace("'","") 
currentEPSQ2 = currentEPSQ2.replace("$","") 
currentEPSQ2 = currentEPSQ2.replace(",","") 
currentEPSQ2 = float(currentEPSQ2)
      #pastQ2
response = urlopen(url)
htmlparser = etree.HTMLParser()
tree = etree.parse(response, htmlparser)
pastEPSQ2 = tree.xpath('//*[@id="style-1"]/div[2]/table/tbody/tr[5]/td[2]/text()')
if (str(pastEPSQ2) == '[]'):
  raise SystemExit
pastEPSQ2 = str(pastEPSQ2)
pastEPSQ2 = pastEPSQ2.replace("]","") 
pastEPSQ2 = pastEPSQ2.replace("[","") 
pastEPSQ2 = pastEPSQ2.replace("'","") 
pastEPSQ2 = pastEPSQ2.replace("$","") 
pastEPSQ2 = pastEPSQ2.replace(",","") 
pastEPSQ2 = float(pastEPSQ2)
      #pastQ1
response = urlopen(url)
htmlparser = etree.HTMLParser()
tree = etree.parse(response, htmlparser)
pastEPSQ1 = tree.xpath('//*[@id="style-1"]/div[2]/table/tbody/tr[6]/td[2]/text()')
if (str(pastEPSQ1) == '[]'):
  raise SystemExit
pastEPSQ1 = str(pastEPSQ1)
pastEPSQ1 = pastEPSQ1.replace("]","") 
pastEPSQ1 = pastEPSQ1.replace("[","") 
pastEPSQ1 = pastEPSQ1.replace("'","") 
pastEPSQ1 = pastEPSQ1.replace("$","") 
pastEPSQ1 = pastEPSQ1.replace(",","") 
pastEPSQ1 = float(pastEPSQ1)
      #currentQ1
response = urlopen(url)
htmlparser = etree.HTMLParser()
tree = etree.parse(response, htmlparser)
currentEPSQ1 = tree.xpath('//*[@id="style-1"]/div[2]/table/tbody/tr[2]/td[2]/text()')
if (str(currentEPSQ1) == '[]'):
  raise SystemExit
currentEPSQ1 = str(currentEPSQ1)
currentEPSQ1 = currentEPSQ1.replace("]","") 
currentEPSQ1 = currentEPSQ1.replace("[","") 
currentEPSQ1 = currentEPSQ1.replace("'","") 
currentEPSQ1 = currentEPSQ1.replace("$","") 
currentEPSQ1 = currentEPSQ1.replace(",","") 
currentEPSQ1 = float(currentEPSQ1)
      #calc
percentQ2 = pastEarningsQ2*(1.29)
percentQ1 = pastEarningsQ1*(1.29)
percentEPSQ2 = pastEPSQ2*(1.39)
percentEPSQ1 = pastEPSQ1*(1.39)
if (currentEPSQ2>=percentEPSQ2 and currentEPSQ1>=percentEPSQ1) or (currentEarningsQ2>=percentQ2 and currentEarningsQ1>=percentQ1):
  print(str(company)+": Good Story")
  print("__________")
else:
  print(str(company)+': Both quarters arent above 29%')
  print("__________")
        #end
