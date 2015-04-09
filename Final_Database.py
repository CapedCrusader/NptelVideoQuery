#!/usr/bin/python`
import re, os

FILE1 = open("file1.txt", "r")
FILE3 = open("out.txt", "w")

for line1 in FILE1:
	
	line1 = line1.split("|")
	filename = line1[0]
	filename = filename.rstrip(".txt")
	link = line1[1]
	link = link.rstrip("\n")
	link = link.lstrip("\n")
	FILE2 = open("file2.txt", "r")
	for line2 in FILE2:
		if re.search(filename,line2,re.IGNORECASE):
			line2 = line2.split("|")
			
			key = line2[0]
			file = line2[1]
			time = str(line2[2])
			time = time.rstrip("\n")
			time = time.lstrip("\n")
			final_link = link + time
			print  >>  FILE3, key + "|" + filename + "|" + final_link,"\n"

