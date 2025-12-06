def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль"
    return a / b

if __name__ == "__main__":
    print("2 + 3 =", add(2, 3))
    print("5 - 2 =", subtract(5, 2))
    print("4 * 3 =", multiply(4, 3))
    print("10 / 2 =", divide(10, 2))

def square(a):
    return a * a
