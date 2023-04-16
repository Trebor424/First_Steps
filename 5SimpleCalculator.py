def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def calc(func, num1, num2):
    print(f'{num1}\n{num2}')
    if func == "+":
        wynik=add(num1,num2)
        print(f'Wynik dodawania {wynik}')
    elif func == "-":
        wynik=subtract(num1,num2)
        print(f'Wynik odejmowania {wynik}')
    elif func == "*":
        wynik=multiply(num1, num2)
        print(f'Wynik mnożenia {wynik}')
    else:
        print("podałeś coś źle, sam sobie radź")


print(f'podaj kolejno rodzaj funkcji "+, -, * '
      f'\n oraz wpisz 2 liczby do obliczeń')

calc(input(),float(input()),float(input()))
