"""
Модуль с функциями для файлового менеджера
"""
import datetime, os

def curent_date():
	x = datetime.datetime.now()
	global today
	today = (x.strftime("%d"),x.strftime("%b"),x.strftime("%Y"))

def print_description():
	curent_date()
	print(" Curent date: " + today[0] + " " + today[1] + " " + today[2])
	print("|__________________________ *** TEST FILE MANAGER in Python *** ________________________|")
	print("|_______________________________________________________________________________________|")
	print("|                                    MAIN FUNCTION                                      |")
	print("|                                                                                       |")
	print("|   1. New Folder                                  C. Change directory                  |")
	print("|   2. Delete Folder                                                                    |")
	print("|   3. Rename Folder                               7. Copy Folder                       |")
	print("|                                                  8. Copy File                         |")
	print("|   4. New File                                    9.                                   |")
	print("|   5. Delete File                                                                      |")
	print("|   6. Rename File                                 H. Help                              |")
	print("|_______________________________________________________________________________________|\n")


def get_command(): # функция запрашивает у пользователя код желаемой операции
	global Command
	Command = input("Command: ")

# main function for file manager

def list_file_and_dir(): # print list of file and folder in Curent Work Dir
	print(os.getcwd(),"\\") # => Curent Dir
	x = os.listdir()
	print("---------------")
	for i in range(len(x)):
		print(i+1, x[i])
	print("---------------")

def new_folder(name):
	pass

def del_folder(name):
	pass

def rename_folder(name1, name2):
	pass

def new_file(name):
	pass

def del_file(name):
	pass

def rename_file(name1, name2):
	pass

def copy_file(name,init_location, new_location):
	pass
