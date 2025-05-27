"""
Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.

Para converter temperaturas entre Celsius (C), Fahrenheit (F) e Kelvin (K), utilize as seguintes fórmulas: 
C para F: F = (C * 9/5) + 32
F para C: C = (F - 32) / 9/5
C para K: K = C + 273.15
K para C: C = K - 273.15
F para K: K = (F - 32) / 9/5 + 273.15
K para F: F = (K - 273.15) * 9/5 + 32
"""

temp = float(input("Digite a temperatura: "))
origem = input("Digite a unidade de origem (C, F ou K): ").upper()
destino = input("Digite a unidade de destino (C, F ou K): ").upper()

if origem == destino:
    resultado = temp
elif origem == "C":
    if destino == "F":
        resultado = (temp * 9/5) + 32
    else:
        resultado = temp + 273.15
elif origem == "F":
    if destino == "C":
        resultado = (temp - 32) / 9/5
    else:
        resultado = (temp - 32) / 9/5 + 273.15 
else:
    if destino == "C":
        resultado = temp - 273.15
    else:
        resultado = (temp - 273.15) * 9/5 + 32              



print (f"A temperatura {temp} {origem} é igual a {resultado:.2f} {destino}")