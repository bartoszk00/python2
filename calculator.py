def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Nie mozna dzielic przez zero"
    return a / b

print("Wynik dodawania:", add(5, 3))
print("Wynik odejmowania:", subtract(10, 4))
print("Wynik mnozenia:", multiply(4, 5))
print("Wynik dzielenia:", divide(10, 2))