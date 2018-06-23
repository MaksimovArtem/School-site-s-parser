import requests
from bs4 import BeautifulSoup
import re #regular expressions
import sys
from grab import Grab

def get_html(url):
	response = requests.get(url)
	windows_1251_encoding_list = ["htm","14","50","94","115","121","139","172","174","176"]
	# htm/html pages and a list of schools with old encoding pages
	for word in windows_1251_encoding_list:
		if url.find(word) != -1:
			response.encoding = 'cp1251' # encode for htm and html web-pages
			break
	return response.text


def search_needed_news(string): #small dictionary that I used to get needed string
	extra_keywords = ["родител","первоклассник","cостоится"]
	for word in extra_keywords:
		if string.find(word) != -1:
			return True
	return False


def prettify_string(string):#make string better)
	result = list()
	for char in string:
			if char.isalnum():
				result.append(char)
			elif (char.isspace() or char in ".-:;") and (not result or not result[-1].isspace()):
				result.append(char)
			elif (char in ","):
				continue
	return ''.join(result)
	

def get_needed_lvl(tag, lvl):#going up in tag tree to make parsing sentence more readable
	for i in range(lvl):
		tag = tag.parent
		i+=1
	return (str)(tag.get_text()).lower()


def parser(html, lvl):
	soup = BeautifulSoup(html, 'html.parser')
	all_news = soup.find_all(text = re.compile("обрани"), limit = 3) # newest 3 words
	answer = ''
	try:
		for news in all_news: 
			string = get_needed_lvl(news,lvl)
			if search_needed_news(string) and len(string) < 500:
				answer += prettify_string(string)
			else:
				continue
		if(len(answer) > 1000):
			return "Слишком большая новость"
		else:
			return answer
	except:
		return "Информации или нет, или где-то ошибка"	
