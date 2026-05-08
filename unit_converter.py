def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9

def kg_to_lb(kg):
    return kg * 2.20462

def lb_to_kg(lb):
    return lb / 2.20462

def menu():
    print("\n--- Unit Converter ---")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    print("3. Celsius to Fahrenheit")
    print("4. Fahrenheit to Celsius")
    print("5. Kilograms to Pounds")
    print("6. Pounds to Kilograms")
    print("7. Exit")

while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        km = float(input("Enter kilometers: "))
        print(f"{km} km = {km_to_miles(km):.2f} miles")
    elif choice == "2":
        miles = float(input("Enter miles: "))
        print(f"{miles} miles = {miles_to_km(miles):.2f} km")
    elif choice == "3":
        c = float(input("Enter Celsius: "))
        print(f"{c}°C = {c_to_f(c):.2f}°F")
    elif choice == "4":
        f = float(input("Enter Fahrenheit: "))
        print(f"{f}°F = {f_to_c(f):.2f}°C")
    elif choice == "5":
        kg = float(input("Enter kilograms: "))
        print(f"{kg} kg = {kg_to_lb(kg):.2f} lb")
    elif choice == "6":
        lb = float(input("Enter pounds: "))
        print(f"{lb} lb = {lb_to_kg(lb):.2f} kg")
    elif choice == "7":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice, try again.")

