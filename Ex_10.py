func = ["" for i in range(50)]
vHor = ["" for i in range(50)]
hNor = ["" for i in range(50)]
hExt = ["" for i in range(50)]
qtdF = 0
refF = 0
oper = 0
while oper != 3:
    if oper == 0:
        print("SENAI Funcontrol 1.0")
        print("-----")
        print("Escolha uma opção: ")
        print(" [1] Cadastrar horas de funcionário")
        print(" [2] Consultar holerite")
        print(" [3] Encerrar sistema")
        oper = int(input())
    elif oper == 1:
        qtdF = qtdF + 1
        refF = qtdF
        func[refF] = input("Nome do funcionário: ")
        vHor[refF] = int(input("Valor da hora normal: "))
        hNor[refF] =  int(input("Quantidade de horas normais: "))
        alt = input("Realizou horas extras? (S ou N): ")
        if alt == "S":
            hExt[refF] = int(input("Quantidade de horas extras: "))
            if hExt[refF] > 20:
                hExt[refF] = 20
                print("")
                print("Horas excedidas! Apenas 20h serão contabilizadas.")
            else:
                hExt[refF] = 0
            print("")
            print("Informações registradas com sucesso! ")
            print("")
            print("Escolha uma opção: ")
            print(" [1] Cadastrar horas de funcionário")
            print(" [2] Consultar holerite")
            print(" [3] Encerrar sistema")
            oper = int(input())
    elif oper == 2:
        print("SENAI Funcontrol 1.0")
        print("-----")
        print("Existem", qtdF, " funcionários registrados:")
        for count in range(1, qtdF + 1):
            print(count, " - ", func[count])
        print("")
        refF = int(input("Insira o código do funcionário para exibir seu holerite: "))
        tNor = hNor[refF] * vHor[refF]
        tExt = hExt[refF] * vHor[refF] * 1.5
        tVen = tNor + tExt
        
        if tVen > 7087.22:
            tInss = 992.21
            inss = 0.14
        else:
            if tVen > 3641.04:
                inss = 0.14
            else:
                if tVen > 2427.36:
                    inss = 0.12
                else:
                    if tVen > 1212.01:
                        inss = 0.09
                    else:
                        inss = 0.075
        tInss = inss * tVen
        
        if tVen > 4664.68:
            irpf = 0.275
        else:
            if tVen > 3751.06:
                irpf = 0.225
            else:
                if tVen > 2826.66:
                    irpf = 0.15
                else:
                    if tVen > 1903.99:
                        irpf = 0.075
                    else:
                        irpf <- 0
        tIrpf = irpf * tVen
        print("/------------------------------------------------\\")
        print("| HOLERITE MENSAL SENAI Funcontrol 1.0 |")
        print("|------------------------------------------------|")
        print("| Funcionário: ", func[refF], "(R$", vHor[refF], "/h) |")
        print("|------------------------------------------------|")
        print("| Descrição Ref Vencimentos Descontos |")
        print("| Salário base ", hNor[refF], "h ", tNor, " 0.00 |")
        print("| Horas extras ", hExt[refF], "h ", tExt, " 0.00 |")
        print("| INSS ", (inss*100), "% 0.00 ", tInss, " |")
        print("| IRPF ", (irpf*100), "% 0.00 ", tIrpf, " |")
        print("|------------------------------------------------|")
        print("| Totais: ", (tNor+tExt), " ", (tInss+tIrpf), " |")
        print("|------------------------------------------------|")
        print("| Salário líquido: R$", (tNor+tExt-tInss+tIrpf), " |")
        print("\------------------------------------------------/")
        print("Escolha uma opção: ")
        print(" [2] Consultar outro holerite")
        print(" [0] Menu principal")
        oper = int(input())
print("FIM")  