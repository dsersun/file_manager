"""
Модуль с функциями для файлового менеджера
"""
import datetime, os, colorama
from colorama import Fore, Back, Style
colorama.init()

# Вывод текущей даты
def curent_date():
	x = datetime.datetime.now()
	global today
	today = (x.strftime("%d"),x.strftime("%b"),x.strftime("%Y"))

# Вывод интервейса программы (подсказки номеров функций)
def print_description():
	curent_date()
	print(Fore.RED + Back.WHITE +" Curent date: " + today[0] + " " + today[1] + " " + today[2] + "  " + Style.RESET_ALL + "   CWD:" + Fore.RED + Back.YELLOW +"  " + os.getcwd() + "  " + Style.RESET_ALL)
	print(Fore.BLUE+ "|__________________________ *** TEST FILE MANAGER in Python *** ________________________|")
	print("|_______________________________________________________________________________________|"+ Style.RESET_ALL)
	print("|                                    " + Fore.RED +"MAIN FUNCTION" + Style.RESET_ALL + "                                      |")
	print("|                                                                                       |")
	print("|   1. New Folder                                  C. Change directory                  |")
	print("|   2. Delete Folder                                                                    |")
	print("|   3. Rename Folder                               7. Copy Folder                       |")
	print("|                                                  8. Copy File                         |")
	print("|   4. New File  " + Fore.MAGENTA + "(inactiv)" + Style.RESET_ALL + "                         9. "+ Fore.BLUE +"List of files in directory"+ Style.RESET_ALL +"        |")
	print("|   5. Delete File                                 F. Find                              |")
	print("|   6. Rename File                                 H. Help   / "+ Fore.RED+"E: Exit"+ Style.RESET_ALL+"                  |")
	print("|   O. Open File                                                                        |")
	print("|_______________________________________________________________________________________|\n")

# main function for file manager

def list_file_and_dir(): # print list of file and folder in Curent Work Dir
	#print(Fore.RED + os.getcwd(),"\\" + Style.RESET_ALL) # => Curent Dir
	x = os.listdir()
	print(Fore.GREEN +"---------------"+ Style.RESET_ALL)
	for i in range(len(x)):
		print(i+1, x[i] + Style.RESET_ALL)
	print(Fore.GREEN +"---------------"+ Style.RESET_ALL)

def find(name):
	x = os.listdir()
	items = []
	for i in range(len(x)):
		if name in x[i]:
			items.append(x[i])


	if items == []:
		print("No result!\n Press ENTER button for return in main menu!")
		input()
		name = None
		clear()
		fm.print_description()
		get_command()
	else:
		for item in items:
			print(Fore.RED + "/ " + Style.RESET_ALL + item)
		print(Fore.GREEN + "Press " + Style.RESET_ALL + Fore.RED + "ENTER" + Style.RESET_ALL + Fore.GREEN + "button for return in main menu!" + Style.RESET_ALL)
		input()
		name = None

def copy_file(name,init_location, new_location):
	pass
