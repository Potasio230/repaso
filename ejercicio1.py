# Lista donde se guardarán todos los usuarios registrados
listaDeUsuarios = []

# Función para ingresar un nuevo usuario
def ingresarUsuario(nombreUsuario, sexo, contraseña):
    while True:
        try:
            # Validamos que el sexo ingresado sea M o F
            if sexo != "M" and sexo != "F":
                print("Por favor, ingrese un valor correcto. F para femenino y M para masculino")
            else:
                # Validamos la contraseña con una función aparte
                contraseñaEsCorrecta = validarContraseña(contraseña)
                if contraseñaEsCorrecta:
                    # Creamos un diccionario con los datos del usuario
                    usuario = {
                        nombreUsuario : {
                            "sexo" : sexo,
                            "contraseña" : contraseña
                        }
                    }
                    # Verificamos si el usuario ya existe
                    usuarioExiste = validarUsuario(nombreUsuario)
                    if usuarioExiste:
                        print("El usuario ya existe")
                        print("Presiona Enter para continuar")
                        input()
                    else:
                        # Si no existe, lo agregamos a la lista
                        listaDeUsuarios.append(usuario)
                        print("Usuario ingresado correctamente")
                        print("Presiona Enter para continuar")
                        input()
                else: 
                    print("La contraseña no cumple con los requisitos, intentalo de nuevo")
                    print("Presiona Enter para continuar")
                    input()
                    
            return
        except ValueError:
            print("ERROR: Ingrese un valor correcto")

# Función para buscar un usuario por su nombre
def buscarUsuario(nombreUsuario):
    for usuario in listaDeUsuarios:
        # Si el nombre se encuentra en el diccionario, entonces nos muestran los datos de el usuario
        if nombreUsuario in usuario:
            print("El usuario que buscas sí existe")
            print("La contraseña de" , nombreUsuario, "es" , usuario[nombreUsuario]["contraseña"])
            print("El sexo de", nombreUsuario, "es", usuario[nombreUsuario]["sexo"])
            return

    print("El usuario no existe")
    print("Presiona Enter para continuar")
    input()

# Función para eliminar un usuario
def eliminarUsuario(nombreUsuario):
    for usuario in listaDeUsuarios:
        if nombreUsuario in usuario:
            # Se elimina el usuario de la lista
            listaDeUsuarios.remove(usuario)
            return True

# Función para validar que la contraseña cumpla los requisitos
def validarContraseña(contraseña):
    if not isinstance(contraseña, str):
        print("La contraseña debe ser solo texto")
        return False
    if len(contraseña) < 8:
        print("La contraseña debe tener más de 8 caracteres")

    else:
        tieneLetras = False
        tieneNumeros = False
        tieneEspacios = False
        # Recorremos cada carácter de la contraseña
        for caracter in contraseña:
            if caracter.isalpha():  # Letras
                tieneLetras = True
            elif caracter.isdigit():  # Números
                tieneNumeros = True
            elif caracter == " ":  # Espacios
                tieneEspacios = True
        # Retorna True si tiene letras, números y sin espacios
        if tieneNumeros and tieneLetras and tieneEspacios == False:
            return True
        elif tieneEspacios:
            return False

# Función para verificar si el usuario ya existe
def validarUsuario(nombreUsuario):
    for usuario in listaDeUsuarios:
        if nombreUsuario in usuario:
            print("El usuario", nombreUsuario, "sí existe")
            return True
    return False  # Esta línea debe ir fuera del for

# Función principal que muestra el menú y ejecuta opciones

def mostrarMenu():
    print("1. Ingresar usuario")
    print("2. Buscar usuario")
    print("3. Eliminar usuario")
    print("4. Salir")

def iniciarPrograma():
    mostrarMenu()

    while True:
        try:
            opcionElegida = int(input("Ingrese la opción que desee: "))

            if opcionElegida == 1:
                # Datos para nuevo usuario
                nombre = input("Ingrese un nombre de usuario: ")
                sexo = input("Ingrese su sexo:  F para femenino / M para masculino: ")
                contraseña = input("Ingrese la contraseña del usuario: ")
                ingresarUsuario(nombre, sexo, contraseña)
                mostrarMenu()

            elif opcionElegida == 2:
                # Buscar un usuario existente
                nombre = input("Ingrese el nombre del usuario que desea buscar: ")
                buscarUsuario(nombre)
                mostrarMenu()

            elif opcionElegida == 3:
                # Eliminar un usuario
                nombre = input("Ingrese el nombre del usuario que desea eliminar: ")
                print("¡Usuario eliminado exitosamente!")
                eliminarUsuario(nombre)
                mostrarMenu()

            elif opcionElegida == 4:
                    print("Saliendo del programa...")
                    break
            
            else:
                print("ERROR: Seleccione una opción válida")
                mostrarMenu()

        except ValueError:
            print("ERROR: Selecione un numero válido")  # Si el usuario no ingresa un número válido
            mostrarMenu()
# Inicia el programa al ejecutar el archivo
iniciarPrograma()
