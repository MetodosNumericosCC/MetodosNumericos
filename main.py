import sys
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from zoneinfo import ZoneInfo
from time import sleep

tipo = 0
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

    def divided_differences(x, y):

        n = len(x)
        coef = y.copy().astype(float)
        for j in range(1, n):
            for i in range(n - 1, j - 1, -1):
                coef[i] = (coef[i] - coef[i - 1]) / (x[i] - x[i - j])
        return coef


    def newton_eval(t, x_points, coef):

        n = len(coef)
        result = coef[-1]
        for k in range(n - 2, -1, -1):
            result = coef[k] + (t - x_points[k]) * result
        return result

    x = np.array([0, 3, 6, 9, 12, 15, 18, 21], float)

    while True:
        flag = 0
        try:
            print("\nESCOLHA O MÉTODO DE INTERPOLAÇÃO:")
            print("1 - LAGRANGE")
            print("2 - NEWTON (DIFERENÇAS DIVIDIDAS)")
            metodo_op = int(input("DIGITE UMA OPÇÃO: "))

            if metodo_op == 1:
               flag = 1
            elif metodo_op == 2:
                flag = 2
            else:
                print("\nOPS...OPÇÃO INVÁLIDA!")
                break
        except ValueError:
            print("\nENTRADA INVÁLIDA. DIGITE UMA OPÇÃO VÁLIDA.")
            break

        try:
            try:
                if flag == 1:
                    print("\nESCOLHA UMA CIDADE:")
                    print("1 - SÃO PAULO")
                    print("2 - NOVA YORK")
                    print("3 - LISBOA")
                    print("4 - TÓQUIO")
                    print("5 - RECIFE")

                    op = int(input("DIGITE UMA OPÇÃO: "))
                    flag = 0

                    match op:
                        case 1:
                            zona = "America/Sao_Paulo"
                            nome_cidade = "São Paulo"
                            y = np.array([19, 18, 17, 21, 26, 27, 24, 21], float)
                            tipo = 1

                            try:
                                print("\nDESEJA VER A TABELA?")
                                print("1 - SIM.")
                                print("2 - NÃO.")
                                op = int(input("DIGITE AQUI: "))

                                if op == 1:
                                    print("\nCARREGANDO TABELA DE TEMPERATURA", end="")
                                    for i in range(3):
                                        sleep(0.7)
                                        print(".", end="")
                                    print()
                                    sleep(0.21)

                                    print("\n--- TABELA DE TEMPERATURAS ---")
                                    print(f"CIDADE: {nome_cidade.upper()}")
                                    print("-------------------------------")
                                    print(f"{'HORA (H)':<10} {'TEMPERATURA (°C)':<20}")
                                    print("-------------------------------")
                                    for i in range(len(x)):
                                        print(f"{x[i]:<20.1f} {y[i]:<20.1f}")
                                    print("-------------------------------")
                                    flag = 1
                                elif op == 2:
                                    flag = 1
                                    print("\nTUDO BEM!")
                                else:
                                    print("\nOPS...OPÇÃO INVÁLIDA!\n")
                                    while True:
                                        try:
                                            print("DESEJA TENTAR NOVAMENTE?")
                                            print("1 - SIM.")
                                            print("2 - NÃO.")
                                            verificar = int(input("DIGITE AQUI: "))

                                            if verificar == 1:
                                                tipo = 0
                                                break
                                            elif verificar == 2:
                                                print("FIQUE BEM", end="")
                                                for i in range(3):
                                                    sleep(0.7)
                                                    print(".", end="")
                                                print()
                                                sleep(0.21)
                                                sys.exit()
                                            else:
                                                print("\nOPS...OPÇÃO INVÁLIDA!\n")
                                        except ValueError:
                                            print("\nENTRADA INVÁLIDA. DIGITE UMA OPÇÃO VÁLIDA.")

                            except ValueError:
                                print("\nENTRADA INVÁLIDA. DIGITE UMA OPÇÃO VÁLIDA.\n")
                        case 2:
                            zona = "America/New_York"
                            nome_cidade = "Nova York"
                            y = np.array([13, 11, 10, 14, 19, 21, 18, 15], float)
                            tipo = 2

                            try:
                                print("\nDESEJA VER A TABELA?")
                                print("1 - SIM.")
                                print("2 - NÃO.")
                                op = int(input("DIGITE AQUI: "))

                                if op == 1:
                                    print("\nCARREGANDO TABELA DE TEMPERATURA", end="")
                                    for i in range(3):
                                        sleep(0.7)
                                        print(".", end="")
                                    print()
                                    sleep(0.21)

                                    print("\n--- TABELA DE TEMPERATURAS ---")
                                    print(f"CIDADE: {nome_cidade.upper()}")
                                    print("-------------------------------")
                                    print(f"{'HORA (H)':<10} {'TEMPERATURA (°C)':<20}")
                                    print("-------------------------------")
                                    for i in range(len(x)):
                                        print(f"{x[i]:<20.1f} {y[i]:<20.1f}")
                                    print("-------------------------------")
                                    flag = 1
                                elif op == 2:
                                    flag = 1
                                    print("\nTUDO BEM!")
                                else:
                                    print("\nOPS...OPÇÃO INVÁLIDA!\n")
                                    while True:
                                        try:
                                            print("DESEJA TENTAR NOVAMENTE?")
                                            print("1 - SIM.")
                                            print("2 - NÃO.")
                                            verificar = int(input("DIGITE AQUI: "))

                                            if verificar == 1:
                                                tipo = 0
                                                break
                                            elif verificar == 2:
                                                print("FIQUE BEM", end="")
                                                for i in range(3):
                                                    sleep(0.7)
                                                    print(".", end="")
                                                print()
                                                sleep(0.21)
                                                sys.exit()
                                            else:
                                                print("\nOPS...OPÇÃO INVÁLIDA!\n")
                                        except ValueError:
                                            print("\nENTRADA INVÁLIDA. DIGITE UMA OPÇÃO VÁLIDA.\n")

                            except ValueError:
                                print("\nENTRADA INVÁLIDA. DIGITE UMA OPÇÃO VÁLIDA.\n")
                        case 3:
                            zona = "Europe/Lisbon"
                            nome_cidade = "Lisboa"
                            y = np.array([15, 13, 12, 17, 22, 23, 20, 17], float)
                            tipo = 3

                            try:
                                print("\nDESEJA VER A TABELA?")
                                print("1 - SIM.")
                                print("2 - NÃO.")
                                op = int(input("DIGITE AQUI: "))

                                if op == 1:
                                    print("\nCARREGANDO TABELA DE TEMPERATURA", end="")
                                    for i in range(3):
                                        sleep(0.7)
                                        print(".", end="")
                                    print()
                                    sleep(0.21)

                                    print("\n--- TABELA DE TEMPERATURAS ---")
                                    print(f"CIDADE: {nome_cidade.upper()}")
                                    print("-------------------------------")
                                    print(f"{'HORA (H)':<10} {'TEMPERATURA (°C)':<20}")
                                    print("-------------------------------")
                                    for i in range(len(x)):
                                        print(f"{x[i]:<20.1f} {y[i]:<20.1f}")
                                    print("-------------------------------")
                                    flag = 1
                                elif op == 2:
                                    flag = 1
                                    print("\nTUDO BEM!")
                                else:
                                    print("\nOPS...OPÇÃO INVÁLIDA!\n")
                                    while True:
                                        try:
                                            print("DESEJA TENTAR NOVAMENTE?")
                                            print("1 - SIM.")
                                            print("2 - NÃO.")
                                            verificar = int(input("DIGITE AQUI: "))

                                            if verificar == 1:
                                                tipo = 0
                                                break
                                            elif verificar == 2:
                                                print("FIQUE BEM", end="")
                                                for i in range(3):
                                                    sleep(0.7)
                                                    print(".", end="")
                                                print()
                                                sleep(0.21)
                                                sys.exit()
                                            else:
                                                print("\nOPS...OPÇÃO INVÁLIDA!\n")
                                        except ValueError:
                                            print("\nENTRADA INVÁLIDA. DIGITE UMA OPÇÃO VÁLIDA.\n")

                            except ValueError:
                                print("\nENTRADA INVÁLIDA. DIGITE UMA OPÇÃO VÁLIDA.\n")
                        case 4:
                            zona = "Asia/Tokyo"
                            nome_cidade = "Tóquio"
                            y = np.array([20, 19, 18, 22, 27, 28, 25, 22], float)
                            tipo = 4

                            try:
                                print("\nDESEJA VER A TABELA?")
                                print("1 - SIM.")
                                print("2 - NÃO.")
                                op = int(input("DIGITE AQUI: "))

                                if op == 1:
                                    print("\nCARREGANDO TABELA DE TEMPERATURA", end="")
                                    for i in range(3):
                                        sleep(0.7)
                                        print(".", end="")
                                    print()
                                    sleep(0.21)

                                    print("\n--- TABELA DE TEMPERATURAS ---")
                                    print(f"CIDADE: {nome_cidade.upper()}")
                                    print("-------------------------------")
                                    print(f"{'HORA (H)':<10} {'TEMPERATURA (°C)':<20}")
                                    print("-------------------------------")
                                    for i in range(len(x)):
                                        print(f"{x[i]:<20.1f} {y[i]:<20.1f}")
                                    print("-------------------------------")
                                    flag = 1
                                elif op == 2:
                                    flag = 1
                                    print("\nTUDO BEM!")
                                else:
                                    print("\nOPS...OPÇÃO INVÁLIDA!\n")
                                    while True:
                                        try:
                                            print("DESEJA TENTAR NOVAMENTE?")
                                            print("1 - SIM.")
                                            print("2 - NÃO.")
                                            verificar = int(input("DIGITE AQUI: "))

                                            if verificar == 1:
                                                tipo = 0
                                                break
                                            elif verificar == 2:
                                                print("FIQUE BEM", end="")
                                                for i in range(3):
                                                    sleep(0.7)
                                                    print(".", end="")
                                                print()
                                                sleep(0.21)
                                                sys.exit()
                                            else:
                                                print("\nOPS...OPÇÃO INVÁLIDA!\n")
                                        except ValueError:
                                            print("\nENTRADA INVÁLIDA. DIGITE UMA OPÇÃO VÁLIDA.\n")

                            except ValueError:
                                print("\nENTRADA INVÁLIDA. DIGITE UMA OPÇÃO VÁLIDA.\n")
                        case 5:
                            zona = "America/Recife"
                            nome_cidade = "Recife"
                            y = np.array([24, 23, 24, 28, 31, 32, 29, 26], float)
                            tipo = 5

                            try:
                                print("\nDESEJA VER A TABELA?")
                                print("1 - SIM.")
                                print("2 - NÃO.")
                                op = int(input("DIGITE AQUI: "))

                                if op == 1:
                                    print("\nCARREGANDO TABELA DE TEMPERATURA", end="")
                                    for i in range(3):
                                        sleep(0.7)
                                        print(".", end="")
                                    print()
                                    sleep(0.21)

                                    print("\n--- TABELA DE TEMPERATURAS ---")
                                    print(f"CIDADE: {nome_cidade.upper()}")
                                    print("-------------------------------")
                                    print(f"{'HORA (H)':<10} {'TEMPERATURA (°C)':<20}")
                                    print("-------------------------------")
                                    for i in range(len(x)):
                                        print(f"{x[i]:<20.1f} {y[i]:<20.1f}")
                                    print("-------------------------------")
                                    flag = 1
                                elif op == 2:
                                    flag = 1
                                    print("\nTUDO BEM!")
                                else:
                                    print("\nOPS...OPÇÃO INVÁLIDA!")
                                    while True:
                                        try:
                                            print("DESEJA TENTAR NOVAMENTE?")
                                            print("1 - SIM.")
                                            print("2 - NÃO.")
                                            verificar = int(input("DIGITE AQUI: "))

                                            if verificar == 1:
                                                tipo = 0
                                                break
                                            elif verificar == 2:
                                                print("FIQUE BEM", end="")
                                                for i in range(3):
                                                    sleep(0.7)
                                                    print(".", end="")
                                                print()
                                                sleep(0.21)
                                                sys.exit()
                                            else:
                                                print("\nOPS...OPÇÃO INVÁLIDA!")
                                        except ValueError:
                                            print("\nENTRADA INVÁLIDA. DIGITE UMA OPÇÃO VÁLIDA.")

                            except ValueError:
                                print("\nENTRADA INVÁLIDA. DIGITE UMA OPÇÃO VÁLIDA.")
                        case _:
                            print("\nOPS...OPÇÃO INVÁLIDA!")
                            while True:
                                try:
                                    print("DESEJA TENTAR NOVAMENTE?")
                                    print("1 - SIM.")
                                    print("2 - NÃO.")
                                    verificar = int(input("DIGITE AQUI: "))

                                    if verificar == 1:
                                        tipo = 0
                                        break
                                    elif verificar == 2:
                                        print("FIQUE BEM", end="")
                                        for i in range(3):
                                            sleep(0.7)
                                            print(".", end="")
                                        print()
                                        sleep(0.21)
                                        sys.exit()
                                    else:
                                        print("\nOPS...OPÇÃO INVÁLIDA!")
                                except ValueError:
                                    print("\nENTRADA INVÁLIDA. DIGITE UMA OPÇÃO VÁLIDA.")

                elif flag == 2:
                    print("\nESCOLHA UMA CIDADE:")
                    print("1 - SÃO PAULO")
                    print("2 - NOVA YORK")
                    print("3 - LISBOA")
                    print("4 - TÓQUIO")
                    print("5 - RECIFE")

                    op = int(input("DIGITE UMA OPÇÃO: "))
                    flag = 0

                    match op:
                        case 1:
                            zona = "America/Sao_Paulo"
                            nome_cidade = "São Paulo"
                            y = np.array([19, 18, 17, 21, 26, 27, 24, 21], float)
                            tipo = 1

                            coef_newton = divided_differences(x, y)

                            try:
                                print("\nDESEJA VER A TABELA?")
                                print("1 - SIM.")
                                print("2 - NÃO.")
                                op = int(input("DIGITE AQUI: "))

                                if op == 1:
                                    print("\nCARREGANDO TABELA DE TEMPERATURA", end="")
                                    for i in range(3):
                                        sleep(0.7)
                                        print(".", end="")
                                    print()
                                    sleep(0.21)

                                    print("\n--- TABELA DE TEMPERATURAS ---")
                                    print(f"CIDADE: {nome_cidade.upper()}")
                                    print("-------------------------------")
                                    print(f"{'HORA (H)':<10} {'TEMPERATURA (°C)':<20}")
                                    print("-------------------------------")
                                    for i in range(len(x)):
                                        print(f"{x[i]:<20.1f} {y[i]:<20.1f}")
                                    print("-------------------------------")
                                    flag = 2
                                elif op == 2:
                                    flag = 2
                                    print("\nTUDO BEM!")
                                else:
                                    print("\nOPS...OPÇÃO INVÁLIDA!\n")
                                    while True:
                                        try:
                                            print("DESEJA TENTAR NOVAMENTE?")
                                            print("1 - SIM.")
                                            print("2 - NÃO.")
                                            verificar = int(input("DIGITE AQUI: "))

                                            if verificar == 1:
                                                tipo = 0
                                                break
                                            elif verificar == 2:
                                                print("FIQUE BEM", end="")
                                                for i in range(3):
                                                    sleep(0.7)
                                                    print(".", end="")
                                                print()
                                                sleep(0.21)
                                                sys.exit()
                                            else:
                                                print("\nOPS...OPÇÃO INVÁLIDA!\n")
                                        except ValueError:
                                            print("\nENTRADA INVÁLIDA. DIGITE UMA OPÇÃO VÁLIDA.")

                            except ValueError:
                                print("\nENTRADA INVÁLIDA. DIGITE UMA OPÇÃO VÁLIDA.\n")
                        case 2:
                            zona = "America/New_York"
                            nome_cidade = "Nova York"
                            y = np.array([13, 11, 10, 14, 19, 21, 18, 15], float)
                            tipo = 2

                            coef_newton = divided_differences(x, y)

                            try:
                                print("\nDESEJA VER A TABELA?")
                                print("1 - SIM.")
                                print("2 - NÃO.")
                                op = int(input("DIGITE AQUI: "))

                                if op == 1:
                                    print("\nCARREGANDO TABELA DE TEMPERATURA", end="")
                                    for i in range(3):
                                        sleep(0.7)
                                        print(".", end="")
                                    print()
                                    sleep(0.21)

                                    print("\n--- TABELA DE TEMPERATURAS ---")
                                    print(f"CIDADE: {nome_cidade.upper()}")
                                    print("-------------------------------")
                                    print(f"{'HORA (H)':<10} {'TEMPERATURA (°C)':<20}")
                                    print("-------------------------------")
                                    for i in range(len(x)):
                                        print(f"{x[i]:<20.1f} {y[i]:<20.1f}")
                                    print("-------------------------------")
                                    flag = 2
                                elif op == 2:
                                    flag = 2
                                    print("\nTUDO BEM!")
                                else:
                                    print("\nOPS...OPÇÃO INVÁLIDA!\n")
                                    while True:
                                        try:
                                            print("DESEJA TENTAR NOVAMENTE?")
                                            print("1 - SIM.")
                                            print("2 - NÃO.")
                                            verificar = int(input("DIGITE AQUI: "))

                                            if verificar == 1:
                                                tipo = 0
                                                break
                                            elif verificar == 2:
                                                print("FIQUE BEM", end="")
                                                for i in range(3):
                                                    sleep(0.7)
                                                    print(".", end="")
                                                print()
                                                sleep(0.21)
                                                sys.exit()
                                            else:
                                                print("\nOPS...OPÇÃO INVÁLIDA!\n")
                                        except ValueError:
                                            print("\nENTRADA INVÁLIDA. DIGITE UMA OPÇÃO VÁLIDA.\n")

                            except ValueError:
                                print("\nENTRADA INVÁLIDA. DIGITE UMA OPÇÃO VÁLIDA.\n")
                        case 3:
                            zona = "Europe/Lisbon"
                            nome_cidade = "Lisboa"
                            y = np.array([15, 13, 12, 17, 22, 23, 20, 17], float)
                            tipo = 3

                            coef_newton = divided_differences(x, y)

                            try:
                                print("\nDESEJA VER A TABELA?")
                                print("1 - SIM.")
                                print("2 - NÃO.")
                                op = int(input("DIGITE AQUI: "))

                                if op == 1:
                                    print("\nCARREGANDO TABELA DE TEMPERATURA", end="")
                                    for i in range(3):
                                        sleep(0.7)
                                        print(".", end="")
                                    print()
                                    sleep(0.21)

                                    print("\n--- TABELA DE TEMPERATURAS ---")
                                    print(f"CIDADE: {nome_cidade.upper()}")
                                    print("-------------------------------")
                                    print(f"{'HORA (H)':<10} {'TEMPERATURA (°C)':<20}")
                                    print("-------------------------------")
                                    for i in range(len(x)):
                                        print(f"{x[i]:<20.1f} {y[i]:<20.1f}")
                                    print("-------------------------------")
                                    flag = 2
                                elif op == 2:
                                    flag = 2
                                    print("\nTUDO BEM!")
                                else:
                                    print("\nOPS...OPÇÃO INVÁLIDA!\n")
                                    while True:
                                        try:
                                            print("DESEJA TENTAR NOVAMENTE?")
                                            print("1 - SIM.")
                                            print("2 - NÃO.")
                                            verificar = int(input("DIGITE AQUI: "))

                                            if verificar == 1:
                                                tipo = 0
                                                break
                                            elif verificar == 2:
                                                print("FIQUE BEM", end="")
                                                for i in range(3):
                                                    sleep(0.7)
                                                    print(".", end="")
                                                print()
                                                sleep(0.21)
                                                sys.exit()
                                            else:
                                                print("\nOPS...OPÇÃO INVÁLIDA!\n")
                                        except ValueError:
                                            print("\nENTRADA INVÁLIDA. DIGITE UMA OPÇÃO VÁLIDA.\n")

                            except ValueError:
                                print("\nENTRADA INVÁLIDA. DIGITE UMA OPÇÃO VÁLIDA.\n")
                        case 4:
                            zona = "Asia/Tokyo"
                            nome_cidade = "Tóquio"
                            y = np.array([20, 19, 18, 22, 27, 28, 25, 22], float)
                            tipo = 4

                            coef_newton = divided_differences(x, y)

                            try:
                                print("\nDESEJA VER A TABELA?")
                                print("1 - SIM.")
                                print("2 - NÃO.")
                                op = int(input("DIGITE AQUI: "))

                                if op == 1:
                                    print("\nCARREGANDO TABELA DE TEMPERATURA", end="")
                                    for i in range(3):
                                        sleep(0.7)
                                        print(".", end="")
                                    print()
                                    sleep(0.21)

                                    print("\n--- TABELA DE TEMPERATURAS ---")
                                    print(f"CIDADE: {nome_cidade.upper()}")
                                    print("-------------------------------")
                                    print(f"{'HORA (H)':<10} {'TEMPERATURA (°C)':<20}")
                                    print("-------------------------------")
                                    for i in range(len(x)):
                                        print(f"{x[i]:<20.1f} {y[i]:<20.1f}")
                                    print("-------------------------------")
                                    flag = 2
                                elif op == 2:
                                    flag = 2
                                    print("\nTUDO BEM!")
                                else:
                                    print("\nOPS...OPÇÃO INVÁLIDA!\n")
                                    while True:
                                        try:
                                            print("DESEJA TENTAR NOVAMENTE?")
                                            print("1 - SIM.")
                                            print("2 - NÃO.")
                                            verificar = int(input("DIGITE AQUI: "))

                                            if verificar == 1:
                                                tipo = 0
                                                break
                                            elif verificar == 2:
                                                print("FIQUE BEM", end="")
                                                for i in range(3):
                                                    sleep(0.7)
                                                    print(".", end="")
                                                print()
                                                sleep(0.21)
                                                sys.exit()
                                            else:
                                                print("\nOPS...OPÇÃO INVÁLIDA!\n")
                                        except ValueError:
                                            print("\nENTRADA INVÁLIDA. DIGITE UMA OPÇÃO VÁLIDA.\n")

                            except ValueError:
                                print("\nENTRADA INVÁLIDA. DIGITE UMA OPÇÃO VÁLIDA.\n")
                        case 5:
                            zona = "America/Recife"
                            nome_cidade = "Recife"
                            y = np.array([24, 23, 24, 28, 31, 32, 29, 26], float)
                            tipo = 5

                            coef_newton = divided_differences(x, y)

                            try:
                                print("\nDESEJA VER A TABELA?")
                                print("1 - SIM.")
                                print("2 - NÃO.")
                                op = int(input("DIGITE AQUI: "))

                                if op == 1:
                                    print("\nCARREGANDO TABELA DE TEMPERATURA", end="")
                                    for i in range(3):
                                        sleep(0.7)
                                        print(".", end="")
                                    print()
                                    sleep(0.21)

                                    print("\n--- TABELA DE TEMPERATURAS ---")
                                    print(f"CIDADE: {nome_cidade.upper()}")
                                    print("-------------------------------")
                                    print(f"{'HORA (H)':<10} {'TEMPERATURA (°C)':<20}")
                                    print("-------------------------------")
                                    for i in range(len(x)):
                                        print(f"{x[i]:<20.1f} {y[i]:<20.1f}")
                                    print("-------------------------------")
                                    flag = 2
                                elif op == 2:
                                    flag = 2
                                    print("\nTUDO BEM!")
                                else:
                                    print("\nOPS...OPÇÃO INVÁLIDA!")
                                    while True:
                                        try:
                                            print("DESEJA TENTAR NOVAMENTE?")
                                            print("1 - SIM.")
                                            print("2 - NÃO.")
                                            verificar = int(input("DIGITE AQUI: "))

                                            if verificar == 1:
                                                tipo = 0
                                                break
                                            elif verificar == 2:
                                                print("FIQUE BEM", end="")
                                                for i in range(3):
                                                    sleep(0.7)
                                                    print(".", end="")
                                                print()
                                                sleep(0.21)
                                                sys.exit()
                                            else:
                                                print("\nOPS...OPÇÃO INVÁLIDA!")
                                        except ValueError:
                                            print("\nENTRADA INVÁLIDA. DIGITE UMA OPÇÃO VÁLIDA.")

                            except ValueError:
                                print("\nENTRADA INVÁLIDA. DIGITE UMA OPÇÃO VÁLIDA.")
                        case _:
                            print("\nOPS...OPÇÃO INVÁLIDA!")
                            while True:
                                try:
                                    print("DESEJA TENTAR NOVAMENTE?")
                                    print("1 - SIM.")
                                    print("2 - NÃO.")
                                    verificar = int(input("DIGITE AQUI: "))

                                    if verificar == 1:
                                        tipo = 0
                                        break
                                    elif verificar == 2:
                                        print("FIQUE BEM", end="")
                                        for i in range(3):
                                            sleep(0.7)
                                            print(".", end="")
                                        print()
                                        sleep(0.21)
                                        sys.exit()
                                    else:
                                        print("\nOPS...OPÇÃO INVÁLIDA!")
                                except ValueError:
                                    print("\nENTRADA INVÁLIDA. DIGITE UMA OPÇÃO VÁLIDA.")
                else:
                    print("\nOPS...OPÇÃO INVÁLIDA!\n")
            except ValueError:
                print("\nENTRADA INVÁLIDA. DIGITE UMA OPÇÃO VÁLIDA.")


            while True:
                if flag == 0:
                    break

                if flag == 1:
                    cidade = ZoneInfo(zona)
                    agora = datetime.now(cidade)
                    hora_decimal = agora.hour + agora.minute / 60 + agora.second / 3600

                    temp_interp = lagrange(x, y, hora_decimal)

                    try:
                        print("\nDESEJA VER A TABELA?")
                        print("1 - SIM.")
                        print("2 - NÃO.")
                        op = int(input("DIGITE AQUI: "))

                        if op == 1:
                            flag = 1
                            print("\nCARREGANDO TABELA DE TEMPERATURA", end="")
                            for i in range(3):
                                sleep(0.7)
                                print(".", end="")
                            print()
                            sleep(0.21)

                            print("\n--- TABELA DE TEMPERATURAS ---")
                            print(f"CIDADE: {nome_cidade.upper()}")
                            print("-------------------------------")
                            print(f"{'HORA (H)':<10} {'TEMPERATURA (°C)':<20}")
                            print("-------------------------------")
                            for i in range(len(x)):
                                print(f"{x[i]:<20.1f} {y[i]:<20.1f}")
                            print("-------------------------------")

                            while True:
                                try:
                                    print(f"\nDESEJA VER A TEMPERATURA ATUAL NA CIDADE DE {nome_cidade.upper()}?\nHORÁRIO ATUAL:", agora.strftime("%H:%M:%S"))
                                    print("1 - SIM.")
                                    print("2 - NÃO.")
                                    verificar = int(input("DIGITE AQUI: "))

                                    if verificar == 1:
                                        print("\nCALCULANDO RESULTADO", end="")
                                        for _ in range(3):
                                            sleep(0.7)
                                            print(".", end="")
                                        print()
                                        sleep(0.21)
                                        print("\n--- RESULTADO ---")
                                        print("CIDADE: ", nome_cidade.upper())
                                        print("HORÁRIO ATUAL:", agora.strftime("%H:%M:%S"))
                                        print(f"HORA DECIMAL: {hora_decimal:.4f}")
                                        print(f"TEMPERATURA INTERPOLADA (LAGRANGE): {temp_interp:.2f} °C")

                                        while True:
                                            print("\nDESEJA COMPARAR OS MÉTODOS?")
                                            print("1 - SIM.")
                                            print("2 - NÃO.")
                                            verificar = int(input("DIGITE AQUI: "))

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
                                                    sys.exit()
                                                else:
                                                    print("\nOPS...OPÇÃO INVÁLIDA!\n")
                                                    while True:
                                                        try:
                                                            print("DESEJA TENTAR NOVAMENTE?")
                                                            print("1 - SIM.")
                                                            print("2 - NÃO.")
                                                            verificar = int(input("DIGITE AQUI: "))

                                                            if verificar == 1:
                                                                break
                                                            elif verificar == 2:
                                                                print("FIQUE BEM", end="")
                                                                for i in range(3):
                                                                    sleep(0.7)
                                                                    print(".", end="")
                                                                print()
                                                                sleep(0.21)
                                                                sys.exit()
                                                            else:
                                                                print("\nOPS...OPÇÃO INVÁLIDA!\n")
                                                        except ValueError:
                                                            print("\nENTRADA INVÁLIDA. DIGITE UMA OPÇÃO VÁLIDA.\n")
                                            except ValueError:
                                                print("\nENTRADA INVÁLIDA. DIGITE UMA OPÇÃO VÁLIDA.\n")
                                        break
                                    elif verificar == 2:
                                        print("FIQUE BEM", end="")
                                        for i in range(3):
                                            sleep(0.7)
                                            print(".", end="")
                                        print()
                                        sleep(0.21)
                                        sys.exit()

                                    else:
                                        print("\nOPS...OPÇÃO INVÁLIDA!\n")

                                except ValueError:
                                    print("\nENTRADA INVÁLIDA. DIGITE UMA OPÇÃO VÁLIDA.\n")
                        elif op == 2:
                            print("FIQUE BEM", end="")
                            for i in range(3):
                                sleep(0.7)
                                print(".", end="")
                            print()
                            sleep(0.21)
                            sys.exit()
                        else:
                            print("\nOPS...OPÇÃO INVÁLIDA!\n")
                            while True:
                                try:
                                    print("DESEJA TENTAR NOVAMENTE?")
                                    print("1 - SIM.")
                                    print("2 - NÃO.")
                                    verificar = int(input("DIGITE AQUI: "))

                                    if verificar == 1:
                                        tipo = 0
                                        break
                                    elif verificar == 2:
                                        print("FIQUE BEM", end="")
                                        for i in range(3):
                                            sleep(0.7)
                                            print(".", end="")
                                        print()
                                        sleep(0.21)
                                        sys.exit()
                                    else:
                                        print("\nOPS...OPÇÃO INVÁLIDA!\n")
                                except ValueError:
                                    print("\nENTRADA INVÁLIDA. DIGITE UMA OPÇÃO VÁLIDA.\n")
                        break
                    except ValueError:
                        print("\nENTRADA INVÁLIDA. DIGITE UMA OPÇÃO VÁLIDA....\n")

                if flag == 2:
                    cidade = ZoneInfo(zona)
                    agora = datetime.now(cidade)
                    hora_decimal = agora.hour + agora.minute / 60 + agora.second / 3600

                    temp_interp = newton_eval(hora_decimal, x, coef_newton)

                    try:
                        print("\nDESEJA VER A TABELA?")
                        print("1 - SIM.")
                        print("2 - NÃO.")
                        op = int(input("DIGITE AQUI: "))

                        if op == 1:
                            flag = 1
                            print("\nCARREGANDO TABELA DE TEMPERATURA", end="")
                            for i in range(3):
                                sleep(0.7)
                                print(".", end="")
                            print()
                            sleep(0.21)

                            print("\n--- TABELA DE TEMPERATURAS ---")
                            print(f"CIDADE: {nome_cidade.upper()}")
                            print("-------------------------------")
                            print(f"{'HORA (H)':<10} {'TEMPERATURA (°C)':<20}")
                            print("-------------------------------")
                            for i in range(len(x)):
                                print(f"{x[i]:<20.1f} {y[i]:<20.1f}")
                            print("-------------------------------")

                            while True:
                                try:
                                    print(
                                        f"\nDESEJA VER A TEMPERATURA ATUAL NA CIDADE DE {nome_cidade.upper()}?\nHORÁRIO ATUAL:",
                                        agora.strftime("%H:%M:%S"))
                                    print("1 - SIM.")
                                    print("2 - NÃO.")
                                    verificar = int(input("DIGITE AQUI: "))

                                    if verificar == 1:
                                        print("\nCALCULANDO RESULTADO", end="")
                                        for _ in range(3):
                                            sleep(0.7)
                                            print(".", end="")
                                        print()
                                        sleep(0.21)
                                        print("\n--- RESULTADO ---")
                                        print("CIDADE: ", nome_cidade.upper())
                                        print("HORÁRIO ATUAL:", agora.strftime("%H:%M:%S"))
                                        print(f"HORA DECIMAL: {hora_decimal:.4f}")
                                        print(f"TEMPERATURA INTERPOLADA (NEWTON): {temp_interp:.2f} °C")

                                        while True:
                                            print("\nDESEJA COMPARAR OS MÉTODOS?")
                                            print("1 - SIM.")
                                            print("2 - NÃO.")
                                            verificar = int(input("DIGITE AQUI: "))

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
                                                    sys.exit()
                                                else:
                                                    print("\nOPS...OPÇÃO INVÁLIDA!\n")
                                                    while True:
                                                        try:
                                                            print("DESEJA TENTAR NOVAMENTE?")
                                                            print("1 - SIM.")
                                                            print("2 - NÃO.")
                                                            verificar = int(input("DIGITE AQUI: "))

                                                            if verificar == 1:
                                                                break
                                                            elif verificar == 2:
                                                                print("FIQUE BEM", end="")
                                                                for i in range(3):
                                                                    sleep(0.7)
                                                                    print(".", end="")
                                                                print()
                                                                sleep(0.21)
                                                                sys.exit()
                                                            else:
                                                                print("\nOPS...OPÇÃO INVÁLIDA!\n")
                                                        except ValueError:
                                                            print("\nENTRADA INVÁLIDA. DIGITE UMA OPÇÃO VÁLIDA.\n")
                                            except ValueError:
                                                print("\nENTRADA INVÁLIDA. DIGITE UMA OPÇÃO VÁLIDA.\n")
                                        break
                                    elif verificar == 2:
                                        print("FIQUE BEM", end="")
                                        for i in range(3):
                                            sleep(0.7)
                                            print(".", end="")
                                        print()
                                        sleep(0.21)
                                        sys.exit()

                                    else:
                                        print("\nOPS...OPÇÃO INVÁLIDA!\n")

                                except ValueError:
                                    print("\nENTRADA INVÁLIDA. DIGITE UMA OPÇÃO VÁLIDA.\n")
                        elif op == 2:
                            print("FIQUE BEM", end="")
                            for i in range(3):
                                sleep(0.7)
                                print(".", end="")
                            print()
                            sleep(0.21)
                            sys.exit()
                        else:
                            print("\nOPS...OPÇÃO INVÁLIDA!\n")
                            while True:
                                try:
                                    print("DESEJA TENTAR NOVAMENTE?")
                                    print("1 - SIM.")
                                    print("2 - NÃO.")
                                    verificar = int(input("DIGITE AQUI: "))

                                    if verificar == 1:
                                        tipo = 0
                                        break
                                    elif verificar == 2:
                                        print("FIQUE BEM", end="")
                                        for i in range(3):
                                            sleep(0.7)
                                            print(".", end="")
                                        print()
                                        sleep(0.21)
                                        sys.exit()
                                    else:
                                        print("\nOPS...OPÇÃO INVÁLIDA!\n")
                                except ValueError:
                                    print("\nENTRADA INVÁLIDA. DIGITE UMA OPÇÃO VÁLIDA.\n")
                        break
                    except ValueError:
                        print("\nENTRADA INVÁLIDA. DIGITE UMA OPÇÃO VÁLIDA....\n")


            while True:
                if tipo == 0:
                    break
                match tipo:
                    case 1:
                        print("\nPREPARANDO GRÁFICOS", end="")
                        for i in range(3):
                            sleep(0.7)
                            print(".", end="")
                        print()
                        sleep(0.21)

                        t_values = np.linspace(min(x), max(x), 300)
                        p_values = [lagrange(x, y, t) for t in t_values]

                        plt.plot(t_values, p_values, label='Polinômio de Lagrange', color='blue')
                        plt.plot(t_values, p_values, label='São Paulo', color='blue')
                        plt.scatter(x, y, color='red', label='Pontos dados')
                        plt.title('Interpolação de Lagrange')
                        plt.xlabel('Hora (h)')
                        plt.ylabel('Temperatura (°C)')
                        plt.legend()
                        plt.grid(True)
                        plt.show()

                        coef_newton = divided_differences(x, y)

                        t_values = np.linspace(min(x), max(x), 300)
                        p_values = [newton_eval(ti, x, coef_newton) for ti in t_values]

                        plt.figure(figsize=(8, 5))
                        plt.plot(t_values, p_values, label='Interpolação (Newton)')
                        plt.scatter(x, y, color='red', label='Pontos dados')
                        plt.title(f'Interpolação polinomial - {nome_cidade} (Newton)')
                        plt.xlabel('Hora (h)')
                        plt.ylabel('Temperatura (°C)')
                        plt.legend()
                        plt.grid(True)
                        plt.show()
                        sleep(2)
                        break
                    case 2:
                        print("\nPREPARANDO GRÁFICOS", end="")
                        for i in range(3):
                            sleep(0.7)
                            print(".", end="")
                        print()
                        sleep(0.21)
                        t_values = np.linspace(min(x), max(x), 300)
                        p_values = [lagrange(x, y, ti) for ti in t_values]

                        plt.plot(x, y, 'ro', label='Pontos dados')
                        plt.plot(t_values, p_values, 'b-', label='Interpolação de Lagrange')
                        plt.plot(t_values, p_values, label='Nova York', color='blue')
                        plt.title('Interpolação Polinomial de Lagrange')
                        plt.xlabel('Hora (h)')
                        plt.ylabel('Temperatura (°C)')
                        plt.legend()
                        plt.grid(True)
                        plt.show()

                        coef_newton = divided_differences(x, y)

                        t_values = np.linspace(min(x), max(x), 300)
                        p_values = [newton_eval(ti, x, coef_newton) for ti in t_values]

                        plt.figure(figsize=(8, 5))
                        plt.plot(t_values, p_values, label='Interpolação (Newton)')
                        plt.scatter(x, y, color='red', label='Pontos dados')
                        plt.title(f'Interpolação polinomial - {nome_cidade} (Newton)')
                        plt.xlabel('Hora (h)')
                        plt.ylabel('Temperatura (°C)')
                        plt.legend()
                        plt.grid(True)
                        plt.show()
                        sleep(2)
                        break
                    case 3:
                        print("\nPREPARANDO GRÁFICOS", end="")
                        for i in range(3):
                            sleep(0.7)
                            print(".", end="")
                        print()
                        sleep(0.21)

                        t_values = np.linspace(min(x), max(x), 300)
                        p_values = [lagrange(x, y, ti) for ti in t_values]

                        plt.plot(t_values, p_values, 'b-', label='Interpolação de Lagrange')
                        plt.scatter(x, y, color='red', label='Pontos dados')
                        plt.plot(t_values, p_values, label='Lisboa', color='blue')
                        plt.title('Polinômio Interpolador de Lagrange')
                        plt.xlabel('Hora (h)')
                        plt.ylabel('Temperatura (°C)')
                        plt.legend()
                        plt.grid(True)
                        plt.show()

                        coef_newton = divided_differences(x, y)

                        t_values = np.linspace(min(x), max(x), 300)
                        p_values = [newton_eval(ti, x, coef_newton) for ti in t_values]

                        plt.figure(figsize=(8, 5))
                        plt.plot(t_values, p_values, label='Interpolação (Newton)')
                        plt.scatter(x, y, color='red', label='Pontos dados')
                        plt.title(f'Interpolação polinomial - {nome_cidade} (Newton)')
                        plt.xlabel('Hora (h)')
                        plt.ylabel('Temperatura (°C)')
                        plt.legend()
                        plt.grid(True)
                        plt.show()
                        sleep(2)
                        break
                    case 4:
                        print("\nPREPARANDO GRÁFICOS", end="")
                        for i in range(3):
                            sleep(0.7)
                            print(".", end="")
                        print()
                        sleep(0.21)
                        t_values = np.linspace(min(x), max(x), 300)
                        p_values = [lagrange(x, y, ti) for ti in t_values]

                        plt.plot(x, y, 'o', label='Pontos dados', color='red')
                        plt.plot(t_values, p_values, label='Polinômio de Lagrange', color='blue')
                        plt.plot(t_values, p_values, label='Tóquio', color='blue')
                        plt.title('Interpolação Polinomial de Lagrange')
                        plt.xlabel('Hora (h)')
                        plt.ylabel('Temperatura (°C)')
                        plt.legend()
                        plt.grid(True)
                        plt.show()

                        coef_newton = divided_differences(x, y)

                        t_values = np.linspace(min(x), max(x), 300)
                        p_values = [newton_eval(ti, x, coef_newton) for ti in t_values]

                        plt.figure(figsize=(8, 5))
                        plt.plot(t_values, p_values, label='Interpolação (Newton)')
                        plt.scatter(x, y, color='red', label='Pontos dados')
                        plt.title(f'Interpolação polinomial - {nome_cidade} (Newton)')
                        plt.xlabel('Hora (h)')
                        plt.ylabel('Temperatura (°C)')
                        plt.legend()
                        plt.grid(True)
                        plt.show()
                        sleep(2)
                        break
                    case 5:
                        print("\nPREPARANDO GRÁFICOS", end="")
                        for i in range(3):
                            sleep(0.7)
                            print(".", end="")
                        print()
                        sleep(0.21)
                        t_values = np.linspace(min(x), max(x), 300)
                        p_values = [lagrange(x, y, ti) for ti in t_values]

                        plt.figure(figsize=(8, 5))
                        plt.plot(x, y, 'ro', label='Pontos conhecidos')
                        plt.plot(t_values, p_values, 'b-', label='Interpolação de Lagrange')
                        plt.plot(t_values, p_values, label='Recife', color='blue')
                        plt.title('Interpolação de Lagrange')
                        plt.xlabel('Hora (h)')
                        plt.ylabel('Temperatura (°C)')
                        plt.legend()
                        plt.grid(True)
                        plt.show()

                        coef_newton = divided_differences(x, y)

                        t_values = np.linspace(min(x), max(x), 300)
                        p_values = [newton_eval(ti, x, coef_newton) for ti in t_values]

                        plt.figure(figsize=(8, 5))
                        plt.plot(t_values, p_values, label='Interpolação (Newton)')
                        plt.scatter(x, y, color='red', label='Pontos dados')
                        plt.title(f'Interpolação polinomial - {nome_cidade} (Newton)')
                        plt.xlabel('Hora (h)')
                        plt.ylabel('Temperatura (°C)')
                        plt.legend()
                        plt.grid(True)
                        plt.show()
                        sleep(2)
                        break
            break

        except ValueError:
            print("\nENTRADA INVÁLIDA. DIGITE UMA OPÇÃO VÁLIDA.\n")
