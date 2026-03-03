def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)

def fibonacci(n):
    a, b = 0, 1
    seq = []
    for _ in range(n):
        seq.append(a)
        a, b = b, a+b
    return seq
    

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

choice = int(input("1.Factorial 2.Fibonacci 3.Prime: "))
num = int(input("Enter number: "))
print(factorial(num) if choice==1 else fibonacci(num) if choice==2 else is_prime(num))
