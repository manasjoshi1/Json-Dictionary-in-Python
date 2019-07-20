import json as js 							#importing json library as js
from difflib import SequenceMatcher as sq
from difflib import get_close_matches as gcm

data=js.load(open("076 data.json"))			#to load the json file into variable data

def translate(word):
	if(word in data):
		return data[word]
	elif len(gcm(word,data.keys(),cutoff=0.75))>0:
		yn= input("Did you mean %s instead?Enter Y if yes, or N if no"% gcm(word,data.keys())[0])
		if(yn.lower()=="y"):
			return data[gcm(word,data.keys())[0]]
		else :
			return"Word doesnt exist. Please double check it"	
	else :
		return"Word doesnt exist. Please double check it"


word =input("Enter the Word: \n")

output=translate(word.lower())

if(type(output)==list):
	i=1;
	for item in output:
		print(i,".",item)
		i+=1
else:
	print(output)












#print(type(data))
#print(data)
#print (data["rain"])

