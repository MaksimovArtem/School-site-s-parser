import requests
from bs4 import BeautifulSoup
import re #regular expressions


def get_html(url):
	response = requests.get(url)
	if "htm" in url:
		response.encoding = 'cp1251' # encode for htm and html web-pages
	return response.text


def search_needed_news(string): #small dictionary that I used to get needed string
	text1 = "родител"
	text2 = "первоклассник"
	text3 = "остоится"
	if string.find(text1) != -1 or string.find(text2)!= -1 or string.find(text3)!= -1:
		return True
	else:
		return False


def prettify_string(string):
	result = list()
	for char in string:
			if char.isalnum():
				result.append(char)
			elif (char.isspace() or char in ".-:;") and (not result or not result[-1].isspace()):
				result.append(char)
	return ''.join(result)


def get_needed_lvl(tag, lvl):
	for i in range(lvl):
		tag = tag.parent
		i+=1
	return (str)(tag.get_text()).lower()


def parser(html, lvl):
	soup = BeautifulSoup(html, 'html.parser')
	all_news = soup.find_all(text = re.compile("обрани"), limit = 3) # last news

	#if len(all_news) != 0:
	#	print(len(all_news))
	#check

	answer = ''
	for news in all_news: 
		#string = (str)(news.parent.parent.get_text()).lower()
		string = get_needed_lvl(news,lvl)
		if search_needed_news(string):
			print(prettify_string(string))
			answer = string # 2nd lvl
		else:
			continue
	return answer