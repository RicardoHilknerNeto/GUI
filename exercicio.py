from tkinter import *

def soma_numeros():
    resultado["text"] = int(caixa_texto.get()) + int(caixa_texto2.get())


window = Tk()
window.title("Soma Números")
window.geometry("350x250+400+200")

rotulo1 = Label(window, text="Digite números abaixo:", font="Impact 16 bold")
rotulo1.pack()

container = Frame(window, pady=15, padx=10)
container.pack()

rotulo2 = Label( container, text="1 N :", font="Impact 16", pady=10 )
rotulo2.pack(side=LEFT)

caixa_texto = Entry(container, font=("Times New Roman", "10"))
caixa_texto.pack(side=LEFT)

rotulo3 = Label( container, text="2 N :", font="Impact 16", pady=10 )
rotulo3.pack(side=LEFT)

caixa_texto2 = Entry(container, font=("Times New Roman", "10"))
caixa_texto2.pack(side=RIGHT)

botao = Button(window, text="Somar", pady=5,padx=10, bg="black", fg="white")
botao["font"] = ("Courier New", "16", "bold")
botao["command"] = soma_numeros
botao.pack()

resultado = Label( window, text="", font="Impact 16", pady=10 )
resultado.pack()

window.mainloop()