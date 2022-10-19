for i in range(int(input("Quantos produtos? "))):
    valor1 = int(input("Digite um valor para esse produto: "))
    valor2 = int(input("Digite outro valor para esse produto: "))
    media = (valor1 + valor2) /2
    situacao = "CARO" if media > min([valor1, valor2]) * 1.5 else "BARATO"
    print(f"Produto {i + 1} Valor 1 = {valor1}, Valor 2 = {valor2} MÉDIA = {media} Situação {situacao}")