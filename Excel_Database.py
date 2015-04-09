#!/usr/bin/env python

import re, os, csv

path = "./Database/"
NPTEL = os.listdir(path)

FILE1 = open("out.csv", "w")

writer = csv.writer(FILE1)
writer.writerow(['Keyword', 'Lecture_Name', 'Youtube_Query']) #if needed

for book in NPTEL:
	file = os.path.join(path, book)
	text = open(file, "r")
	for line in text:
		if line != "\n":
			line = line.rstrip()
			line = line.lstrip()
			li = line.split("|")
			writer.writerow(li)
FILE1.close()		
