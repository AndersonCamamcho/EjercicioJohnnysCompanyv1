import validation

def pedirEdad ():
    edad = int(input("Por favor ingrese su edad: "))
    validation.eage(edad)


if __name__ == '__main__':
    pedirEdad()