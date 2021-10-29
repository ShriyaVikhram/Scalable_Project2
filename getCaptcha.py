import csv
from urllib2 import urlopen

file = open('vikhrams-challenge-filenames.csv', "rU")
reader = csv.reader(file, delimiter=',')
for row in reader:
    urlopen.geturl("https://cs7ns1.scss.tcd.ie/index.php?download=noresume_speed&shortname=vikhrams&myfilename="+row[0], row[0])
