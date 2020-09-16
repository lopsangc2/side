from bs4 import BeautifulSoup
import requests

with open('simple.html') as html_files:
	soup = BeautifulSoup(html_files, 'lxml')

# print(soup.prettify())

for match in soup.find_all('div', class_='article'):
	headline = match.h2.a.text
	print(headline)

	paragraph = match.p.text
	print(paragraph)