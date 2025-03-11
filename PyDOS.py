import tkinter as tk
import os
import time
import subprocess
import shutil
import webbrowser
from os import listdir
from os.path import isfile, join
from colorama import init, Fore

init()

# Словарь с переводами
LANGUAGES = {
    "ru": {
        "welcome": "Добро пожаловать в PyDOS!",
        "prompt": "Введите команду PyDOS >>> ",
        "help": {
            "move": "move - Переместить папку, объект, файл.",
            "delete": "delete - Удалить папку, объект, файл.",
            "notepad": "notepad - Открывает блокнот.",
            "browser": "browser - Открывает браузер.",
            "dir": "dir - Показывает все файлы в директории.",
            "copy": "copy - Копирует файл в другое место.",
            "ipconfig": "ipconfig - Получение текущего IP-адреса, шлюза и подсетки.",
            "finger": "finger - Получение информации о пользователях.",
            "attrib": "attrib - Изменяет атрибуты файла.",
            "cls": "cls - Очищает экран консоли.",
            "cmd": "cmd - Открывает командную строку.",
            "rename": "rename - Изменяет название файла.",
        },
        "move": {
            "source": "Введите имя файла для перемещения: ",
            "current_dir": "Введите текущую директорию файла: ",
            "target_dir": "Введите директорию, куда переместить файл: ",
            "success": "Файл {} успешно перемещен в {}",
            "error_not_found": "Ошибка: Файл или директория не найдены.",
            "error_permission": "Ошибка: Недостаточно прав для перемещения файла.",
        },
        "delete": {
            "path": "Введите путь к файлу: ",
            "name": "Введите имя файла: ",
            "success": "Файл успешно удален.",
            "error_not_found": "Файл не найден.",
        },
        "notepad": "Открываю блокнот...",
        "browser": "Открываю браузер...",
        "dir": "Список файлов в текущей директории:",
        "copy": "Копирование файла...",
        "ipconfig": "Информация о сети:",
        "finger": "Введите имя пользователя: ",
        "attrib": "Неправильный формат команды ATTRIB. Допустимые команды: '+r', '-r', '+h', '-h'.",
        "cls": "Очистка экрана...",
        "cmd": "Открываю командную строку...",
        "rename": {
            "old_name": "Введите старое имя файла: ",
            "new_name": "Введите новое имя файла: ",
            "success": "Файл {} успешно переименован в {}.",
            "error_not_found": "Файл не найден.",
        },
    },
    "en": {
        "welcome": "Welcome to PyDOS!",
        "prompt": "Enter a PyDOS command >>> ",
        "help": {
            "move": "move - Move a folder, object, or file.",
            "delete": "delete - Delete a folder, object, or file.",
            "notepad": "notepad - Opens Notepad.",
            "browser": "browser - Opens the browser.",
            "dir": "dir - Shows all files in the directory.",
            "copy": "copy - Copies a file to another location.",
            "ipconfig": "ipconfig - Retrieves the current IP address, gateway, and subnet.",
            "finger": "finger - Retrieves information about users.",
            "attrib": "attrib - Changes file attributes.",
            "cls": "cls - Clears the console screen.",
            "cmd": "cmd - Opens the command prompt.",
            "rename": "rename - Renames a file.",
        },
        "move": {
            "source": "Enter the file name to move: ",
            "current_dir": "Enter the current directory of the file: ",
            "target_dir": "Enter the target directory: ",
            "success": "File {} successfully moved to {}",
            "error_not_found": "Error: File or directory not found.",
            "error_permission": "Error: Insufficient permissions to move the file.",
        },
        "delete": {
            "path": "Enter the file path: ",
            "name": "Enter the file name: ",
            "success": "File successfully deleted.",
            "error_not_found": "File not found.",
        },
        "notepad": "Opening Notepad...",
        "browser": "Opening the browser...",
        "dir": "List of files in the current directory:",
        "copy": "Copying file...",
        "ipconfig": "Network information:",
        "finger": "Enter the username: ",
        "attrib": "Invalid ATTRIB command format. Allowed commands: '+r', '-r', '+h', '-h'.",
        "cls": "Clearing the screen...",
        "cmd": "Opening the command prompt...",
        "rename": {
            "old_name": "Enter the old file name: ",
            "new_name": "Enter the new file name: ",
            "success": "File {} successfully renamed to {}.",
            "error_not_found": "File not found.",
        },
    },
}

# Выбор языка
print("Select language / Выберите язык:")
print("1. English")
print("2. Русский")
language_choice = input("Enter 1 or 2: ")

if language_choice == "1":
    lang = "en"
elif language_choice == "2":
    lang = "ru"
else:
    print("Invalid choice. Defaulting to English.")
    lang = "en"

# Переменные для перевода
messages = LANGUAGES[lang]

while True:
    print(Fore.YELLOW + "PyDOS - PORTALIUS & HOROSHIY .corp 2077 no copyrights")
    print(Fore.YELLOW + messages["welcome"])

    cmd = input(Fore.MAGENTA + messages["prompt"])

    if cmd == "help":
        time.sleep(1)
        for command in messages["help"].values():
            print(command)

    elif cmd == "move":
        time.sleep(1)
        file_name = input(messages["move"]["source"])
        current_dir = input(messages["move"]["current_dir"])
        target_dir = input(messages["move"]["target_dir"])

        src_file = os.path.join(current_dir, file_name)
        dst_file = os.path.join(target_dir, file_name)

        try:
            shutil.move(src_file, dst_file)
            print(messages["move"]["success"].format(file_name, target_dir))
        except FileNotFoundError:
            print(messages["move"]["error_not_found"])
        except PermissionError:
            print(messages["move"]["error_permission"])
        except Exception as e:
            print(f"An error occurred: {e}")

    elif cmd == "delete":
        time.sleep(1)
        current_dir = input(messages["delete"]["path"])
        file_name = input(messages["delete"]["name"])
        file_path = os.path.join(current_dir, file_name)

        if os.path.exists(file_path):
            os.remove(file_path)
            print(messages["delete"]["success"])
        else:
            print(messages["delete"]["error_not_found"])

    elif cmd == "notepad":
        time.sleep(1)
        print(Fore.GREEN + messages["notepad"])
        subprocess.Popen(['notepad.exe'])

    elif cmd == "browser":
        time.sleep(1)
        print(Fore.GREEN + messages["browser"])
        url_to_open = "https://www.google.com"
        webbrowser.open(url_to_open)

    elif cmd == "dir":
        time.sleep(1)
        mypath = "."
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        print(messages["dir"])
        print(onlyfiles)

    elif cmd == "copy":
        time.sleep(1)
        def copy_file(source_file, destination_file):
            with open(source_file, 'rb') as f_source:
                with open(destination_file, 'wb') as f_destination:
                    f_destination.write(f_source.read())
        print(messages["copy"])
        copy_file('source.txt', 'destination.txt')

    elif cmd == "ipconfig":
        time.sleep(1)
        cmd = "ipconfig"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        print(messages["ipconfig"])
        print(result.stdout)

    elif cmd == "finger":
        time.sleep(1)
        def finger(username):
            os.system(f"finger {username}")
        username = input(messages["finger"])
        finger(username)

    elif cmd == "attrib":
        time.sleep(1)
        def attrib(command, filename):
            if command == '+r':
                os.system(f'attrib +r {filename}')
            elif command == '-r':
                os.system(f'attrib -r {filename}')
            elif command == '+h':
                os.system(f'attrib +h {filename}')
            elif command == '-h':
                os.system(f'attrib -h {filename}')
            else:
                print(messages["attrib"])
        attrib('+r', 'example.txt')

    elif cmd == "cls":
        time.sleep(1)
        def clear_screen():
            os.system('cls' if os.name == 'nt' else 'clear')
        print(messages["cls"])
        clear_screen()

    elif cmd == "cmd":
        time.sleep(1)
        cmd_command = "cmd"
        print(messages["cmd"])
        os.system(cmd_command)

    elif cmd == "rename":
        time.sleep(1)
        def rename_file(old_name, new_name):
            try:
                os.rename(old_name, new_name)
                print(messages["rename"]["success"].format(old_name, new_name))
            except FileNotFoundError:
                print(messages["rename"]["error_not_found"])
        old_name = input(messages["rename"]["old_name"])
        new_name = input(messages["rename"]["new_name"])
        rename_file(old_name, new_name)
