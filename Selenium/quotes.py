from selenium import webdriver
from urllib.parse import urljoin

PATH = "" #INSERT THE PATH TO CHROMEDRIVER IN THIS STRING
ROOT_URL = 'http://quotes.toscrape.com'
url = ROOT_URL
data=[]
driver=webdriver.Chrome(PATH)
while url:
    driver.get(url)
    for quote in driver.find_elements_by_class_name("quote"):
        quote_data=[]
        quote_data.append('"' + quote.find_element_by_class_name("text").text + '"')
        quote_data.append(quote.find_element_by_class_name("author").text)
        quote_data.append('"' + ",".join([tag.text for tag in quote.find_elements_by_class_name("tag")]) + '"')
        data.append(quote_data)
    try:
        url = urljoin(ROOT_URL, driver.find_element_by_class_name("next").find_element_by_tag_name("a").get_attribute("href"))
    except:
        url=None
with open("quotes.csv", "w") as file:
    for element in data:
        file.write(",".join(element) + "\n")
