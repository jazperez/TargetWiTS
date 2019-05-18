import json 
import os
import sys


def getfurnattributes(dirname):
	attributes = []
	for file in os.listdir(dirname):
		fp = open(dirname + "/" + file, 'r')
		values = json.load(fp)
		attributes.append((values["product"]["product_description"]["title"], values["product"]["product_classification"]["item_type"]["name"], values["product"]["variation"]["color"]))
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
	for (name, category, color1) in furniture:
		for color2 in overlaps:
			if color2 in color1.lower():
				comps.append((category, name))
	return comps

def findincategory(furniture, category):
	matchingfurniture = []
	for (c, n) in furniture:
		if (c == category):
			matchingfurniture.append((c,n))
	return matchingfurniture

def main():
	palette = {"bedroom1": ["blue", "gray"], "bedroom2": ["white", "green"], "bedroom3": ["gold", "black"]}
	jsonfiledir = sys.argv[1]
	chosen_palette = palette[sys.argv[2]]
	spec_category = sys.argv[3]
	complements = {"blue": ["pink", "gray", "black", "white"], "black": ["blue", "gray"], "gray": ["white", "black", "blue"],"white": ["black", "gray", "brown", "blue"], "green": ["gold", "white"], "pink": ["white", "blue"]}
	overlaps = findoverlapping(complements, chosen_palette)
	furniture = getfurnattributes(jsonfiledir)
	relevant = []
	if(spec_category == "all"):
		relevant = getcomplements(furniture, overlaps)
	else:
		relevant = findincategory(getcomplements(furniture, overlaps), spec_category)
	print("chosen palette colors:")
	for c in chosen_palette:
		print("-"+c)
	print("\n")
	print("complementing colors:")
	for c in overlaps:
		print("-"+c)
	print("\n")
	print("displayed furniture:")
	for (c, n) in relevant:
		print("-"+c + ": " + n)
	print("\n")

if __name__ == '__main__':
	main()
