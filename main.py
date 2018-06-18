from ParsersPackage.parsers import get_html, parser
import csv
from tqdm import tqdm
#schools_map = {
	#'Школа 5' : ['http://www.nnovschool5.edusite.ru/p505aa1.html', 2],
	#'Школа 12': ['http://schoolnn12.narod.ru/', 2],
	#'Школа 15': ['http://www.school-15.ru/parents.htm', 4]
#}

news_map = dict()

def csv_reader(file):

	reader = csv.reader(file)
	for row in reader:
		string = " ".join(row)
		result_string = list()
		i = j = 0 # i - key j - value of dictionary
		for char in string:
			if not char.isspace():
				result_string.append(char)
			else:
				if i == 0:
					word1 = "".join(result_string)
					result_string = []
					i += 1
				elif i == 1 and j == 0:
					word2 = "".join(result_string)
					result_string = []
					j += 1
				else:
					word3 = "".join(result_string)
					result_string = []
		schools_map[word1] = [word2, word3]


def csv_writer(file):
	with open(file,"w", newline = '') as file:
		writer = csv.writer(file, delimiter = ',')
		for school in schools_map:
			

def main():

	#for iterator in tqdm(schools_map.items()):
	for iterator in schools_map.items():
		html = get_html(iterator[1][0]) #2nd element of tuple; 1 element of list
		news_map[iterator[0]] = parser(html, (int)(iterator[1][1]))
		
	for i in news_map.items():
		print(i)
	

if __name__ == '__main__':
	schools_map = dict()
	csv_path = "initial_data.csv"
	with open(csv_path, "r") as file:
		csv_reader(file)
	main()