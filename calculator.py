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

print("1. Dodawanie")
print("2. Odejmowanie")
print("3. Mnozenie")
print("4. Dzielenie")

choice = input("Wybierz operacje (1-4): ")
a = float(input("Podaj pierwsza liczbe: "))
b = float(input("Podaj druga liczbe: "))

if choice == "1":
    print("Wynik:", add(a, b))
elif choice == "2":
    print("Wynik:", subtract(a, b))
elif choice == "3":
    print("Wynik:", multiply(a, b))
elif choice == "4":
    print("Wynik:", divide(a, b))