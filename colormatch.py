import json 
import os
import sys


def getfurnattributes(dirname):
	attributes = []
	for file in os.listdir(dirname):
		fp = open(dirname + "/" + file, 'r')
		values = json.load(fp)
		attributes.append((values["product"]["product_description"]["title"], values["product"]["variation"]["color"]))
		fp.close()
	return attributes

def findoverlapping(complements, chosen_palatte):
	seencolors = set()
	finalcolors = []
	for color in chosen_palatte:
		comps = complements[color]
		for compcolor in comps:
			if compcolor in seencolors:
				finalcolors.append(compcolor)
			else:
				seencolors.add(compcolor)
	return finalcolors

def getcomplements(furniture, overlaps):
	comps = []
	for (name, color1) in furniture:
		for color2 in overlaps:
			if color2 in color1.lower():
				comps.append(name)
	return comps

def main():
	palette = {"bedroom1": ["blue", "gray"], "bedroom2": ["white", "green"], "bedroom3": ["gold", "black"]}
	jsonfiledir = sys.argv[1]
	chosen_palette = palette[sys.argv[2]]
	complements = {"blue": ["pink", "gray", "black", "white"], "black": ["blue", "gray"], "gray": ["white", "black", "blue"],"white": ["black", "gray", "brown", "blue"], "green": ["gold", "white"], "pink": ["white", "blue"]}
	overlaps = findoverlapping(complements, chosen_palette)
	furniture = getfurnattributes(jsonfiledir)
	relevant = getcomplements(furniture, overlaps)
	print(relevant)


if __name__ == '__main__':
	main()
