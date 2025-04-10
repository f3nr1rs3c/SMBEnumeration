#!/usr/bin/env python
import os
import socket
from pyfiglet import Figlet
from colorama import init, Fore

init()

def clear_screen():
    os.system('clear')

def print_banner():
    f = Figlet(font='slant', width=200)
    print(Fore.CYAN + f.renderText('SMB Enumeration Kit') + Fore.RESET)
    print(Fore.RED + "                         | - |  By : Fenrir - Penetration Tester | - |              " + Fore.RESET)

def print_menu():
    print("""

{0}1){2} enum4linux
{0}2){2} nbtscan
{0}3){2} smbmap
{0}4){2} smbclient
{0}5){2} rpcclient
{0}6){2} nmblookup
{0}X) Exit Program{0}

          """.format(Fore.RED, "0", Fore.RESET))

def enum4linux():
    target = input(Fore.BLUE + "Enter target IP or hostname: " + Fore.RESET)
    os.system(f"enum4linux -a {target}")

def nbtscan():
    network = input(Fore.BLUE + "Enter target network (e.g., 192.168.1.0/24): " + Fore.RESET)
    os.system(f"nbtscan {network}")

def smbmap():
    target = input(Fore.BLUE + "Enter target IP or hostname: " + Fore.RESET)
    os.system(f"smbmap -H {target}")

def smbclient():
    target = input(Fore.BLUE + "Enter target IP or hostname: " + Fore.RESET)
    os.system(f"smbclient -L //{target}//")

def rpcclient():
    target = input(Fore.BLUE + "Enter target IP or hostname: " + Fore.RESET)
    username = input(Fore.BLUE + "Enter username: " + Fore.RESET)
    os.system(f"rpcclient -U {username}%password {target}")

def nmblookup():
    target = input(Fore.BLUE + "Enter target IP or hostname: " + Fore.RESET)
    os.system(f"nmblookup -A {target}")

def main():
    clear_screen()
    print_banner()
    print_menu()

    while True:
        choice = input(Fore.BLUE + "Enter a process number: " + Fore.RESET)
        
        if choice.lower() == "x":
            print(Fore.RED + "Exiting The Program..." + Fore.RESET)
            break

        elif choice == "1":
            enum4linux()
        
        elif choice == "2":
            nbtscan()
        
        elif choice == "3":
            smbmap()
        
        elif choice == "4":
            smbclient()
        
        elif choice == "5":
            rpcclient()
            
        elif choice == "6":
            nmblookup()
        
        else:
            print(Fore.RED + "Invalid input! Please try again." + Fore.RESET)

if __name__ == "__main__":
    main()
