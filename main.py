import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from zoneinfo import ZoneInfo
from time import sleep

while True:

    def lagrange(x, y, t):
        n = len(x)
        total = 0.0
        for i in range(n):
            Li = 1.0
            for j in range(n):
                if i != j:
                    Li *= (t - x[j]) / (x[i] - x[j])
            total += y[i] * Li
        return total

    x = np.array([0, 3, 6, 9, 12, 15, 18, 21], float)

    try:
        print("\nEscolha uma cidade:")
        print("1 - São Paulo")
        print("2 - Nova York")
        print("3 - Lisboa")
        print("4 - Tóquio")
        print("5 - Recife")

        op = int(input("Digite a opção: "))
        flag = 0

        match op:
            case 1:
                zona = "America/Sao_Paulo"
                nome_cidade = "São Paulo"
                y = np.array([19, 18, 17, 21, 26, 27, 24, 21], float)

                try:
                    print("\nDeseja ver o gráfico?")
                    print("1 - Sim.")
                    print("2 - Não.")
                    op = int(input("Digite aqui: "))

                    if op == 1:
                        t_values = np.linspace(min(x), max(x), 300)
                        p_values = [lagrange(x, y, t) for t in t_values]

                        plt.plot(t_values, p_values, label='Polinômio de Lagrange', color='blue')
                        plt.scatter(x, y, color='red', label='Pontos dados')
                        plt.title('Interpolação de Lagrange')
                        plt.xlabel('x')
                        plt.ylabel('y')
                        plt.legend()
                        plt.grid(True)
                        plt.show()
                    elif op == 2:
                        print("Tudo bem!")
                    else:
                        print("\nOps...opção invalida!\n")
                except ValueError:
                    print("\nEntrada inválida. Digite uma opção válido.\n")
                    break
                flag = 1
            case 2:
                zona = "America/New_York"
                nome_cidade = "Nova York"
                y = np.array([13, 11, 10, 14, 19, 21, 18, 15], float)

                try:
                    print("\nDeseja ver o gráfico?")
                    print("1 - Sim.")
                    print("2 - Não.")
                    op = int(input("Digite aqui: "))

                    if op == 1:
                        t = np.linspace(min(x), max(x), 200)
                        p = [lagrange(x, y, ti) for ti in t]

                        plt.plot(x, y, 'ro', label='Pontos dados')
                        plt.plot(t, p, 'b-', label='Interpolação de Lagrange')
                        plt.title('Interpolação Polinomial de Lagrange')
                        plt.xlabel('x')
                        plt.ylabel('y')
                        plt.legend()
                        plt.grid(True)
                        plt.show()
                    elif op == 2:
                        print("Tudo bem!")
                    else:
                        print("\nOps...opção invalida!\n")
                except ValueError:
                    print("\nEntrada inválida. Digite uma opção válido.\n")
                    break
                flag = 1
            case 3:
                zona = "Europe/Lisbon"
                nome_cidade = "Lisboa"
                y = np.array([15, 13, 12, 17, 22, 23, 20, 17], float)

                try:
                    print("\nDeseja ver o gráfico?")
                    print("1 - Sim.")
                    print("2 - Não.")
                    op = int(input("Digite aqui: "))

                    if op == 1:
                        t = np.linspace(min(x), max(x), 300)
                        p = [lagrange(x, y, ti) for ti in t]

                        plt.plot(t, p, 'b-', label='Interpolação de Lagrange')
                        plt.scatter(x, y, color='red', label='Pontos dados')
                        plt.title('Polinômio Interpolador de Lagrange')
                        plt.xlabel('x')
                        plt.ylabel('y')
                        plt.legend()
                        plt.grid(True)
                        plt.show()
                    elif op == 2:
                        print("Tudo bem!")
                    else:
                        print("\nOps...opção invalida!\n")
                except ValueError:
                    print("\nEntrada inválida. Digite uma opção válido.\n")
                    break
                flag = 1
            case 4:
                zona = "Asia/Tokyo"
                nome_cidade = "Tóquio"
                y = np.array([20, 19, 18, 22, 27, 28, 25, 22], float)

                try:
                    print("\nDeseja ver o gráfico?")
                    print("1 - Sim.")
                    print("2 - Não.")
                    op = int(input("Digite aqui: "))

                    if op == 1:
                        t = np.linspace(min(x), max(x), 300)
                        p = [lagrange(x, y, ti) for ti in t]

                        plt.plot(x, y, 'o', label='Pontos dados', color='red')
                        plt.plot(t, p, label='Polinômio de Lagrange', color='blue')
                        plt.xlabel('x')
                        plt.ylabel('y')
                        plt.title('Interpolação Polinomial de Lagrange')
                        plt.legend()
                        plt.grid(True)
                        plt.show()
                    elif op == 2:
                        print("Tudo bem!")
                    else:
                        print("\nOps...opção invalida!\n")
                except ValueError:
                    print("\nEntrada inválida. Digite uma opção válido.\n")
                    break
                flag = 1
            case 5:
                zona = "America/Recife"
                nome_cidade = "Recife"
                y = np.array([24, 23, 24, 28, 31, 32, 29, 26], float)

                try:
                    print("\nDeseja ver o gráfico?")
                    print("1 - Sim.")
                    print("2 - Não.")
                    op = int(input("Digite aqui: "))

                    if op == 1:
                        t = np.linspace(min(x), max(x), 200)
                        p = [lagrange(x, y, ti) for ti in t]

                        plt.figure(figsize=(8, 5))
                        plt.plot(x, y, 'ro', label='Pontos conhecidos')
                        plt.plot(t, p, 'b-', label='Interpolação de Lagrange')
                        plt.xlabel('x')
                        plt.ylabel('y')
                        plt.title('Interpolação de Lagrange')
                        plt.legend()
                        plt.grid(True)
                        plt.show()
                    elif op == 2:
                        print("Tudo bem!")
                    else:
                        print("\nOps...opção invalida!\n")
                except ValueError:
                    print("\nEntrada inválida. Digite uma opção válido.\n")
                    break
                flag = 1
            case _:
                print("\nEntrada inválida. Digite uma opção válido.\n")
                while True:
                    try:
                        print("Deseja tentar novamente?")
                        print("1 - Sim.")
                        print("2 - Não.")
                        verificar = int(input("Digite aqui: "))

                        if verificar == 1:
                            flag = 0
                            break
                        elif verificar == 2:
                            print("FIQUE BEM", end="")
                            for i in range(3):
                                sleep(0.7)
                                print(".", end="")
                            print()
                            sleep(0.21)
                            exit()
                        else:
                            print("\nOps...opção invalida!\n")
                    except ValueError:
                        print("\nEntrada inválida. Digite uma opção válido.\n")

        if flag == 1:
            cidade = ZoneInfo(zona)
            agora = datetime.now(cidade)
            hora_decimal = agora.hour + agora.minute / 60 + agora.second / 3600

            temp_interp = lagrange(x, y, hora_decimal)

            print("CARREGANDO TABELA DE TEMPERATURA", end="")
            for i in range(3):
                sleep(0.7)
                print(".", end="")
            print()
            sleep(0.21)

            print("\n--- TABELA DE TEMPERATURAS ---")
            print(f"Cidade: {nome_cidade}")
            print("-------------------------------")
            print(f"{'Hora (h)':<10} {'Temperatura (°C)':<20}")
            print("-------------------------------")
            for i in range(len(x)):
                print(f"{x[i]:<10.0f} {y[i]:<20.1f}")
            print("-------------------------------")
            
            while True:
                try:
                    print("\nDeseja ver a temperatura ás", agora.strftime("%H:%M:%S"))
                    print("1 - Sim.")
                    print("2 - Não.")
                    verificar = int(input("Digite aqui: "))

                    if verificar == 1:
                        print("CARREGANDO RESULTADO", end="")
                        for _ in range(3):
                            sleep(0.7)
                            print(".", end="")
                        print()
                        sleep(0.21)
                        print("\n--- RESULTADO ---")
                        print("Horário atual:", agora.strftime("%H:%M:%S"))
                        print(f"Hora decimal: {hora_decimal:.4f}")
                        print(f"Temperatura interpolada (Lagrange): {temp_interp:.2f} °C")
                        
                        print("\nDeseja fazer uma nova consulta?")
                        print("1 - Sim.")
                        print("2 - Não.")
                        verificar = int(input("Digite aqui: "))

                        try:
                            if verificar == 1:
                                break
                            elif verificar == 2:
                                print("FIQUE BEM", end="")
                                for i in range(3):
                                    sleep(0.7)
                                    print(".", end="")
                                print()
                                sleep(0.21)
                                exit()
                            else:
                                print("\nOps...opção invalida!\n")
                        except ValueError:
                            print("\nEntrada inválida. Digite uma opção válido.\n")
                            
                    elif verificar == 2:
                        print("FIQUE BEM", end="")
                        for i in range(3):
                            sleep(0.7)
                            print(".", end="")
                        print()
                        sleep(0.21)
                        exit()
                        
                    else:
                        print("\nOps...opção invalida!\n")
    
                except ValueError:
                    print("\nEntrada inválida. Digite uma opção válida.\n")
    except ValueError:
        print("\nEntrada inválida. Digite uma opção válido.\n")