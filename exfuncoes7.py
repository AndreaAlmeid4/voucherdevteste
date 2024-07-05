#calculo de salario e hora extra ##

def calcular_salario(ht):
    valor_horaextra = 75
    qtde_horaextra = 0
    if ht > 160:
        qtde_horaextra = ht - 160

    salario = (55 * ht) + (valor_horaextra * qtde_horaextra)
    print("QUANTIDADE DE HORAS EXTRAS: ",qtde_horaextra)
    print("SALARIO NORMAL: ",55 * ht)
    print("SALARIO HORA EXTRA: ",valor_horaextra * qtde_horaextra)
    print("SALARIO BRUTO: ",salario)



pedro = calcular_salario(181)
