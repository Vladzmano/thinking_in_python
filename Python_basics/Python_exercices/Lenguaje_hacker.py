def leet_speak(text):
    leet_table = {
        'a': '4',
        'b': '8',
        'e': '3',
        'g': '6',
        'l': '1',
        'o': '0',
        's': '5',
        't': '7',
        'z': '2'
    }

    leet_text = ''
    for char in text:
        if char.lower() in leet_table:
            leet_char = leet_table[char.lower()]
            leet_text += leet_char
        else:
            leet_text += char

    return leet_text

# Ejemplo de uso
texto = input("Ingresa un texto: ")
texto_en_leet = leet_speak(texto)
print("Texto en 'lenguaje hacker':", texto_en_leet)