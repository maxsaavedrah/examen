def contar_leds(numero):
    # Cantidad de LEDs para cada dígito
    leds_por_digito = {
        '0': 6, '1': 2, '2': 5, '3': 5, '4': 4,
        '5': 5, '6': 6, '7': 3, '8': 7, '9': 6
    }
    
    total_leds = 0
    for digito in str(numero):
        total_leds += leds_por_digito[digito]
    
    return total_leds

# Bloque principal
numero = input("Ingresa un número: ")
cantidad_leds = contar_leds(numero)
print(f"El número {numero} utiliza {cantidad_leds} LEDs.")
