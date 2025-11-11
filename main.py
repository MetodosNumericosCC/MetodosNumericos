def mostrar_tabela(x_points, y_points):
    """
    Exibe os dados (hora x temperatura) em formato de tabela (matriz).
    """
    print("\nTABELA DE DADOS - VARIAÇÃO DE TEMPERATURA")
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
    # Dados base (hora x temperatura)
    x_points = [6, 9, 12, 15, 18]
    y_points = [15, 18, 24, 22, 19]

    # Mostra tabela de dados
    mostrar_tabela(x_points, y_points)

    # Solicita ao usuário a hora que deseja estimar
    try:
        x_estimar = float(input("Digite a hora do dia que deseja estimar a temperatura: "))
        y_estimado = lagrange_interpol(x_points, y_points, x_estimar)

        if x_estimar > 18:
            print("Não é possivel fazer a interpolação, pós o valor excede os dados do gráfico!")
        else:
            print(f"\n🌡️  Temperatura estimada às {x_estimar:.2f}h: {y_estimado:.2f} °C\n")
    except ValueError:
        print("\n❌ Entrada inválida. Digite um número válido para a hora.\n")


if __name__ == "__main__":
    main()