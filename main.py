from ParsersPackage.parsers import get_html, parser
import csv
from tqdm import tqdm

news_map = dict()

def csv_reader(file):
	reader = csv.reader(file)
	for row in reader:
		string = " ".join(row)
		result_string = list()
		i = j = 0 # i - key j - value of dictionary
		word1 = word2 = word3 = ""
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
		for news in news_map.items():
			writer.writerow(news)
			

def main():
	#for iterator in tqdm(schools_map.items()):
	print("You are here!")
	for iterator in schools_map.items():
		if(iterator[1][0] == ""):
			news_map[iterator[0]] = "DISTRICT"
		else:
			html = get_html(iterator[1][0]) #2nd element of tuple; 1 element of list
			news_map[iterator[0]] = parser(html, (int)(iterator[1][1]))	
	#sv_writer("output.csv")
	for i in news_map.items():
		print(i)
	print("You are here2!")
	

if __name__ == '__main__':
	schools_map = dict()
	csv_path = "initial_data.csv"
	with open(csv_path, "r") as file:
		csv_reader(file)
	main()