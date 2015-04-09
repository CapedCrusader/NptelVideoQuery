#!/usr/bin/env python

import os

# SPECIFY THE PATH OF THE TRANSCRIPTS (Open the terminal & use "pwd" command to get the right path)

path = "./IIT_Guwahati/Engineering Mechanics/Edited"
NPTEL = os.listdir(path)

FILE1 = open("Filenames_Engineering_Mechanics.txt", "w")
for filename in NPTEL:
	file = os.path.join(path, filename)
	text = open(file, "r")
	print >> FILE1, filename + "|" + os.linesep
	text.close()
