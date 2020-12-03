def main():
    MENU = """C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice=="C":
            choice=c_C()
        elif choice=="F":
            choice=c_F()
        else:
            print("Invalid option")
        print(choice)
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you")

def c_C():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit

def c_F():
    fahrenheit = float(input("Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9.0
    return celsius

main()