def fibonacci(n):
    a, b = 0, 1
    while a < n:
        print(a, end='C ')
        a, b = b, a + b
fibonacci(1000)
