import tkinter as tk
from datetime import datetime, timedelta

def contagem_regressiva(hora_corrida):
    janela = tk.Tk()
    janela.title("Contagem Regressiva Fórmula E")

    # Rótulo para a mensagem "Próxima corrida em:"
    rotulo_proxima_corrida = tk.Label(janela, text="Próxima corrida em:")
    rotulo_proxima_corrida.pack(pady=10)

    # Rótulo para exibir a data da próxima corrida
    rotulo_data_corrida = tk.Label(janela, text=hora_corrida.strftime("%d/%m/%Y %H:%M:%S"))
    rotulo_data_corrida.pack()

    # Rótulo para a mensagem "Tempo restante:"
    rotulo_tempo_restante = tk.Label(janela, text="Tempo restante:")
    rotulo_tempo_restante.pack(pady=10)

    # Rótulo para exibir o tempo restante (inicialmente vazio)
    rotulo_tempo = tk.Label(janela, text="")
    rotulo_tempo.pack()

    def atualizar_tempo():
        agora = datetime.now()
        tempo_restante = hora_corrida - agora

        if tempo_restante.total_seconds() <= 0:
            rotulo_tempo.config(text="A corrida começou!")
        else:
            dias = tempo_restante.days
            horas, segundos = divmod(tempo_restante.seconds, 3600)
            minutos, segundos = divmod(segundos, 60)
            rotulo_tempo.config(text=f"{dias}d {horas}h {minutos}m {segundos}s")
            janela.after(1000, atualizar_tempo)  # Atualiza a cada 1 segundo

    atualizar_tempo()
    janela.mainloop()

# Data da próxima corrida (substitua pela data correta)
proxima_corrida = datetime(2024, 10, 29, 18, 3, 0)  
contagem_regressiva(proxima_corrida)
