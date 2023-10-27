from tkinter import *


def muda_imagem():
    nova_imagem = "../aula 02/imagens/" + escolha.get() + ".png"
    imagem["file"] = nova_imagem

fonte = ("Arial", "12")
window = Tk()
window.title("Esolha seu avatar")
window.geometry("400x200")
window.configure(bg="moccasin")
escolha = StringVar()
escolha.set("chaplin")
container1 = Frame(window, padx=10, bg="moccasin")
container2 = Frame(window, padx=10, bg="moccasin")
container1.pack(side=LEFT)
container2.pack(side=TOP)
texto= ["Charles Chaplin", "Harley Quinn", "Ninja do Deserto", "Copo do Zorro"]
valor = ["chaplin", "arlequina", "ninja", "zorro"]

for i in range(0, 4, 1):
    Radiobutton(container1, text=[i], value=[i], variable=escolha, width=15, anchor="w", padx=10, pady=10, indicatoron=False,bg="moccasin", font=fonte, command=muda_imagem).pack()

imagem = PhotoImage(file="../aula 02/imagens/chaplin.png")
rotulo = Label(container2, image=imagem, bg="moccasin")

rotulo.pack()
window.mainloop()