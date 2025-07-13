vehiculos = {
    'TOY8475': ['Toyota', 2019, '65000km', 'Gasolina', 'Automática', '1.8L 4cil', 'Blanco'],
    'FOR2175': ['Ford', 2017, '85000km', 'Gasolina', 'Manual', '1.6L 4cil', 'Azul'],
    'CHE9834': ['Chevrolet', 2020, '25000km', 'Gasolina', 'Automática', '2.0L 4cil', 'Negro'],
    'NIS7654': ['Nissan', 2016, '95000km', 'Gasolina', 'Manual', '1.6L 4cil', 'Rojo'],
    'HYU4521': ['Hyundai', 2021, '15000km', 'Híbrido', 'Automática', '1.6L 4cil', 'Gris'],
    'KIA3456': ['Kia', 2018, '75000km', 'Diesel', 'Manual', '2.0L 4cil', 'Blanco'],
    'MAZ8901': ['Mazda', 2019, '55000km', 'Gasolina', 'Automática', '2.5L 4cil', 'Rojo'],
    'SUB2468': ['Subaru', 2020, '30000km', 'Gasolina', 'Manual', '2.0L 4cil', 'Verde'],
    'TOY2222': ['Toyota', 2022, '22000km', 'Gasolina', 'Automática', '1.8L 4cil', 'Negro'],

}

inventario = {
    'TOY8475': [8500000, 1],
    'FOR2175': [6200000, 1], 
    'CHE9834': [12750000, 1],
    'NIS7654': [5400000, 2], 
    'HYU4521': [15200000, 1], 
    'KIA3456': [7800000, 1],
    'MAZ8901': [9200000, 1], 
    'SUB2468': [11500000, 0],
    'TOY2222': [2200000, 12],

}

#calcula el stock de vehiculos disponibles en el inventario para una marca especifica
def inventario_marca(marca):
    total_stock = 0 #variable para acumular el stock total
    marca_buscada = marca.lower() #convierte la marca ingresada a minusculas
    
    #recorre todos los vehiculos
    for codigo, datos in vehiculos.items():
        marca_vehiculo = datos[0].lower() #obtiene la marca del vehiculo en minusculas
        if marca_vehiculo == marca_buscada:
            if codigo in inventario:
                stock_vehiculo = inventario[codigo][1] #obtiene el stock del vehiculo
                if stock_vehiculo > 0:
                    total_stock = total_stock + stock_vehiculo
    
    print(f"El inventario de {marca} es: {total_stock}")

#busca vehiculos dentro de un rango de precios y con stock disponible
def busqueda_precio(precio_min, precio_max):
    vehiculos_encontrados = []
    
    for codigo, datos_inventario in inventario.items():
        precio = datos_inventario[0]
        stock = datos_inventario[1]
        
        if precio_min <= precio <= precio_max and stock > 0:
            if codigo in vehiculos:
                marca = vehiculos[codigo][0]
                formato_resultado = f"{marca}--{codigo}"
                vehiculos_encontrados.append(formato_resultado)
    
    vehiculos_encontrados.sort() #ordena alfabéticamente los vehículos encontrados
    
    if len(vehiculos_encontrados) > 0:
        print(f"Los vehículos en el rango de precios consultado son: {vehiculos_encontrados}")
    else:
        print("No hay vehículos en ese rango de precios.")

#actualiza el precio de un vehículo en el inventario
def actualizar_precio(codigo, precio_nuevo):
    if codigo in inventario: #verifica si el código del vehículo existe
        inventario[codigo][0] = precio_nuevo
        return True
    else:
        return False

#solicita al usuario un número entero y valida la entrada
def obtener_numero_entero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Debe ingresar valores enteros!!")

#muestra el menú de opciones al usuario
def mostrar_menu():
    print("*** MENU CONCESIONARIO AUTOUSADOS ***")
    print("1. Consultar inventario por marca.")
    print("2. Búsqueda por rango de precios.")
    print("3. Modificar precio de vehículo.")
    print("4. Salir del sistema.")

#controlador principal del programa
def programa_principal():
    while True:
        mostrar_menu()
        opcion = input("Ingrese opción: ")
        
        if opcion == "1":
            marca = input("Ingrese marca a consultar: ")
            inventario_marca(marca)
            
        elif opcion == "2":
            precio_min = obtener_numero_entero("Ingrese precio mínimo: ")
            precio_max = obtener_numero_entero("Ingrese precio máximo: ")
            busqueda_precio(precio_min, precio_max)
            
        elif opcion == "3":
            continuar = True
            while continuar: #permite actualizar múltiples precios
                codigo = input("Ingrese código del vehículo a actualizar: ")
                precio_nuevo = obtener_numero_entero("Ingrese precio nuevo: ")
                
                if actualizar_precio(codigo, precio_nuevo):
                    print("Precio actualizado exitosamente!!")
                else:
                    print("El código del vehículo no existe!!")
                
                respuesta = input("¿Desea actualizar otro precio (s/n)?: ")
                if respuesta.lower() != "s":
                    continuar = False
                    
        elif opcion == "4":
            print("Sistema finalizado correctamente.")
            break
            
        else:
            print("Debe seleccionar una opción válida!!")


#inicia el programa principal
programa_principal()