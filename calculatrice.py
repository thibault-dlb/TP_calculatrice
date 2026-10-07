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

if __name__ == "__main__" :
    print(add())
    print(substracte())
    print(multiply())
    print(divide())