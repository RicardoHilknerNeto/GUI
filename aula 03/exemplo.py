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

radio_chaplin = Radiobutton(container1, text="Charles Chaplin", value="chaplin", variable=escolha, width=15, anchor="w", padx=10, pady=10, bg="moccasin", font=fonte, command=muda_imagem)
radio_chaplin.pack()

radio_arlequina = Radiobutton(container1, text="Harley Quinn", value="arlequina", variable=escolha, width=15, anchor="w", padx=10, pady=10, bg="moccasin", font=fonte, command=muda_imagem)
radio_arlequina.pack()

radio_ninja = Radiobutton(container1, text="Ninja do Deserto", value="ninja", variable=escolha, width=15, anchor="w", padx=10, pady=10, bg="moccasin", font=fonte, command=muda_imagem)
radio_ninja.pack()

radio_zorro = Radiobutton(container1, text="Copo do Zorro", value="zorro", variable=escolha, width=15, anchor="w", padx=10, pady=10, bg="moccasin", font=fonte, command=muda_imagem)
radio_zorro.pack()

imagem = PhotoImage(file="../aula 02/imagens/chaplin.png")
rotulo = Label(container2, image=imagem, bg="moccasin")
rotulo.pack()

window.mainloop()