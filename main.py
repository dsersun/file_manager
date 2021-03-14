"""
основной файл с реализацией файлового менеджера
"""
import file_manager_function_mod as fm
import os, colorama
from colorama import Fore, Back, Style
colorama.init()
command = None
function_code = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "C", "H", "c", "h", "+"]

def get_command(): # функция запрашивает у пользователя код желаемой операции
	global command
	command = str(input("Insert your command: >>> "))

# Удаляется содержимое экрана для вывода обновленного контента. Так исключается большая простыня выводов
def clear(): 
	os.system('cls' if os.name == 'nt' else 'clear')

fm.print_description() #list of function

get_command()

while command != "e":
	if command in function_code:
# Реализуем весь функционал ТУТ

# New Folder
		if command == "1": 
			clear()
			name_folder = input("Create New Folder,\ninsert Folder Name: >>>")
			os.mkdir(name_folder)
			clear()
			fm.print_description()
			print("Folder "+ Fore.GREEN + name_folder + Style.RESET_ALL + " created!")
			get_command()
# Delete Folder
		elif command == "2":
			clear()
			name_folder = input("Insert Folder Name for Delete: >>>")
			alert = input("Attention! The folder "+ name_folder +" will be deleted along with the files it contains!\nDo you want to continue? (Y / N):")
			if alert == "Y" or alert == "y":
				import shutil
				shutil.rmtree(name_folder)
				clear()
				fm.print_description()
				print("Folder "+ Fore.RED + name_folder + Style.RESET_ALL + " Deleted!")
				get_command()
			elif alert == "N" or alert == "n":
				clear()
				fm.print_description()
				print("Folder not deleted.")
				get_command()
			else:
				clear()
				fm.print_description()
				print("Invalid responce! Folder not deleted!")
				get_command()
# Rename Folder
		elif command == "3": 
			clear()
			old = input("Insert curent folder name: >>> ")
			new = input("Insert NEW folder name: >>> ")
			os.renames(old, new)
			old = new = None
			clear()
			fm.print_description()
			print("Folder renamed")
			get_command()

# Create file / temporary inactiv function
		elif command == "4":
			clear()
			fm.print_description()
			print("function in construction")
			get_command()

#  Delete file
		elif command == "5": 
			clear()
			file_name = input("Insert File Name for Delete: >>>")
			alert = input("You definitely want to delete the file" + file_name + "\n" + "Do you want to continue? (Y / N):")
			if alert == "Y" or alert == "y":
				if os.path.exists(file_name):
					os.remove(file_name)
					clear()
					fm.print_description()
					print("File "+ Fore.RED + file_name + Style.RESET_ALL + " Deleted!")
					get_command()
				else:
					clear()
					fm.print_description()
					print("The file does not exist and therefore can'n be deleted")
					get_command()		
			elif alert == "N" or alert == "n":
				clear()
				fm.print_description()
				print("File not deleted.")
				get_command()
			else:
				clear()
				fm.print_description()
				print("Invalid responce! File not deleted!")
				get_command()
# rename file
		elif command == "6":
			clear()
			fm.print_description()
			print("6")
			get_command()
# Copy folder
		elif command == "7":
			clear()
			fm.print_description()
			print("7")
			get_command()
# Copy file
		elif command == "8":
			clear()
			fm.print_description()
			print("8")
			get_command()


		elif command == "9":
			clear()
			fm.print_description()
			print("List of files in directory:")
			fm.list_file_and_dir()
			get_command()
# изменение текущей директории
		elif command == "c" or command == "C":
			clear()
			fm.print_description()
			print(Fore.RED + os.getcwd(),"\\" + Style.RESET_ALL)
			print("Change working directories")
			path = input("Insert new path: ")
			os.chdir(path)
			clear()
			fm.print_description()
			print(Fore.RED + os.getcwd(),"\\" + Style.RESET_ALL)
			get_command()
# Запрос помощи
		elif command == "h" or command == "H":
			clear()
			print(Fore.RED + "Help options is here"+ Style.RESET_ALL)
			print("******* HELP CONTENT *******\nfor MAIN Menu - insert '+' and press 'Enter'!")
			get_command()
		elif command == "+":
			clear()
			fm.print_description()
			get_command()
	else:
		clear()
		fm.print_description()
		print(Fore.RED + "Invalid value!"+ Style.RESET_ALL)
		get_command()
print("End of programm\nPress 'Enter'")
input()