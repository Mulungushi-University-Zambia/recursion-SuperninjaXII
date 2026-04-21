def f(n):
    if n == 0 or n == 1 or None:
        return 1
    return n * f(n-1)

print(f(7))