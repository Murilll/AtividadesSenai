di = 0
fi = 0
print("Digite 10 valores")
for x in range(10):
    v = float(input(f"{x}, Valor: "))
    if (v >= 10) and (v <= 20):
        di = di + 1
    else:
        fi = fi + 1
print("Dos 10 valores digitados")
print(f"{di} estão dentro do intervalo de 10 e 20")
print(f"E {fi} não estão nesse intervalor")