import pywhatkit as kit
import os
from datetime import datetime, timedelta

caminho_da_pasta = os.path.dirname(os.path.abspath(__file__))

os.chdir(caminho_da_pasta)

data_atual = datetime.now()
tempo_agendado = data_atual + timedelta(minutes=2)

nome_cliente = "Julia"

kit.sendwhatmsg("", 
                f"Olá, {nome_cliente}. Tudo bem? O seu pedido já está finalizado e pronto para retirada. Nosso horário de funcionamento é das 10h às 17h.",
                data_atual.hour,
                data_atual.minute + 2)