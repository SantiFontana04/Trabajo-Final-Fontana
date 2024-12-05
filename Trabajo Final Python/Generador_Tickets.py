import pickle, sys, os, random

# Crear carpeta para guardar los tickets
if not os.path.exists("tickets"):
    os.makedirs("tickets")

def crear_ticket():
    """Función para crear un ticket."""
    os.system("cls" if os.name == "nt" else "clear")
    print("=== CREAR TICKET ===")
    
    nombre = input("Ingrese su nombre: ")
    sector = input("Ingrese el sector: ")
    asunto = input("Ingrese el asunto: ")
    problema = input("Describa el problema: ")
    
    numero_random = random.randint(1000, 9999)
    ticket = {
        "numero": numero_random,
        "nombre": nombre,
        "sector": sector,
        "asunto": asunto,
        "problema": problema
    }
    
    # Guardar el ticket
    archivo = f"tickets/ticket_{numero_random}.pkl"
    with open(archivo, "wb") as f:
        pickle.dump(ticket, f)
    
    # Mostrar el ticket generado
    print("\n=== TICKET GENERADO ===")
    for clave, valor in ticket.items():
        print(f"{clave.capitalize()}: {valor}")
    print("\n¡Recuerde su número de ticket para futuras consultas!")
    
    # Preguntar si desea crear otro ticket
    while True:
        opcion = input("¿Desea crear otro ticket? (s/n): ").lower()
        if opcion == "s":
            crear_ticket()
            break
        elif opcion == "n":
            break
        else:
            print("Opción inválida. Por favor ingrese 's' o 'n'.")

def leer_ticket():
    """Función para leer un ticket."""
    os.system("cls" if os.name == "nt" else "clear")
    print("=== LEER TICKET ===")
    
    while True:
        try:
            numero_ticket = int(input("Ingrese el número de ticket: "))
            archivo = f"tickets/ticket_{numero_ticket}.pkl"
            
            if not os.path.isfile(archivo):
                print("Error: El ticket no existe.")
            else:
                with open(archivo, "rb") as f:
                    ticket = pickle.load(f)
                
                print("\n=== TICKET ENCONTRADO ===")
                for clave, valor in ticket.items():
                    print(f"{clave.capitalize()}: {valor}")
            
        except ValueError:
            print("Error: Ingrese un número válido.")
        
        # Preguntar si desea leer otro ticket
        opcion = input("\n¿Desea leer otro ticket? (s/n): ").lower()
        if opcion == "n":
            break
        elif opcion != "s":
            print("Opción inválida. Regresando al menú principal.")
            break

def salir():
    """Función para salir del programa."""
    confirmar = input("¿Está seguro de que desea salir? (s/n): ").lower()
    if confirmar == "s":
        print("Saliendo del programa...")
        sys.exit()
    else:
        print("Cancelando salida. Regresando al menú principal.")

# Menú principal
def menu_principal():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("===== MENÚ PRINCIPAL =====")
        print("1. Crear ticket")
        print("2. Leer ticket")
        print("0. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            crear_ticket()
        elif opcion == "2":
            leer_ticket()
        elif opcion == "0":
            salir()
        else:
            print("Opción inválida. Intente de nuevo.")


menu_principal()