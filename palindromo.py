def es_palindromo(texto):
    texto = texto.lower()
    limpio = ""
    for caracter in texto:
        if caracter != " ":
            limpio += caracter
    return limpio == limpio[::-1]

if __name__ == "__main__":
    entrada = input("Ingrese una frase: ")
    resultado = es_palindromo(entrada)
    if resultado:
        print("Es un palíndromo")
    else:
        print("No es palíndromo")
