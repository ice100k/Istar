#A simple shell program for I*
#by ice100k
#08/04/2020

#<<<<<<<<<<<<<<<<<<IMPORTS>>>>>>>>>>>>>>>>>>

import istar

#<<<<<<<<<<<<<<<<<RUNTIME>>>>>>>>>>>>>>>>>>>

while True:

	text = input("Istar:  ")

	if text == "quit()":
		quit()

	else:

		result, error = istar.run('<stdin>', text)

		if error: print(error.as_string())
		elif result: print(result)
