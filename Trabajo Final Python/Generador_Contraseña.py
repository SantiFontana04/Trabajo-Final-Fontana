import secrets, string, sys

diccionario = {
'letras': string.ascii_letters,
'numeros': string.digits,
'caracteres': string.punctuation
}

def generar_password(fuente_caracteres, longitud):
    password = ''.join(secrets.choice(fuente_caracteres)  for _ in range(longitud))
    password_lista = list(password)
    secrets.SystemRandom().shuffle(password_lista)
    return ''.join(password_lista)

while True:
    print("\n=========================")
    print("Generador de Contraseñas V0.1")
    print("=========================")
    print("1. Generar contraseña solo de Letras")
    print("2. Generar contraseña solo de Números")
    print("3. Generar contraseña de Letras y Números")
    print("4. Generar contraseña de Letras, Números, y Caracteres")
    print("0. Salir")
    opcion = input("Escriba la opción seleccionada: ")
    
    if opcion == "0":
        print("Saliendo del programa. ¡Hasta luego!")
        break

    try:
        longitud = int(input("Ingrese la longitud de la contraseña (mínimo 6 caracteres): "))
        if longitud < 6:
            print("La longitud debe ser de al menos 6 caracteres.")
            continue
    except ValueError:
        print("Por favor, ingrese un número entero.")
        continue
    
    if opcion == "1":
        fuente_caracteres = diccionario['letras']
    elif opcion == "2":
        fuente_caracteres = diccionario['numeros']
    elif opcion == "3":
        fuente_caracteres = diccionario['letras'] + diccionario['numeros']
    elif opcion == "4":
        fuente_caracteres = diccionario['letras'] + diccionario['numeros'] + diccionario['caracteres']
    else:
        print("Opción inválida. Por favor, elija una opción del menú.")
        continue
    
    contraseña = generar_password(fuente_caracteres, longitud)
    print(f"Contraseña generada: {contraseña}")

