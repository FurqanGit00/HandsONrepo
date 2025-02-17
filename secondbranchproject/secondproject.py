def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

num_terms = int(input("Enter number of Fibonacci terms: "))
print(list(fibonacci_generator(num_terms)))