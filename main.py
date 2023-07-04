fibonacci_calculado = {}

def fibonacci(n):
    if n == 0:
        return 1

    if n == 1:
        return 1

    valor_calculado = fibonacci_calculado.get(n)

    if valor_calculado is None:
        fibonacci_calculado[n] = fibonacci(n - 1) + fibonacci(n - 2)

    return fibonacci_calculado[n]


def print_fibonacci(n):
    print('F(' + str(n) + '):' + str(fibonacci(n)))


for i in range(0,100):
    print_fibonacci(i)
