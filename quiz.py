def fazer_pergunta(pergunta, opcoes, resposta_correta): # Utilizamos a função para fazer a pergunta ao usuário e verificar se a resposta está correta
    # Utilizado para exibir a pergunta e as opções de resposta
    print(f"\n{pergunta}")
    for i, opcao in enumerate(opcoes):
        print(f"{chr(65+i)}) {opcao}")

    resposta_usuario = input("Sua resposta: ").strip().upper() # Recebemos a resposta do usuário

    if resposta_usuario == resposta_correta: # Verifica se a resposta do usuário está correta
        return True
    else:
        return False


def calcular_pontuacao(respostas): # Calcula a pontuação de acordo com as respostas
    return sum(respostas)

def exibir_resultados(respostas): # Utilizamos para exibir o resultado de cada pergunta (Correta ou Errada)
    for i, correta in enumerate(respostas):
        if correta:
            resultado = "correta"
        else:
            resultado = "errada"
        print(f"Questão {i+1}: {resultado}")


def perguntas():
    # Listas contendo perguntas, opções e respostas corretas
    perguntas = [
        "1- Ano da primeira corrida da Fórmula E?",
        "2- Principal característica dos carros da Fórmula E?",
        "3- Fundador da Fórmula E?",
        "4- Cidade da primeira corrida da Fórmula E?",
        "5- Quantos carros por equipe na Fórmula E?",
        "6- Diferença principal entre Fórmula E e Fórmula 1?",
        "7- Duração média de uma corrida de Fórmula E?",
        "8- Temporadas completadas até 2023?",
        "9- Sistema de votação dos fãs?",
        "10- Nome do troféu do campeão da Fórmula E?"
    ]

    opcoes = [
        ["2012", "2013", "2014", "2015"],
        ["Motores a gasolina", "Motores elétricos", "Motores híbridos", "Motores a diesel"],
        ["Alejandro Agag", "Bernie Ecclestone", "Jean Todt", "Toto Wolff"],
        ["Nova York", "Paris", "Pequim", "Londres"],
        ["Um", "Dois", "Três", "Quatro"],
        ["Motores elétricos vs. combustão", "Corridas mais longas", "Circuitos ovais vs. de rua", "Reabastecimento permitido"],
        ["45 min + 1 volta", "60 min + 2 voltas", "90 min + 1 volta", "120 min + 2 voltas"],
        ["7", "8", "9", "10"],
        ["Fan Boost", "Power Up", "Speed Boost", "Turbo Vote"],
        ["Troféu de Ouro", "Troféu das Estrelas", "Troféu Jules Bianchi", "Troféu ABB FIA"]
    ]

    respostas_certas = ['C', 'B', 'A', 'C', 'B', 'A', 'A', 'D', 'A', 'D']

    respostas = [] # Armazena a resposta do usuário

    # Loop perguntas e coletar as respostas do usuário
    for i in range(len(perguntas)):
        correta = fazer_pergunta(perguntas[i], opcoes[i], respostas_certas[i])
        respostas.append(correta)

    pontuacao = calcular_pontuacao(respostas)  # Usado para calcular a pontuação total

    print(f"\nVocê tem {pontuacao} pontos acumulados.\n")  # Exibir a pontuação final do usuário

    exibir_resultados(respostas) # Exibir os resultados de cada pergunta


perguntas() # Chamamos a função para rodar o código no terminal
