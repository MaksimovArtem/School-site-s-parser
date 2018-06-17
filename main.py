import ParsersPackage.parsers

schools_map = {
	'Школа 5' : ['http://www.nnovschool5.edusite.ru/p505aa1.html', 2],
	'Школа 12': ['http://schoolnn12.narod.ru/', 2],
	'Школа 15': ['http://www.school-15.ru/parents.htm', 4]
}

news_map = dict()

def main():
	for iterator in schools_map.values():
		html = ParsersPackage.parsers.get_html(iterator[0])
		ParsersPackage.parsers.parser(html, iterator[1])



if __name__ == '__main__':
	main()