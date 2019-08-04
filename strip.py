# Kavya Aswadhati 7/18/19
# Strip table to just species list
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help = "input filename")
parser.add_argument("-o","--output", help = "output filename")
args = parser.parse_args()

output = args.output
input = args.input


speciesList = []

for line in open(input):
	b = line.strip().split('\t')
	speciesList.append(b[0])
print("table:",speciesList)

outfile = open(output,'w')

for species in speciesList:
	outfile.write(species +'\n')