import ParsersPackage.parsers

schools_map = {
	#'Школа 5' : 'http://www.nnovschool5.edusite.ru/p505aa1.html',
	#'Школа 12': 'http://schoolnn12.narod.ru/'
	'Школа 15': 'http://www.school-15.ru/parents.htm'
}

news_map = dict()

def main():
	for url in schools_map.values():
		html = ParsersPackage.parsers.get_html(url)
		ParsersPackage.parsers.parser(html)



if __name__ == '__main__':
	main()