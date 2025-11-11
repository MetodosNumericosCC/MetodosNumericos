import numpy as np
import sympy as sp
import matplotlib.pyplot as plt


def mostrar_tabela(x_points, y_points):
    """
    Exibe os dados (hora x temperatura) em formato de tabela (matriz).
    """
    print("\nTABELA DE DADOS - VARIAÇÃO DE TEMPERATURA DO MUNICÍPIO DE CARUARU - DATA: 12/10/2025")
    print("┌────────────┬───────────────────────┐")
    print("│  Hora (h)  │  Temperatura (°C)     │")
    print("├────────────┼───────────────────────┤")
    for x, y in zip(x_points, y_points):
        print(f"│    {x:>5}   │       {y:>8.2f}        │")
    print("└────────────┴───────────────────────┘\n")


def lagrange_interpol(x_points, y_points, x):
    """
    Interpolação de Lagrange para estimar y em um dado x.
    """
    n = len(x_points)
    result = 0.0

    for i in range(n):
        L_i = 1.0
        for j in range(n):
            if i != j:
                L_i *= (x - x_points[j]) / (x_points[i] - x_points[j])
        result += y_points[i] * L_i

    return result


def main():

    x_points = [0, 3, 6, 9, 12, 15, 18, 21]
    y_points = [18.5, 18.5, 18.2, 18, 21.3, 25.4, 24.3, 20.2]

    mostrar_tabela(x_points, y_points)

    try:
        x_estimar = float(input("Digite a hora do dia que deseja estimar a temperatura: "))
        y_estimado = lagrange_interpol(x_points, y_points, x_estimar)

        print(f"\n🌡️  Temperatura estimada às {x_estimar:.2f}h: {y_estimado:.2f} °C\n")
    except ValueError:
        print("\n❌ Entrada inválida. Digite um número válido para a hora.\n")


if __name__ == "__main__":
    main()
