nt = ("Digite o valor de n(Quantos números deverão ser lidos): ")
print(nt)
for x in nt:
    n = int(input("Digite o valor: "))
    if n == 0:
        print("Valor = 0 Fatorial = 1")
    else:
        aux = n
        fat = n 
        while aux != 1:
            fat = fat * (aux - 1)
            aux = aux - 1
    print("Valor =", n," Fatorial =", fat)