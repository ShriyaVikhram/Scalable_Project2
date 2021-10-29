import csv
import urllib.request

file = open('vikhrams-challenge-filenames.csv', "rU")
reader = csv.reader(file, delimiter=',')
for row in reader:
	   urllib.request.urlretrieve("https://cs7ns1.scss.tcd.ie/index.php?download=noresume_speed&shortname=vikhrams&myfilename="+row[0], row[0])