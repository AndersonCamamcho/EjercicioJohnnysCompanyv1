import validation

def pedirDatos ():
    name = input("Regalame su nombre, por favor: ")
    edad = int(input("Por favor ingrese su edad: "))
    validation.eage(edad, name)


if __name__ == '__main__':
    pedirDatos()