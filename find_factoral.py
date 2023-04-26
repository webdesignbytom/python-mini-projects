# Factortal n! is the multiplication of intergers that are <= n
## i.e 6! = 6*5*4*3*2*1

# Recursive funciton - calls itself at the end 
def factorial(n):
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)

num = 5
print("Factorial! of", num, "is", factorial(num))

# Iterative approach - 
def it_factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while(n > 1):
            fact *= n
            n -= 1
        return fact

print("Factorial! of", num, "is", it_factorial(num))