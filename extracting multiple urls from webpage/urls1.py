import requests
from bs4 import BeautifulSoup

urls = 'https://www.intel.com/content/www/us/en/support/products/96066/software/development-software/openvino-toolkit.html#support-recommended-articles'
grab = requests.get(urls)
soup = BeautifulSoup(grab.text, 'html.parser')

# opening a file in write mode
f = open("test1.csv", "w")
# traverse paragraphs from soup
for link in soup.find_all("a"):
    data = str(link.get('href'))
    if data == "" or data == "None" or data == "#":
        continue
    f.write(data)
    f.write("\n")

f.close()
