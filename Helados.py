import random

helados = []

def crear_helado():
    nombre = input("Ingrese el nombre del helado: ")
    descripcion = input("Ingrese la descripción del helado: ")
    while True:
        try:
            precio = float(input("Ingrese el precio unitario del helado: "))
            break
        except ValueError:
            print("Por favor, ingrese un valor numérico para el precio.")
    
    id_helado = random.randint(0, 15)
    
    while any(helado["id"] == id_helado for helado in helados):
        id_helado = random.randint(0, 15)

    helado = {
        "id": id_helado,
        "nombre": nombre,
        "descripcion": descripcion,
        "precio": precio
    }
    
    helados.append(helado)
    print(f"Helado '{nombre}' creado con éxito. ID: {id_helado}")

def ver_helados():
    if len(helados) == 0:
        print("No hay helados registrados.")
    else:
        helados_ordenados = sorted(helados, key=lambda x: x['precio'], reverse=True)
        
        print("\nLista de helados registrados (ordenados por precio de mayor a menor):")
        for helado in helados_ordenados:
            print(f"ID: {helado['id']} | Nombre: {helado['nombre']} | Descripción: {helado['descripcion']} | Precio: {helado['precio']}")

def modificar_helado():
    id_helado = input("Ingrese el ID del helado a modificar: ")
    helado_encontrado = None
    
    for helado in helados:
        if str(helado["id"]) == id_helado:
            helado_encontrado = helado
            break
    
    if helado_encontrado:
        print(f"Helado encontrado: {helado_encontrado['nombre']}")
        nuevo_nombre = input("Ingrese el nuevo nombre del helado: ")
        nueva_descripcion = input("Ingrese la nueva descripción del helado: ")
        while True:
            try:
                nuevo_precio = float(input("Ingrese el nuevo precio unitario del helado: "))
                break
            except ValueError:
                print("Por favor, ingrese un valor numérico para el precio.")
        
        helado_encontrado["nombre"] = nuevo_nombre
        helado_encontrado["descripcion"] = nueva_descripcion
        helado_encontrado["precio"] = nuevo_precio
        
        print(f"Helado '{helado_encontrado['nombre']}' actualizado con éxito.")
    else:
        print("Helado no encontrado con ese ID.")

def eliminar_helado():
    id_helado = input("Ingrese el ID del helado a eliminar: ")
    helado_encontrado = None
    
    for helado in helados:
        if str(helado["id"]) == id_helado:
            helado_encontrado = helado
            break
    
    if helado_encontrado:
        helados.remove(helado_encontrado)
        print(f"Helado '{helado_encontrado['nombre']}' eliminado con éxito.")
    else:
        print("Helado no encontrado con ese ID.")

def menu():
    while True:
        print("\n--- Gestión de Helados ---")
        print("1. Crear un helado")
        print("2. Ver lista de helados")
        print("3. Modificar un helado")
        print("4. Eliminar un helado")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            crear_helado()
        elif opcion == "2":
            ver_helados()
        elif opcion == "3":
            modificar_helado()
        elif opcion == "4":
            eliminar_helado()
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

menu()





