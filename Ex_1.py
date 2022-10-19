b = 0
cont = 0
while cont < 5:
    a = int(input("Digite um valor para 'a': "))
    print(a)
    if a <= 0:
        b += 1
    cont += 1
if b == 1:
    print("Dos 5 valores atribuidos para 'a', 1, é negativo")
else:
    print(f"Dos 5 valores atribuidos para 'a',{b}, são negativos")