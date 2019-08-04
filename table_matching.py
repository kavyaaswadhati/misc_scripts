'''
Kavya Aswadhati
7/17/19
tableMatching.py
Script to match species that are ordered according to their position on a phylogenetic tree
with their reproductive manipulator species infections.
'''

import argparse

# Assuming that first input file will be the species as ordered by tree, the second
# a tab delimited file of the species and their relative frequencies
parser = argparse.ArgumentParser()
parser.add_argument("-i1", "--input1", help = "input tree ordered species filename")
parser.add_argument("-i2", "--input2", help = "input species info as table filename")
parser.add_argument("-o","--output", help = "output filename")
args = parser.parse_args()

output = args.output
input1 = args.input1
input2 = args.input2

orderedSpecies = []
speciesTable = []
orderedTable = []

for line in open(input1):
	a=line.strip()
	# the input format uses snake script for species name, remove the underline.
	c = a.replace("_"," ")
	orderedSpecies.append(c)
# input file is in reverse order
temp = orderedSpecies[::-1]
orderedSpecies = temp

for line in open(input2):
	b = line.strip().split('\t')
	speciesTable.append(b)

outfile = open(output,'w')
print("species file len",len(orderedSpecies))
print("table file len",len(speciesTable))

for species in orderedSpecies:
	tableEntry = [spec for spec in speciesTable if species in spec]
	if len(tableEntry)!=1:
		print(species+" not found or found twice")
		print(tableEntry)
	if len(tableEntry) == 1:
		outfile.write('\t'.join(tableEntry[0])+'\n')

	
	
	
	
	

	
