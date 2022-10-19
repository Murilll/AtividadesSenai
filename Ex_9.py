v = float(input("Digite 50 valores: "))
c = 1
ma = v
me = v
while c < 51:
    while True:
        try:
            v = float(input("Digite 50 valores: "))
        except:
            print("Inválido")
        break           
    if v > ma:
        ma = v
    if v < me:
        me = v
    c = c + 1
print(f"O maior valor é: {ma}")
print(f"O menor valor é: {me}")