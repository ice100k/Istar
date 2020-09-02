#A simple shell program for I*
#by ice100k
#08/04/2020

#<<<<<<<<<<<<<<<<<<IMPORTS>>>>>>>>>>>>>>>>>>

import istar
from os import system, name

#<<<<<<<<<<<<<<<<FUNCTIONS>>>>>>>>>>>>>>>>>>

def clear():


    if name == 'nt':
        _ = system('cls')


    else:
        _ = system('clear')

#<<<<<<<<<<<<<<<<<RUNTIME>>>>>>>>>>>>>>>>>>>

while True:

	text = input(">>>  ")

	if text == "Admin:Terminate":
		quit()

	elif text == "Admin:Prism":
		print("[Admin] Prism is now admin")

	elif text == "Admin:Clear":
		clear()
		print("[Admin] Cleared")

	elif text == "Admin:Help":
		print("[Admin] Here is the Admin Help list:")
		print("^C (ctrl + c) overrides everything and terminates the program")
		print("Admin:Terminate Terminates the program")
		print("Admin:Help idk why you need to know about this you litteraly need to know it to get here lol")
		print("Admin:Clear clears everything on screen")

	else:

		result, error = istar.run('<stdin>', text)

		if error: print("[Istar] " + error.as_string())
		elif result: print("[Istar] " + str(result))
