# Random Number Generator
# This script generates random numbers based on user-defined criteria.
# It includes a menu system, input validation, and a simple spinner animation.
# Requires the 'pyfiglet' library for ASCII art banners.
import random
import os
import time
import sys
from pyfiglet import Figlet, FigletFont

def generate_banner():
    try:
        figlet = Figlet(font='slant')  # Use a safe, visible font
        title = figlet.renderText("Zach's")
    except:
        title = "Zach's\n"

    subtitle = "RANDOM NUMBER GENERATOR"
    line = "-" * len(subtitle)
    return f"{title}{subtitle}\n{line}"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_menu():
    banner = generate_banner()
    print(banner)
    print(r"""
  ________________________________
 |                                |
 |      RANDOM NUMBER MENU        |
 |________________________________|
 | 1) Generate random numbers     |
 | 2) Exit                        |
 |________________________________|
""")

def spinner(text="Generating"):
    spinner_chars = ['|','/','-','\\']
    for i in range(20):
        sys.stdout.write('\r{} {}'.format(text, spinner_chars[i % len(spinner_chars)]))
        sys.stdout.flush()
        time.sleep(0.1)
    print("\rDone!           ")

def get_range():
    while True:
        start = int(input("Enter the starting number: "))
        end = int(input("Enter the ending number: "))
        if start == end:
            print("Start and End values cannot be the same. Try again.\n")
            continue
        if start > end:
            start, end = end, start
        return start, end

def get_amount():
    while True:
        amount = int(input("How many random numbers do you want to generate? "))
        if amount <= 0:
            print("Please enter a positive number.")
            continue
        return amount

def get_filter_choice():
    print("\nSelect number type:")
    print("1) Any")
    print("2) Even only")
    print("3) Odd only")
    while True:
        choice = input("Choice (1-3): ")
        if choice in ['1','2','3']:
            return choice
        print("Invalid choice. Please select 1, 2, or 3.")

def generate_random_numbers(start, end, amount, filter_choice):
    results = []
    attempts = 0
    while len(results) < amount:
        num = random.randint(start, end)
        if filter_choice == '2' and num % 2 != 0:
            continue
        if filter_choice == '3' and num % 2 == 0:
            continue
        results.append(num)
        attempts += 1
        if attempts > 1000:
            print("Generation limit exceeded. Check range and filter.")
            break
    return results

def main():
    while True:
        clear_screen()
        draw_menu()
        choice = input("Select an option: ")

        if choice == '1':
            clear_screen()
            print(generate_banner())
            print("=== Generate Random Numbers ===")
            start, end = get_range()
            amount = get_amount()
            filter_choice = get_filter_choice()
            print("\nGenerating numbers, please wait...\n")
            spinner("Generating")
            numbers = generate_random_numbers(start, end, amount, filter_choice)
            print(f"\n{amount} random number(s) between {start} and {end}:")
            print(numbers)
            input("\nPress ENTER to return to the menu...")

        elif choice == '2':
            print("Goodbye!")
            break

        else:
            print("Invalid selection. Please choose 1 or 2.")
            input("Press ENTER to continue...")

if __name__ == "__main__":
    main()
