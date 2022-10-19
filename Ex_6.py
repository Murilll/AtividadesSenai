print("Digite 5 pares (a,b) de números inteiros e positivos")
for x in range(5):
    while True:
        a = int(input(f"{x} par a: "))
        b = int(input("b: "))
        if (a>=0) and (b>=0):
            break
    for y in range(a,b):
        if y == a:
            print(f"Os números paress dentro do intervalo {a,b} são: ")
        if y %2 == 0:
            print(y)