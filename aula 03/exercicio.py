from tkinter import *

def muda_imagem():
    nova_imagem = "../aula 03/jogo_img/" + escolha.get() + ".png"
    imagem["file"] = nova_imagem

fonte = ("Arial", "12")
window = Tk()
window.title("Escolha seu avatar")
window.geometry("400x200")
window.configure(bg="moccasin")
escolha = StringVar()
escolha.set("vazio")
container1 = Frame(window, padx=10, bg="moccasin")
container2 = Frame(window, padx=10, bg="moccasin")
container3 = Frame(window, padx=10, bg="moccasin")
container1.pack(side=LEFT)
container2.pack(side=TOP)
container3.pack(side=TOP)

containerTitle = Frame(window)
containertotal = Frame(window)

jogador = Label( containerTitle, text="Jogador ", font="Impact 20", bg="moccasin")
jogador.pack(side=LEFT)

computador = Label( containerTitle, text="computador ", font="Impact 20", bg="moccasin")
computador.pack(side=RIGHT)

texto = ["Pedra", "Papel", "Tesoura"]
valor = ["pedra", "papel", "tesoura"]

for i in range(3):
    Radiobutton(container1, text=texto[i], value=valor[i], variable=escolha, width=15, anchor="w", padx=10, pady=10, indicatoron=False, bg="moccasin", font=fonte, command=muda_imagem).pack(side=BOTTOM)


imagem = PhotoImage(file="../aula 03/jogo_img/vazio.png")
rotulo = Label(containertotal, image=imagem, bg="moccasin")
rotulo1 = Label(containertotal, image=imagem, bg="moccasin")
rotulo.pack(side=LEFT)
rotulo1.pack(side=RIGHT)
containertotal.pack()
containerTitle.pack(side=TOP)

window.mainloop()
