# JOGO DA VÉIA
print('-='*30)
print('JOGO DA VÉIA')
print('-='*30)


def criar_tabuleiro():
    return ["1", "2", "3",
            "4", "5", "6",
            "7", "8", "9"]


def mostrar_tabuleiro(tabuleiro):
    print(f"""
     {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}
    ---+---+---
     {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}
    ---+---+---
     {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}
    """)


def verificar_vitoria(tabuleiro, jogador):
    combinacoes = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for combo in combinacoes:
        if (
            tabuleiro[combo[0]] == jogador and
            tabuleiro[combo[1]] == jogador and
            tabuleiro[combo[2]] == jogador
        ):
            return True

    return False


def tabuleiro_cheio(tabuleiro):
    for casa in tabuleiro:
        if casa not in ["X", "O"]:
            return False
    return True


while True:

    tabuleiro = criar_tabuleiro()
    jogador = "X"

    # LOOP DA PARTIDA
    while True:

        mostrar_tabuleiro(tabuleiro)

        try:
            posicao = int(input(f"Jogador {jogador}, escolha uma posição (1-9): ")) - 1

            if posicao < 0 or posicao > 8:
                print("❌ Posição inválida!")
                continue

            if tabuleiro[posicao] in ["X", "O"]:
                print("⚠️ Essa posição já está ocupada!")
                continue

            tabuleiro[posicao] = jogador

            if verificar_vitoria(tabuleiro, jogador):
                mostrar_tabuleiro(tabuleiro)
                print(f"\n🎉 Jogador {jogador} venceu!")
                break

            if tabuleiro_cheio(tabuleiro):
                mostrar_tabuleiro(tabuleiro)
                print("\n😐 Deu velha!")
                break

            # troca de jogador
            if jogador == "X":
                jogador = "O"
            else:
                jogador = "X"

        except ValueError:
            print("❌ Digite apenas números!")

    # LOOP DA RESPOSTA
    while True:

        jogar_novamente = input("\nQuer jogar de novo? (s/n): ").lower()

        if jogar_novamente == "s":
            break

        elif jogar_novamente == "n":
            print("👋 Jogo encerrado!")
            exit()

        else:
            print("❌ Digite apenas 's' ou 'n'!")
