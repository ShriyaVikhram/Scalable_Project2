import csv
import urllib.request

file = open('vikhrams-challenge-filenames.csv', "rU")
filelist = csv.reader(file, delimiter=',')
for rec in filelist:
	   urllib.request.urlretrieve("https://cs7ns1.scss.tcd.ie/index.php?download=noresume_speed&shortname=vikhrams&myfilename="+rec[0], rec[0])