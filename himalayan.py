from bs4 import BeautifulSoup
import requests
import csv

ul = 'https://kathmandupost.ekantipur.com'


source = requests.get(ul).text
soup = BeautifulSoup(source, 'lxml')

def kathmadnupost():

	with open('KathmanduPostNews.csv', 'w') as csv_file:
		csv_writer = csv.writer(csv_file)
		csv_writer.writerow(['title', 'summary', 'article-link'] )

		#title = soup.find('div', class_='row order')
		head = soup.find('div', class_='row order')

		for article in head.find_all('article', class_='article-image'):

			title = article.h3.a.text
			print(title)
			summary = article.p.text
			print(summary)
			try:
				image_link = article.find('a')['href']
				print(image_link)
			except:
				print("link not found")
			print()

			csv_writer.writerow([title, summary, image_link])


kathmadnupost()