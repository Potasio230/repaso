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

def inventarioMarca(marca):
    totalStock = 0
    marcaBuscada = marca.lower()

    for codigo, datos in vehiculos.items():
        marcaVehiculo = datos[0].lower()
        if marcaVehiculo == marcaBuscada:
            if codigo in inventario:
                stockVehiculo = inventario[codigo][1]
                if stockVehiculo > 0:
                    totalStock = totalStock + stockVehiculo
    print(f"El inventario de {marca} es: {totalStock}")


def busquedaPrecio(precioMin, precioMax):
    vehiculosEncontrados = []

    for codigo, datosInventario in inventario.items():
        precio = datosInventario[0]
        stock = datosInventario[1]

        if precioMin <= precio <= precioMax and stock > 0:
            if codigo in vehiculos:
                marca = vehiculos[codigo][0]
                formatoResultado = f"{marca}---{codigo}"
                vehiculosEncontrados.append(formatoResultado)

    vehiculosEncontrados.sort()

    if len(vehiculosEncontrados) > 0:
        print(f"Los vehiculos en el rango de precios consultados son: {vehiculosEncontrados}")
    else:
        print("No hay vehículos en ese rango de precios.")

def actualizarPrecio(codigo, precioNuevo):
    if codigo in inventario:
        inventario[codigo][0] = precioNuevo
        return True
    else:
        return False
    
def obtenerNumeroEntero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("¡¡¡Debes ingresar numeros enteros!!!")

def mostrarMenu():
    print("*** MENU CONCESIONARIO AUTOUSADOS ***")
    print("1. Consultar inventario por marca.")
    print("2. Búsqueda por rango de precios.")
    print("3. Modificar precio de vehículo.")
    print("4. Salir del sistema.")

def programaPrincipal():
    while True:
        mostrarMenu()
        opcion = input("Seleccione una opción: ")

        if opcion == 1:
            marca = input("Ingrese la marca del vehículo: ")
            inventarioMarca(marca)

        elif opcion == 2:
            precioMin = obtenerNumeroEntero("Ingrese el precio mínimo: ")
            precioMax = obtenerNumeroEntero("Ingrese el precio máximo: ")
            busquedaPrecio(precioMin, precioMax)

        elif opcion == 3:
            continuar = True
            while continuar:
                codigo = input("Ingrese el código del vehículo a actualizar: ")
                precioNuevo = obtenerNumeroEntero("Ingrese el precio nuevo: ")

                if actualizarPrecio(codigo, precioNuevo):
                    print("¡¡¡Precio actualizado exitosamente!!!")
                else:
                    print("¡¡¡El código del vehículo no existe!!!")

                respuesta = input("¿Desea actualizar otro vehículo? (s/n): ")
                if respuesta.lower() != "s":
                    continuar = False

        elif opcion == 4:
            print("Saliendo del sistema...")
            break
        else:
            print("¡¡¡Debe seleccionar una opción válida!!!")


programaPrincipal()

