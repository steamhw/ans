import json #import json library

f = open("noble_gases.json")#open json file(read mode)

halogens = { #dictionary for the halogens
	"Fluorine" : {"atomicNumber" : 9, "name" : "Fluorine", "symbol" : "F"},
	"Chlorine" : {"atomicNumber" : 17, "name" : "Chlorine", "symbol" : "Cl"},
	"Bromine" : {"atomicNumber" : 35, "name" : "Bromine", "symbol" : "Br"},
	"Iodine" : {"atomicNumber" : 53, "name" : "Iodine", "symbol" : "I"},
	"Astatine" : {"atomicNumber" : 85, "name" : "Astatine", "symbol" : "At"}
}

elements = json.load(f) #phrase json data to dictionary
elements.update(halogens) #append halogen into the dictionary
f.close() #close the file

f = open("noble_gases.json", "w") #open the json file(write mode(overwrites the previous value))
f.write(json.dumps(elements)) #write the new dictionary into the json file
f.close() #close the file