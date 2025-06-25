# Ayuditassss

listaDeUsuarios = [] 
# Función para buscar un usuario por su nombre
def buscarUsuario(nombreUsuario):

    for usuario in listaDeUsuarios:
        # Si el nombre se encuentra en el diccionario, entonces nos muestran los datos de el usuario
        if nombreUsuario in usuario:
            print("El usuario que buscas sí existe")
            print("La contraseña de" , nombreUsuario, "es" , usuario[nombreUsuario]["contraseña"])
            print("El sexo de", nombreUsuario, "es", usuario[nombreUsuario]["sexo"])
            return
        

# Función para validar que la contraseña cumpla los requisitos
def validarContraseña(contraseña):
    # Acá no estoy seguro de esta funcion, pero la puse como alternativa para que el
    # isalpha y isdigit funcionen correctamente
    if not isinstance(contraseña, str):
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