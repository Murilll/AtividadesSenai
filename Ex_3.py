c = 0
n = 0
while n != 0:
    n = int(input("Digite um valor (0 p/ encerrar a entrada de dadod): "))
    if (c == 0) or (c == 20):
        print("Valor Valor**2 Valor**3 Raiz Quadrada")
        c = 1
    rn = (n**0.5)
    print(f"{n},{n*2},{n*3},{rn}")