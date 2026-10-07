def add ():
    a = float(input("a = "))
    b = float(input("b = "))
    return a + b

def substracte():
    a = float(input("a = "))
    b = float(input("b = "))
    return a - b

def multiply():
    a = float(input("a = "))
    b = float(input("b = "))
    return a * b

def divide():
    a = float(input("a = "))
    b = 0
    while b == 0 :
        print("'b' doit être différent de 0")
        b = float(input("b = "))
    return a / b

def power():
    a = float(input("a = "))
    b = float(input("b = "))
    return a ** b

def menu():
    choix = 0
    while choix not in [1, 2, 3, 4, 5]:
        print("Choisissez votre opération (1 pour add, 2 pour substracte, 3 pour multiply, 4 pour divide et 5 pour power)")
        choix = int(input("Choix : "))
    match choix:
        case 1:
            result = add()
        case 2:
            result = substracte()
        case 3:
            result = multiply()
        case 4:
            result = divide()
        case 5:
            result = power()
        case _:
            print("Erreur")
    return result


if __name__ == "__main__" :
    print(menu())