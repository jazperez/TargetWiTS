import json 
import os
import sys


def getfurncolors(filename):
	file = open(filename, 'r')
	values = json.load(file)
	color = values["product"]["variation"]["color"]	
	file.close()
	return color

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


def main():
	palette = {"bedroom1": ["blue", "gray"], "bedroom2": ["white", "green"], "bedroom3": ["gold", "black"]}
	jsonfile = sys.argv[1]
	chosen_palette = palette[sys.argv[2]]
	complements = {"blue": ["pink", "gray", "black", "white"], "gray": ["white", "black", "blue"],"white": ["black", "gray", "brown", "blue"], "green": ["gold", "white"], "pink": ["white", "blue"]}
	overlaps = findoverlapping(complements, chosen_palette)
	print(overlaps)
	furniture_colors = getfurncolors(jsonfile)
	print(furniture_colors)



if __name__ == '__main__':
	main()
