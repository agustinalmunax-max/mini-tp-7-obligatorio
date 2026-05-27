codigo = input("Ingrese el código de la materia (ej: PROG-101): ")

codigo_limpio = codigo.strip().upper()

if codigo_limpio.count("-") == 1:
    partes = codigo_limpio.split("-")
    parte_letras = partes[0]
    parte_numeros = partes[1]
    if parte_letras.isalpha() and parte_numeros.isdigit():
        print(f"Codigo valido: {codigo_limpio}")
    else:
        print("Error: el formato no es valido. debe contener letras en el lado izquierdo y nnumeros en el lado derecho")
else:
    print("Error: el codigo debe tener un solo guion")