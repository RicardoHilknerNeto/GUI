# Ricardo Hilkner Neto
# RM: 550757

from tkinter.ttk import *
from tkinter import *

dic = [
    {
        "Escolha": 0.0,
        "burger": 34.90,
        "noodles": 44.50,
        "pizza": 49.00,
    },
    {
        "fritas": 14.90,
        "nuggets": 9.50,
        "milho": 12.30,
    },
    {
        "suco": 14.90,
        "shake": 19.90
    }
]

def mudaImagem():
    nova_imagem = "cardapio/" + comboLanche.get() + ".png"
    nova_imagem2 = "cardapio/" + comboPorcao.get() + ".png"
    nova_imagem3 = "cardapio/" + comboBebida.get() + ".png"

    imagem["file"] = nova_imagem
    imagem2["file"] = nova_imagem2
    imagem3["file"] = nova_imagem3

def calcular_total():
    lanche = comboLanche.get()
    porcao = comboPorcao.get()
    bebida = comboBebida.get()

    total = dic[0].get(lanche, 0) + dic[1].get(porcao, 0) + dic[2].get(bebida, 0)
    resultado["text"] = f"Total: R${total:.2f}"

fonte = ("Cooper Black", "14")
window = Tk()
window.title("Escolha um Combo")
window.geometry("600x400")

container = Frame(window, pady=1, padx=10)
container.pack()
rotulo1 = Label(container, text="Lanche:", font="Impact 16", pady=5)
rotulo1.pack(side=LEFT)
comboLanche = Combobox(container)
comboLanche["values"] = ("Escolha", "burger", "noodles", "pizza")
comboLanche["state"] = "readonly"
comboLanche.current(0)
comboLanche.pack(side=LEFT)

container = Frame(window, pady=1, padx=5)
container.pack()
rotulo1 = Label(container, text="Porção:", font="Impact 16", pady=5)
rotulo1.pack(side=LEFT)
comboPorcao = Combobox(container)
comboPorcao["values"] = ("Escolha", "fritas", "nuggets", "milho")
comboPorcao["state"] = "readonly"
comboPorcao.current(0)
comboPorcao.pack(side=LEFT)

container = Frame(window, pady=5, padx=5)
container.pack()
rotulo1 = Label(container, text="Bebida:", font="Impact 16", pady=5)
rotulo1.pack(side=LEFT)
comboBebida = Combobox(container)
comboBebida["values"] = ("Escolha", "suco", "shake")
comboBebida["state"] = "readonly"
comboBebida.current(0)
comboBebida.pack(side=LEFT)

container1 = Frame(window, pady=20, padx=10)
container1.pack()
imagem = PhotoImage(file="cardapio/escolha.png")
imagem2 = PhotoImage(file="cardapio/escolha.png")
imagem3 = PhotoImage(file="cardapio/escolha.png")

rotulo2 = Label(container1, image=imagem)
rotulo2.pack(side=LEFT)
rotulo4 = Label(container1, image=imagem3)
rotulo4.pack(side=RIGHT)
rotulo3 = Label(container1, image=imagem2)
rotulo3.pack(side=RIGHT)

botao = Button(window, text="Fazer Pedido", padx=10, font=fonte, command=lambda: [mudaImagem(), calcular_total()])
botao.pack()


resultado = Label(window, text="Total:", font="Impact 16", pady=10)
resultado.pack()

window.mainloop()
