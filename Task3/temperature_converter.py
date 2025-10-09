import os
from colorama import Fore,Style,init
import time
init(autoreset=True)
HISTORY_FILE = "history.txt"
def celsius_to_fahrenheit(c):
    return(c * 9/5)+32
def celsius_to_kelvin(c):
    return c + 273.15
def fahrenheit_to_celsius(f):
    return(f - 32)*5/9
def fahrenheit_to_kelvin(f):
    return(f -32)*5/9 + 273.15
def kelvin_to_celsius(k):
    return k - 273.15
def kelvin_to_fahrenheit(k):
    return (k - 273.15)*9/5 + 32
def loading_animation():
    print(Fore.YELLOW + "Converting")
    time.sleep(1)
def save_history(entry):
    with open(HISTORY_FILE,"a") as file:
        file.write(entry + "\n")
def view_history():
    print(Fore.CYAN + "\nConversion History:")
    if not os.path.exists(HISTORY_FILE):
        print(Fore.YELLOW + "No conversion history found yet")
        return
    with open(HISTORY_FILE,"r") as file:
        lines = file.readlines()
        if not lines:
            print(Fore.YELLOW + "(Empty)")
        else:
            for line in lines:
                print(Fore.GREEN + "-" + line.strip())

def temperature_converter():
    print(Fore.CYAN + Style.BRIGHT + "\nTemperature Converter")
    print(Fore.MAGENTA + "  ")
    while True:
        print(Fore.BLUE + "\nselect an option:")
        print(Fore.WHITE + "1. Celsius -> Fahrenheit & Kelvin")
        print("2. Fahrenheit -> Celsius & Kelvin")
        print("3. Kelvin -> Celsius & Fahrenheit")
        print("4. View Conversion History")
        print("5. Exit")
        choice = input(Fore.YELLOW + "\nEnter your choice(1-5):")
        if choice == "1":
            try:
                c = float(input(Fore.WHITE + "Enter temperature in Celsius:"))
                loading_animation()
                f = celsius_to_fahrenheit(c)
                k = celsius_to_kelvin(c)
                result = f"{c:.2f}0C = {f:.2f}0F | {k:.2f}K"
                print(Fore.GREEN + "",result)
                save_history(result)
            except ValueError:
                print(Fore.RED + "Invalid input! Please enter a number")
        elif choice == "2":
            try:
                f = float(input(Fore.WHITE + "Enter temperature in Fahrenheit:"))
                loading_animation()
                c = fahrenheit_to_celsius(f)
                k = fahrenheit_to_kelvin(f)
                result = f"{f:.2f}0F = {c:.2F}0C | {k:.2f}K"
                print(Fore.GREEN + "", result)
                save_history(result)
            except ValueError:
                print(Fore.RED + "Invalid input!Please enter a number")
        elif choice == "2":
            try:
                f = float(input(Fore.WHITE + "Enter temperature in Fahrenheit:"))
                loading_animation()
                c = fahrenheit_to_celsius(f)
                k = fahrenheit_to_kelvin(f)
                result = f"{f:.2f}0F = {c:.2F}0C | {k:.2f}K"
                print(Fore.GREEN + "", result)
                save_history(result)
            except ValueError:
                print(Fore.RED + "Invalid input!Please enter a number")
                 
        elif choice == "3":
            try:
                k = float(input(Fore.WHITE + "Enter temperature in Kelvin:"))
                loading_animation()
                c = kelvin_to_celsius(k)
                k = kelvin_to_fahrenheit(k)
                result = f"{k:.2f}K = {c:.2F}0C | {f:.2f}0F"
                print(Fore.GREEN + "", result)
                save_history(result)
            except ValueError:
                print(Fore.RED + "Invalid input!Please enter a number")
        elif choice == "4":
            view_history()
        elif choice == "5":
            print(Fore.CYAN + "\nThank you for using the Temperature Converter!")
            break
        else:
            print(Fore.RED + "Invalid choice!please enter a number from 1-5")
if __name__ == "__main__":
    temperature_converter()
