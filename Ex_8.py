print("Digite 20 vezes o valor de N")
for x in range(1, 20):
    n = int(input(f"{x} Valor: "))
    if n == 0:
        print("0 x 0 = 0")
    for y in range(1, n):
        print(f"{y} x {n} = {y*n}")
    print(" ")