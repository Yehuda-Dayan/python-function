def fibonacci(n):
   
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
num = int(input("Enter a non-negative integer: "))
print(f"The {num}th Fibonacci number is: {fibonacci(num)}")