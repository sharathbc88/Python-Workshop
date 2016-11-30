"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
__author__ = 'Sharath'



def convert_celsius_to_fahrenheit(celsius):
   # celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print("Result: {:.2f} F".format(fahrenheit))


def convert_fahrenheit_to_celsius(fahrenheit):
   # fahrenheit = float(input("fahrenheit:"))
    celsius = 5 / 9 * (fahrenheit - 32)
    print("Result: {:.2f} F".format(celsius))


MENU = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ (for quit)"
print(MENU)
choice = input(">>> ").upper()
temperature = float(input("Enter temperature:"))

while choice != "Q":
    if choice == "C":
        convert_celsius_to_fahrenheit(temperature)
    elif choice == "F":
        convert_fahrenheit_to_celsius(temperature)
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")
