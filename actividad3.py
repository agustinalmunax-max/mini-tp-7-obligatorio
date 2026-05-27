nombres = [" mara ", "TOMAS", "  luCIA", "mARcos  ", " SOFIA "]
nombres_normalizados = []

for n in nombres:
    nombre_limpio = n.strip().capitalize()
    nombres_normalizados.append(nombre_limpio)

print(nombres_normalizados)