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
	text3 = "cостоится"
	if string.find(text1) != -1 or string.find(text2)!= -1 or string.find(text3)!= -1:
		return True
	else:
		return False


def prettify_string(string):#make string better)
	result = list()
	for char in string:
			if char.isalnum():
				result.append(char)
			elif (char.isspace() or char in ".-:;") and (not result or not result[-1].isspace()):
				result.append(char)
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
			if search_needed_news(string):
				answer += prettify_string(string)
			else:
				continue
		if(len(answer) > 1500):
			return "Something has broken"
		else:
			return answer
	except:
		return ""	