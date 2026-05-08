def mostrar_trabuleiro(tab):
    print("\n")
    print(f" {tab[0][0]} | {tab[0][1]} | {tab[0][2]}")
    print("---+---+---")
    print(f" {tab[1][0]} | {tab[1][1]} | {tab[1][2]}")
    print("---+---+---")
    print(f" {tab[2][0]} | {tab[2][1]} | {tab[2][2]}")
    print("\n")


def verificacao_vitoria(tab, jogador):

    # Linhas
    for i in range(3):
        if tab[i][0] == jogador and tab[i][1] == jogador and tab[i][2] == jogador:
            return True

    # Colunas
    for i in range(3):
        if tab[0][i] == jogador and tab[1][i] == jogador and tab[2][i] == jogador:
            return True

    # Diagonal principal
    if tab[0][0] == jogador and tab[1][1] == jogador and tab[2][2] == jogador:
        return True

    # Diagonal secundária
    if tab[0][2] == jogador and tab[1][1] == jogador and tab[2][0] == jogador:
        return True

    return False


while True:

    tabuleiro = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]
    ]

    jogador_atual = 'X'

    print("=" * 25)
    print("      JOGO DA VELHA")
    print("=" * 25)

    for rodada in range(9):

        mostrar_trabuleiro(tabuleiro)

        try:
            escolha = input(f"Jogador {jogador_atual}, escolha uma posição (1-9): ")

            pos = int(escolha) - 1

            if pos < 0 or pos > 8:
                print("\n❌ Escolha um número de 1 até 9.\n")
                continue

            linha = pos // 3
            coluna = pos % 3

            if tabuleiro[linha][coluna] in ['X', 'O']:
                print("\n⚠️ Essa posição já está ocupada.\n")
                continue

            tabuleiro[linha][coluna] = jogador_atual

            if verificacao_vitoria(tabuleiro, jogador_atual):
                mostrar_trabuleiro(tabuleiro)

                print("=" * 25)
                print(f"🏆 Jogador {jogador_atual} venceu!")
                print("=" * 25)

                break

            if jogador_atual == 'X':
                jogador_atual = 'O'
            else:
                jogador_atual = 'X'

        except ValueError:
            print("\n❌ Digite apenas números.\n")

    else:
        mostrar_trabuleiro(tabuleiro)

        print("=" * 25)
        print("🤝 Deu velha! Empate.")
        print("=" * 25)

    # Pergunta se quer jogar novamente
    while True:

        resposta = input("\nQuer jogar novamente? (s/n): ").lower()

        if resposta == 's':
            break

        elif resposta == 'n':
            print("\n👋 Obrigado por jogar!")
            exit()

        else:
            print("❌ Digite apenas 's' ou 'n'.")