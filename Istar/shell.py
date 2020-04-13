#I* a programming language
#by ice100k
#08/04/2020

import istar

while True:

	text = input("Istar:  ")
	
	result, error = istar.run('<stdin>', text)

	if error: print(error.as_string())
	else: print(result) 
