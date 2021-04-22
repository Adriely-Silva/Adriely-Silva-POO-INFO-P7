def se_e_triangulo(canudo1, canudo2, canudo3):
    if canudo1 <=0 or canudo2 <= 0 or canudo3 <= 0:
        return False
    if canudo1 == canudo2 and canudo2 == canudo3:
        return True
    if canudo1 >= canudo2 and canudo1 >= canudo3:
        return  canudo1 < canudo2 + canudo3
    if canudo2 >= canudo1 and canudo2 >= canudo3:
        return canudo2 < canudo1 + canudo3
    if canudo3 >= canudo1 and canudo3 >= canudo2:
        return  canudo3 < canudo1 + canudo2


canudo1 = input(" Digite o primeiro comprimento: ")
canudo2 = input(" Digite o segundo comprimento: ")
canudo3 = input(" Digite o terceiro comprimento: ")

valor = se_e_triangulo(int(canudo1), int(canudo2), int(canudo3))
print(valor)




    

    