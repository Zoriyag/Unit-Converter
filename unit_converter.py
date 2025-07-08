def convert_length():
    print("\n📏 Length Conversion")
    print("1. Inches to Centimeters")
    print("2. Centimeters to Inches")
    choice = input("Choose an option (1 or 2): ")
    value = float(input("Enter value: "))
    
    if choice == "1":
        print(f"{value} inches = {value * 2.54:.2f} cm")
    elif choice == "2":
        print(f"{value} cm = {value / 2.54:.2f} inches")
    else:
        print("Invalid selection.")

def convert_weight():
    print("\n⚖️ Weight Conversion")
    print("1. Pounds to Kilograms")
    print("2. Kilograms to Pounds")
    choice = input("Choose an option (1 or 2): ")
    value = float(input("Enter value: "))
    
    if choice == "1":
        print(f"{value} lbs = {value * 0.4536:.2f} kg")
    elif choice == "2":
        print(f"{value} kg = {value / 0.4536:.2f} lbs")
    else:
        print("Invalid selection.")

def convert_temperature():
    print("\n🌡 Temperature Conversion")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    choice = input("Choose an option (1 or 2): ")
    value = float(input("Enter value: "))
    
    if choice == "1":
        print(f"{value}°F = {(value - 32) * 5/9:.2f}°C")
    elif choice == "2":
        print(f"{value}°C = {(value * 9/5) + 32:.2f}°F")
    else:
        print("Invalid selection.")

while True:
    print("\n=== Unit Converter ===")
    print("1. Length")
    print("2. Weight")
    print("3. Temperature")
    print("4. Exit")
    
    option = input("Choose a category (1–4): ")

    if option == "1":
        convert_length()
    elif option == "2":
        convert_weight()
    elif option == "3":
        convert_temperature()
    elif option == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid input. Try again.")
