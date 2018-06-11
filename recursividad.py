# -*- coding: utf-8 -*-
# Recursividad

# f(n) = f(n-1) + f (n-2)

def fibonacci(n):
    print(n)
    if n <= 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(100))