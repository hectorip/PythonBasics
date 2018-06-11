# -*- coding: utf-8 -*-
import time
# Fibonacci
# f(n) = f(n-1) + f (n-2)
# f(0) = 1
# f(1) = 1
# 1, 1, 2, 3, 5, 8, 13, 21
# 0, 1, 2, 3, 4, 5, 6, 7

def fibonacci(n):
    if n <= 1:
        return 1

    fn_1 = 1
    fn_2 = 1

    for i in range(2, n + 1):
        resultado = fn_1 + fn_2
        fn_2 = fn_1
        fn_1 = resultado
        # print(resultado)

    return resultado

start_time = time.time()
fibonacci(1000000)
end_time = time.time()
print("Tardó: %s" % (end_time - start_time))