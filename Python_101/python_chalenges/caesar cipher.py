# caesar cipher

def cifrado_cesar(texto, desplazamiento):
    texto_cifrado = ''
    
    for caracter in texto:
        if caracter.isalpha():  # Solo se cifran las letras del alfabeto
            codigo = ord(caracter) + desplazamiento  # Obtener el código ASCII del caracter y sumar el desplazamiento
            if caracter.isupper():  # Si es una letra mayúscula
                limite = ord('Z')
            else:  # Si es una letra minúscula
                limite = ord('z')
            
            if codigo > limite:  # Si el código excede el límite, volver al inicio del alfabeto
                codigo = codigo - 26
            
            caracter_cifrado = chr(codigo)  # Obtener el caracter cifrado a partir del código ASCII
        else:
            caracter_cifrado = caracter  # Mantener los caracteres no alfabéticos sin cambios
        
        texto_cifrado += caracter_cifrado  # Agregar el caracter cifrado al texto resultante
    
    return texto_cifrado


texto_original = "Hola mi osa, este es un ejemplo de Cifrado Cesar!"
desplazamiento = 3

texto_cifrado = cifrado_cesar(texto_original, desplazamiento)
print("Texto cifrado:", texto_cifrado)

texto_descifrado = cifrado_cesar(texto_cifrado, -desplazamiento)  # Para descifrar, se utiliza el desplazamiento negativo
print("Texto descifrado:", texto_descifrado)
