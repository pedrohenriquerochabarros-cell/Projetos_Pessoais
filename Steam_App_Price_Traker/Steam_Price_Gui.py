from Steam_Price_CSV import processar_busca
from tkinter import *

BLUE = "#483d8b"
FONT_NAME = "Courier"

##----- Botão ADD -----##

def buscar_e_atualizar_ui():
    app_id = game_name.get()
    if len(app_id) == 0:
        return

    melhor_preco, melhor_data, preco_atual = processar_busca(app_id)

    preco_texto.config(text=melhor_preco)
    data_texto.config(text=melhor_data)
    valor_preco_atual.config(text=preco_atual) 
    
    game_name.delete(0, 'end')

##----- UI Setup -----##

window = Tk()
window.title("Podex Game")
window.config(padx=20, pady=20, bg=BLUE, highlightthickness=0)

canvas = Canvas(height=100, width=176, bg=BLUE, highlightthickness=0)
logo_img = PhotoImage(file="Steam_logo.png")
canvas.create_image(89, 38, image=logo_img)
canvas.grid(column=0, row=0, columnspan=2)

game_name = Entry(width=40)
game_name.grid(column=0, row=1, columnspan=2)

botao_ADD = Button(text="Adicionar / Buscar", command=buscar_e_atualizar_ui, font=(FONT_NAME, 10, "bold")) 
botao_ADD.grid(column=0, row=2, columnspan=2, pady=10)

label_preco = Label(text="Preço", bg=BLUE, highlightthickness=0,font=(FONT_NAME, 15, "bold"))
label_preco.grid(column=0, row=3)

labal_data = Label(text="Data", bg=BLUE, highlightthickness=0,font=(FONT_NAME, 15, "bold"))
labal_data.grid(column=1, row=3)

labal_preco_atual = Label(text="Preço Atual", bg=BLUE, highlightthickness=0,font=(FONT_NAME, 15, "bold"))
labal_preco_atual.grid(column=0, row=5, columnspan=2)

##----- UI Resposta Setup -----##

preco_texto = Label(text="R$ ---", bg=BLUE, highlightthickness=0, font=(FONT_NAME, 15, "bold"))
preco_texto.grid(column=0, row=4)

data_texto = Label(text="--/--/-----", bg=BLUE, highlightthickness=0, font=(FONT_NAME, 15, "bold"))
data_texto.grid(column=1, row=4)

valor_preco_atual = Label(text="R$ ---", bg=BLUE, highlightthickness=0, font=(FONT_NAME, 15, "bold"))
valor_preco_atual.grid(column=0, row=6, columnspan=2)

window.mainloop()