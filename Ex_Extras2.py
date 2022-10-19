times = [
    [
        {
            "idade": int(input("Idade: ")),
            "peso": float(input("Peso: ")),
            "altura": float(input("Altura: "))
        } for jogador in range(2)
    ] for time in range(2)
]

menosDe18 = 0
mediaDeIdades = []
mediaDeAltura = 0
quantJogadores = 0
maisDe80kg = 0

for time in times:
    mediaDeIdadesTime = 0
    for jogador in time:
        if jogador["idade"] < 18:
            menosDe18 += 1
        if jogador["peso"] > 80:
            maisDe80kg += 1
        mediaDeIdadesTime += jogador["idade"]
        mediaDeAltura += jogador["altura"]
    mediaDeIdadesTime /= len(time)
    mediaDeIdades.append(mediaDeIdadesTime)
    quantJogadores += len(time)
mediaDeAltura /= quantJogadores
maisDe80kg = (maisDe80kg * 100) / quantJogadores
print(f"A quantidade de jogadores com idades inferior a 18 anos: {menosDe18}")
print(f"A média as idades dos jogadores de cada time: {mediaDeIdades}")
print(f"A média das alturas de todos os jogadores do compeonato: {mediaDeAltura}")
print(f"A porcentagem de jogadores com mais de 80 quilosgramas entre todos os jogadores do compeonato: {maisDe80kg}")