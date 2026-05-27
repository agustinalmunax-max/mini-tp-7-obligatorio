edad = input("Ingrese su edad: ")
edad_limpia = edad.strip()

if edad_limpia.isnumeric():
    edad_introducida = int(edad_limpia)
    if edad_introducida >= 0 and edad_introducida <= 120:
        print(f"Edad ingresada: {edad_limpia}")
    else:
        print("Error: la edad debe estar entre 0 y 120")
else:
    print("Error: por favor, ingrese un numero valido")