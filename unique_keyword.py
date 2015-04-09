################################################################
# AUTHOR  -  NIRANJAN                                          #
# PROGRAM -  To remove the duplicate keywords                  #
################################################################


#!/usr/bin/env python

# INPUT TRANSCRIPT

inputfile = open("Strength_of_materials.txt")
unique = []

for line in inputfile:
	line = line.strip()
	if line not in unique:
		unique.append(line)
inputfile.close()

for i in range(0, len(unique)):
	unique[i] += "\n"

# OUTPUT TRANSCRIPT

output = open("Strength_of_materials_keywords.txt", "w")
output.writelines(unique)
output.close
