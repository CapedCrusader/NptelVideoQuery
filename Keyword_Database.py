##########################################################################################
# AUTHOR    - NIRANJAN                                                                   #
# PROGRAM   - Generating Keyword database with lecture-names and time-stamps             #
# NOTE      - In every transcript, the following format should be added at the beginning.# 
#             (Refer Slide Time: 00:00:00)                                               #
##########################################################################################

#!/usr/bin/env python

import re, os, inspect

# SPECIFY THE PATH OF THE TRANSCRIPTS (Open the terminal & use "pwd" command to get the right path)

path = "./Transcripts/IIT_Guwahati/Engineering Mechanics/Edited"
NPTEL = os.listdir(path)

# NAME THE OUTPUT FILE-NAME ACCORDING TO THE COURSE & THEIR IIT's Ex: database_<coursename>_<iitname>.txt

FILE1 = open("./Database/IIT_Guwahati/Engineering_Mechanics.txt", "w")

# OPEN THE KEYWORD FILE

FILE2 = open("engineering_mechanics_iitguhwati_keywords.txt","r")

for key_word in FILE2:
	key_word = key_word.rstrip('\n')
	key_word = key_word.lstrip('\n')
	for book in NPTEL:
		file = os.path.join(path, book)
		text = open(file, "r")
		for line in text:
			time = re.search(r'Time:?\s?o?n?:?\s?\s?\(?(\w?\w?:?\w+\:\w?\w+)', line, re.IGNORECASE)
			if time :
				times = time.group(1)
			if re.search(key_word,line):
				timestamp = times.split(':')
                                length = len(timestamp)
				a = timestamp[0]
				b = timestamp[1]
				if length == 2:
                                	print  >>  FILE1, key_word + "|" + book + "|?t=" + a + "m" + b + "s","\n"
				if length == 3:
					secs = str(00)
                                	print  >>  FILE1, key_word + "|" + book + "|?t=" + a + "h" + b + "m" + secs + "s","\n"
				break
		text.close()
