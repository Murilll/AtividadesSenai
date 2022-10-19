Qtd = int(input("Quantos nomes: "))
lista_nomes = []
lista_horas = []
lista_salario = []
hora = 8.80
inss = 0
for i in range(1, Qtd + 1):
    nome = input("Digite seu nome: ")
    lista_nomes.append(nome)

for k,j in enumerate (lista_nomes):
    horas = int(input(f"Digite as horas trabalhadas pelo {j}: "))
    esc = input("Fez horas extras?[s/n]: ").lower()
    if esc[0] == "s":
        horas_extras = float(input("Número de horas extras: "))
        horas += horas_extras*hora
        salario = horas*hora
    lista_horas.append(horas)
    salario.append(lista_salario)
    print(f"Horas Trabalhadas pelo {j}: {lista_horas[k]}")

for a,l in lista_nomes:
    if lista_salario[a] <= 2400:
        inss = 10
    elif lista_salario[a] > 2400:
        inss = 14
    print(f"Nome: {l}\nTrabalhou: {lista_horas[a]} HRS\nDesconto INSS: {inss}%\nSalário Bruto: {inss/100*lista_salario[a]}")