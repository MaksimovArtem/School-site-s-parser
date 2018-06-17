import requests
from bs4 import BeautifulSoup
import re #regular expressions


def get_html(url):
	response = requests.get(url)
	response.encoding = 'cp1251' # encode old site's format
	return response.text


def search_needed_news(string): #small dictionary that I used to get needed string
	text1 = "родител"
	text2 = "первоклассник"
	text3 = "остоится"
	if string.find(text1) != -1 or string.find(text2)!= -1 or string.find(text3)!= -1:
		return True
	else:
		return False


def parser(html):
	soup = BeautifulSoup(html, 'html.parser')
	all_news = soup.find_all(text = re.compile("обрани"), limit = 3) # )))))))))))))))))

	if len(all_news)!=0:
		print(len(all_news))
	#check

	answer = ''
	for news in all_news: 
		string = (str)(news.parent.parent.parent.parent.get_text()).lower()
		
		if search_needed_news(string):
			print(news.parent.parent.parent.parent.get_text())
			answer = news.parent.parent.get_text() # 2nd lvl
		else:
			continue
	return answer