def fazer_pergunta(pergunta, opcoes, resposta_correta, feedback, i):
    print(f"\n{pergunta}")
    for j, opcao in enumerate(opcoes):  # Usando 'j' para o índice do loop interno
        print(f"{chr(65+j)}) {opcao}")

    resposta_usuario = input("Sua resposta: ").strip().upper()

    if resposta_usuario == resposta_correta:
        print(f"Parabéns! Sua resposta está correta.\n\n{feedback[resposta_correta][i]}")
    else:
        print(f"Que pena! A resposta correta é {resposta_correta}.\n\n{feedback[resposta_correta][i]}")

def iniciar_quiz():
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

    feedbacks = {
        'A': [
            "A primeira corrida da Fórmula E ocorreu em 2014, em Pequim.",
            "Os carros da Fórmula E utilizam motores elétricos.",
            "Alejandro Agag é o fundador da Fórmula E.",
            "A primeira corrida da Fórmula E foi em Pequim.",
            "Cada equipe na Fórmula E possui dois carros.",
            "A principal diferença é o uso de motores elétricos na Fórmula E e motores a combustão na Fórmula 1.",
            "Uma corrida de Fórmula E dura em média 45 minutos + 1 volta.",
            "Até 2023, foram completadas 9 temporadas da Fórmula E.",
            "O sistema de votação dos fãs na Fórmula E é chamado Fanboost.",
            "O troféu do campeão da Fórmula E é chamado Troféu ABB FIA."
        ],
        'B': [
            "A primeira corrida da Fórmula E ocorreu em 2014, não em 2012.",
            "Os carros da Fórmula E utilizam motores elétricos, e não a gasolina.",
            "Alejandro Agag é o fundador da Fórmula E.",
            "A primeira corrida da Fórmula E foi em Pequim, não em Paris.",
            "Cada equipe na Fórmula E possui dois carros.",
            "A principal diferença é o uso de motores elétricos na Fórmula E e motores a combustão na Fórmula 1.",
            "Uma corrida de Fórmula E dura em média 45 minutos + 1 volta.",
            "Até 2023, foram completadas 9 temporadas da Fórmula E.",
            "O sistema de votação dos fãs na Fórmula E é chamado Fanboost.",
            "O troféu do campeão da Fórmula E é chamado Troféu ABB FIA."
        ],
        'C': [
            "A primeira corrida da Fórmula E ocorreu em 2014, não em 2013.",
            "Os carros da Fórmula E utilizam motores elétricos, e não híbridos.",
            "Alejandro Agag é o fundador da Fórmula E.",
            "A primeira corrida da Fórmula E foi em Pequim.",
            "Cada equipe na Fórmula E possui dois carros.",
            "A principal diferença é o uso de motores elétricos na Fórmula E e motores a combustão na Fórmula 1.",
            "Uma corrida de Fórmula E dura em média 45 minutos + 1 volta.",
            "Até 2023, foram completadas 9 temporadas da Fórmula E.",
            "O sistema de votação dos fãs na Fórmula E é chamado Fanboost.",
            "O troféu do campeão da Fórmula E é chamado Troféu ABB FIA."
        ],
        'D': [
            "A primeira corrida da Fórmula E ocorreu em 2014, não em 2015.",
            "Os carros da Fórmula E utilizam motores elétricos, e não a diesel.",
            "Alejandro Agag é o fundador da Fórmula E.",
            "A primeira corrida da Fórmula E foi em Pequim, não em Londres.",
            "Cada equipe na Fórmula E possui dois carros.",
            "A principal diferença é o uso de motores elétricos na Fórmula E e motores a combustão na Fórmula 1.",
            "Uma corrida de Fórmula E dura em média 45 minutos + 1 volta.",
            "Até 2023, foram completadas 9 temporadas da Fórmula E.",
            "O sistema de votação dos fãs na Fórmula E é chamado Fanboost.",
            "O troféu do campeão da Fórmula E é chamado Troféu ABB FIA."
        ]
    }

    for i in range(len(perguntas)):
        fazer_pergunta(perguntas[i], opcoes[i], respostas_certas[i], feedbacks, i)

iniciar_quiz()
