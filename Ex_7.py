medsal = 0
tpessoa = 0
percpessoa = 0
sal = 1
msal = 9999
medf = 0
while sal > 0:
    sal = float(input("Digite o salário: "))
    medsal = medsal + sal
    if sal > msal:
        msal = sal
    if sal <= 100:
        percpessoa = percpessoa + 1 
    f = int(input("Digite o número de filhos: "))
    medf = medf + f
    tpessoa = tpessoa + 1
    break
print(f"A média do salário da população é: {medsal/tpessoa}")
print(f"A média do número de filhos é: {medf/tpessoa}")
print(f"O maior salário é: {msal}")
print(f"O percentual de pessoas com salário até R$100,00 é: {percpessoa*100/tpessoa}%")