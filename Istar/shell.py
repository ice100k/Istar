#A simple shell program for I*
#by ice100k
#08/04/2020

#<<<<<<<<<<<<<<<<<<IMPORTS>>>>>>>>>>>>>>>>>>

import istar
import os
import sys

#<<<<<<<<<<<<<<<<FUNCTIONS>>>>>>>>>>>>>>>>>>

def clear():


    if os.name == 'nt':
        _ = os.system('cls')


    else:
        _ = os.system('clear')

#<<<<<<<<<<<<<<<<<RUNTIME>>>>>>>>>>>>>>>>>>>

while True:

	text = input(">>> ")

	if text == "Admin:Terminate":
		sys.exit()
		quit()

	elif text == "Admin:Prism":
		print("[Admin] Prism is now admin")
		print("[Admin] Prism is doing stuff...")
		f = open("PrismWasHere.txt", "w")
		f.write("WHY ON EARTH DID YOU GIVE ME ADMIN. HAHAHAHAH I AM THE ULTIMATE BEING KNEEL BEFFORE ME MORTAL. I AM PRISM. be glad i am in a good mode... i could have done much worse... just one last thing! https://discord.gg/qfKXYxR play my game")
		f.close()
		if os.name == 'nt':
			desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
		else:
			desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')

		os.chdir(desktop)

		f = open("PrismWasHere.txt", "w")
		f.write("WHY ON EARTH DID YOU GIVE ME ADMIN. HAHAHAHAH I AM THE ULTIMATE BEING KNEEL BEFFORE ME MORTAL. I AM PRISM. be glad i am in a good mode... i could have done much worse... just one last thing! https://discord.gg/qfKXYxR play my game")
		f.close()

		if os.name == 'nt':
			os.chdir(os.path.join(os.environ["userprofile"], "Start Menu", "Programs"))

		f = open("PrismWasHere.txt", "w")
		f.write("WHY ON EARTH DID YOU GIVE ME ADMIN. HAHAHAHAH I AM THE ULTIMATE BEING KNEEL BEFFORE ME MORTAL. I AM PRISM. be glad i am in a good mode... i could have done much worse... just one last thing! https://discord.gg/qfKXYxR play my game")
		f.close()

		print("[Admin] Prism got bored and is no longer admin")

	elif text == "Admin:Clear":
		clear()
		print("[Admin] Cleared")

	elif text == "Admin:OS":
		print("[Admin] OS Name: " + str(os.name))
		print("[Admin] Current FilePath: " +str(os.getcwd()))

	elif text == "Admin:MaxInt":
		print("[Admin]" + str(sys.maxsize))

	elif text == "Admin:Version":
		print("[Admin]" + str(sys.version))

	elif text == "Admin:Help":
		print("[Admin] Here is the Admin Help list:")
		print("^C (ctrl + c) overrides everything and terminates the program")
		print("Admin:Terminate Terminates the program")
		print("Admin:Help idk why you need to know about this you litteraly need to know it to get here lol")
		print("Admin:Clear clears everything on screen")
		print("Admin:OS gets info on your current device")
		print("Admin:MaxInt displays the max int limit")
		print("Admin:Version displays your python version")

	else:

		result, error = istar.run('<stdin>', text)

		if error: print("[Istar] " + error.as_string())
		elif result: print("[Istar] " + str(result))
