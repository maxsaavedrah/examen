def invertir_numero(numero):
    invertido = 0
    while numero > 0:
        digito = numero % 10  
        invertido = invertido * 10 + digito  
        numero //= 10  
    return invertido


def es_numero_perfecto(numero):
    invertido = invertir_numero(numero)
    return numero == invertido  # Retorna True si es perfecto, False si no


# Bloque principal
numero = int(input("Ingresa un número: "))
if es_numero_perfecto(numero):
    print(f"{numero} es un número perfecto.")
else:
    print(f"{numero} no es un número perfecto.")
