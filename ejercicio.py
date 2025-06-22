listaDeUsuarios = []

def ingresarUsuario(nombreUsuario, sexo, contraseña):
    if sexo != "M" and sexo != "F":
        print("Por favor, ingrese un valor correcto. F para femenino y M para masculino")
    else:
        contraseñaEsCorrecta = validarContraseña(contraseña)
        if contraseñaEsCorrecta:
            usuario = {
                nombreUsuario : {
                    "sexo" : sexo,
                    "contraseña" : contraseña
                }
            }
            usuarioExiste = validarUsuario(nombreUsuario)
            if usuarioExiste:
                print("El usuario ya existe")
            else:
                listaDeUsuarios.append(usuario)
        else: 
                print("La contraseña no cumple con los requisitos, intentalo de nuevo")
    return

def buscarUsuario(nombreUsuario):
    for usuario in listaDeUsuarios:
        if nombreUsuario in usuario:
            print("El usuario que buscas si existe")
            print("La contraseña de" , nombreUsuario, "es" , usuario[nombreUsuario]["contraseña"])
            print("El sexo de", nombreUsuario, "es", usuario[nombreUsuario]["sexo"])
            return
        
    print("El usuario no existe")

def eliminarUsuario(nombreUsuario):
    for usuario in listaDeUsuarios:
        if nombreUsuario in usuario:
            listaDeUsuarios.remove(usuario)
            return True
        
def validarContraseña(contraseña):
            if not isinstance(contraseña, str):
                return False
            if len(contraseña) < 8:
                print("La contraseña debe tener más de 8 caracteres")

            else:
                tieneLetras = False
                tieneNumeros = False
                tieneEspacios = False
                for caracter in contraseña:
                    if caracter.isalpha():
                        tieneLetras = True
                    elif caracter.isdigit():
                        tieneNumeros = True
                    elif caracter == " ":
                        tieneEspacios = True
                if tieneNumeros and tieneLetras and tieneEspacios == False:
                    return True
                elif tieneEspacios:
                    return False
        
def validarUsuario(nombreUsuario):
    for usuario in listaDeUsuarios:
        if nombreUsuario in usuario:
            print("El usuario", nombreUsuario, "si existe")
            return True
        return False
    
def iniciarPrograma():
    print("1. Ingresar usuario")
    print("2. Buscar usuario")
    print("3. Eliminar usuario")
    print("4. Salir")


    while True:
        try:
            opcionElegida = int(input("Ingrese la opción que desee: "))

            if opcionElegida == 1:
                while True:
                    nombre = input("Ingrese un nombre de usuario: ")
                    break
                
                while True:
                    sexo = input("Ingrese su sexo:  F para femenino / M para masculino: ")
                    break

                while True:
                    contraseña = input("Ingrese la contraseña del usuario: ")
                    ingresarUsuario(nombre, sexo, contraseña)
                    iniciarPrograma()
            elif opcionElegida == 2:
                nombre = input("Ingrese el nombre del usuario que desea buscar: ")
                buscarUsuario(nombre)
                iniciarPrograma()
            elif opcionElegida == 3:
                nombre = input("Ingrese el nombre del usuario que desea eliminar: ")
                print("¡Usuario eliminado existosamente!")
                eliminarUsuario(nombre)
                iniciarPrograma()
            elif opcionElegida == 4:
                break
        except ValueError:
            print("ERROR")

iniciarPrograma()