# -*- coding: utf-8 -*-
import os
import sys
import platform
import time

g = "\033[32;1m"
gt = "\033[0;32m"
bt = "\033[34;1m"
b = "\033[36;1m"
m = "\033[31;1m"
c = "\033[0m"
p = "\033[37;1m"
u = "\033[35;1m"
M = "\033[3;1m"
k = "\033[33;1m"
kt = "\033[0;33m"
a = "\033[30;1m"

W = '\x1b[0m'
R = '\x1b[31m'
G = '\x1b[1;32m'
O = '\x1b[33m'
B = '\x1b[34m'
P = '\x1b[35m'
C = '\x1b[36m'
GR = '\x1b[37m'



semut=(gt+"""
 #####  ####### #     # #     # ####### 
#     # #       ##   ## #     #    #    
#       #       # # # # #     #    #    
 #####  #####   #  #  # #     #    #    
      # #       #     # #     #    #    
#     # #       #     # #     #    #    
 #####  ####### #     #  #####     #    
 =================================
""")
l="Harap tunggu.."

def main_menu():
    clear()
    print(p+"INSTALASI SUKSES 100%" +
"\n ---> 鈥⑩€⑩€⑩€⑩€⑩€⑩€⑩€⑩€⑩€⑩€⑩€⑩€⑩€⑩€� <---"
        "\n ---> TELKOMSEL 5GB RP 0<---"
        "\n  [1] MULAI TEMBAK" + 
        "\n  [0] Exit" 
"\n ---> 鈥⑩€⑩€⑩€⑩€⑩€⑩€⑩€⑩€⑩€⑩€⑩€⑩€⑩€⑩€� <---"
    )
    choice = str(input(" CONTOH : 1 -> "))
    exec_menu(choice)
    return

def exec_menu(choice):
    clear()
    if(choice == ''):
        menu_actions['main']()
    else:
        try:
            menu_actions[choice]()
        except KeyError:
            print("Invalid selection, please try again.\n")
            menu_actions['main']()
    return

def menu_1():
    os.system('php dor.php')

def menu_2():
    print(m+"errrrrrrrrrroroorororororoororo")
    

def exit():
    sys.exit()

def clear():
    return os.system("cls") if (platform.system() == 'Windows') else os.system("clear")

menu_actions = {
    "main" : main_menu,
    "1" : menu_1,
    "2" : menu_2,
    "0" : exit
}


if __name__ == "__main__":
    main_menu()




