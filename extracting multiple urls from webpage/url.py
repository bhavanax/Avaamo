import requests
from bs4 import BeautifulSoup


url = 'https://www.intel.com/content/www/us/en/support/products/96066/software/development-software/openvino-toolkit.html#support-article-selector'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')

urls = []
for link in soup.find_all('a'):
	print(link.get('href'))
