import math

def factorial(n):
    return math.factorial(n)

def fibonacci(n):
    seq = []
    a, b = 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def gcd(a, b):
    return math.gcd(a, b)

def main():
    while True:
        print("\n--- Math Utility ---")
        print("1. Factorial")
        print("2. Fibonacci sequence")
        print("3. Prime check")
        print("4. GCD (Greatest Common Divisor)")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            n = int(input("Enter a number: "))
            print("Factorial:", factorial(n))
        elif choice == "2":
            n = int(input("Enter number of terms: "))
            print("Fibonacci sequence:", fibonacci(n))
        elif choice == "3":
            n = int(input("Enter a number: "))
            print("Prime?" , is_prime(n))
        elif choice == "4":
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("GCD:", gcd(a, b))
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
