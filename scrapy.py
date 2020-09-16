from bs4 import BeautifulSoup
import requests
import csv


source = requests.get('http://coreyms.com').text
 
soup = BeautifulSoup(source, 'lxml')





for article in soup.find_all('article'):

	title = article.header.h2.a.text
	print(title)

	summary = article.find('div', class_='entry-content').p.text
	print(summary)

	try:
		vid_src = article.find('iframe', class_='youtube-player')['src']
		vid_id = vid_src.split('/')[4]
		vid_id = vid_id.split('?')[0]

		yt_link = f'https://youtube.com/watch?v={vid_id}'
		print(yt_link)

		
	except:
		print(">>> --- !!! Link not found !!! --- <<<")

	print()



