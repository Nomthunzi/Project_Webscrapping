import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

ROOT_URL = 'http://quotes.toscrape.com'
url = ROOT_URL
data=[]
while url:
    html = requests.get(url).text
    doc = BeautifulSoup(html, "html.parser")
    for quote in doc.select(".quote"):
        quote_data=[]
        quote_data.append('"' + quote.select_one(".text").text + '"')
        quote_data.append(quote.select_one(".author").text)
        quote_data.append('"' + ",".join([tag.text for tag in quote.select(".tag")]) + '"')
        data.append(quote_data)
    try:
        url = urljoin(ROOT_URL, doc.select_one(".next").select_one("a").attrs["href"])
    except:
        url=None
with open("quotes.csv", "w") as file:
    for element in data:
        file.write(",".join(element) + "\n")
