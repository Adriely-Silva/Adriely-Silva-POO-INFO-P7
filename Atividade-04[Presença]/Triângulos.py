lado1 = input(" Digite o primeiro lado do triângulo: ")
lado2 = input(" Digite o segundo lado do triângulo: ")
lado3 = input(" Digite o terceiro lado do triângulo: ")


if lado1 == lado2 and lado2 == lado3:
    print(" O triângulo é equilátero! ")
elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
    print(" O triângulo é escaleno! ")
else:
    print(" O triângulo é isósceles! ")
