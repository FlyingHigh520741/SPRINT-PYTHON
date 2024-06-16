import time
from datetime import datetime

hora_corrida = datetime(2024, 6, 29, 18, 3, 0)  # Definimos a data da próxima corrida (Ano, Mês, Dia, Hora, Minuto e Segundo)

def contagem_regressiva(hora_corrida): #Função para calcular e mostrar a contagem regressiva até a próxima corrida.
    
    while True:
        agora = datetime.now()
        tempo_restante = hora_corrida - agora  # Calcula o tempo restante até a corrida
        
        if tempo_restante.total_seconds() <= 0:  # Verifica se o tempo restante é menor ou igual a zero, indicando que a corrida começou
            print("A corrida começou!")
            break
        
        dias = tempo_restante.days
        horas, segundos = divmod(tempo_restante.seconds, 3600)
        minutos, segundos = divmod(segundos, 60)

        mensagem = (f'Próxima corrida em: {hora_corrida.strftime("%d/%m/%Y %H:%M:%S")}' ) # Utilizamos uma váriavel para montar a mensagem com a data da próxima corrida
        mensagem += (f' | Tempo restante: {dias}d {horas}h {minutos}m {segundos}s')  # Adiciona o tempo restante à mensagem

        print(mensagem, end='\r', flush=True)  # Imprime a mensagem no terminal, atualizando a linha
        
        time.sleep(1)  # Aguarda 1 segundo antes de atualizar novamente

contagem_regressiva(hora_corrida)  # Chama a função para iniciar a contagem regressiva no terminal
 