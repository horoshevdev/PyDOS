import tkinter as tk
import os
import time
import subprocess

time.sleep(1)
print("Установка зависимостей/Installing dependences...")
print("Пожалуйста подождите/Please wait...")
subprocess.run(['pip', 'install', 'colorama'])
subprocess.run(['python.exe', '-m', 'pip', 'install', '--upgrade', 'pip'])

import shutil
import webbrowser
from os import listdir
from os.path import isfile, join
from colorama import init, Fore

init()

while True:
    print(Fore.YELLOW + "PyDOS - PORTALIUS & HOROSHIY .corp 2077 no copyrights")
    print(Fore.YELLOW + "Добро пожаловать в PyDOS!")

    cmd = input(Fore.MAGENTA + "Введите команду PyDOS >>> ")
    
    if cmd == "help":
        time.sleep(1)
        print("move - Переместить папку, объект, файл.")
        print("delete - удалить папку, объект, файл.")
        print("notepad - открывает блокнот.")
        print("browser - открывает браузер.")
        print("dir - показывает все файлы в директории.")
        print("copy - копирует файл в другое место:")
        print("ipconfig - получение текущего IP-адреса, шлюза и подсетки:")
        print("finger - получение информации о пользователях:")
        print("attrib - изменяет атрибуты файла:")
        print("cls - очищает экран консоли:")
        print("cmd - открывает командую строку:")
        print("rename - изменяет название файла:")
        print("Больше команд скоро!")

    if cmd == "move":
        time.sleep(1)
        file_name = input("Введите имя файла для перемещения: ")
        current_dir = input("Введите текущую директорию файла: ")
        target_dir = input("Введите директорию, куда переместить файл: ")

        src_file = os.path.join(current_dir, file_name)
        dst_file = os.path.join(target_dir, file_name)

        try:
            shutil.move(src_file, dst_file)
            print(f"Файл {file_name} успешно перемещен в {target_dir}")
        except FileNotFoundError:
            print("Ошибка: Файл или директория не найдены.")
        except PermissionError:
            print("Ошибка: Недостаточно прав для перемещения файла.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

    if cmd == "delete":
        time.sleep(1)
        current_dir = input("Введите путь к файлу: ")
        file_name = input("Введите имя файла: ")
        file_path = os.path.join(current_dir, file_name)

        if os.path.exists(file_path):
            os.remove(file_path)
            print("Файл успешно удален.")
        else:
            print("Файл не найден.")

    if cmd == "notepad":
        time.sleep(1)
        print(Fore.GREEN + "Открываю блокнот...")
        subprocess.Popen(['notepad.exe'])

    if cmd == "browser":
        time.sleep(1)
        print(Fore.GREEN + "Открываю браузер...")
        url_to_open = "https://www.google.com"
        webbrowser.open(url_to_open)

    if cmd == "dir":
        time.sleep(1)
        mypath = "."

        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        print(onlyfiles)

    if cmd == "copy":
        time.sleep(1)
        def copy_file(source_file, destination_file):
            with open(source_file, 'rb') as f_source:
                with open(destination_file, 'wb') as f_destination:
                    f_destination.write(f_source.read())

        copy_file('source.txt', 'destination.txt')

    if cmd == "ipconfig":
        time.sleep(1)
        cmd = "ipconfig"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

        print(result.stdout)

    if cmd == "finger":
        time.sleep(1)
        def finger(username):
            os.system(f"finger {username}")

        username = input("Введите имя пользователя: ")
        finger(username)

    if cmd == "attrib":
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
            print("Неправильный формат команды ATTRIB. Допустимые команды: '+r', '-r', '+h', '-h'.")

    if cmd == "cls":
        time.sleep(1)
        def clear_screen():
            os.system('cls' if os.name == 'nt' else 'clear')

        clear_screen()

    if cmd == "cmd":
        time.sleep(1)
        cmd_command = "cmd"

        os.system(cmd_command)
    
    if cmd == "rename":
        time.sleep(1)
    def rename_file(old_name, new_name):
        try:
            os.rename(old_name, new_name)
            print(f"Файл {old_name} успешно переименован в {new_name}.")
        except FileNotFoundError:
            print("Файл не найден.")

    cmd = "rename"
    if cmd == "rename":
        time.sleep(1)
        rename_file("старое_имя.txt", "новое_имя.txt")
