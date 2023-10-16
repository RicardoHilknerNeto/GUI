# Importa a biblioteca tkinter para criar a interface gráfica
from tkinter import *

# Cria uma janela principal
window = Tk()

# Define o título e a geometria da janela (largura x altura + posição_x + posição_y)
window.title("Título da Janela")
window.geometry("350x250+400+200")

# Configura o plano de fundo da janela
window.configure(background="moccasin")

# Cria um rótulo (um componente de texto) dentro da janela
rotulo = Label(window)

# Define o texto do rótulo
rotulo["text"] = "Hello World"

# Define a fonte, tamanho e estilo do texto no rótulo
rotulo["font"] = ("Impact", "20", "bold")

# Define a cor do texto no rótulo
rotulo["fg"] = "brown"

# Define a cor de fundo do rótulo
rotulo["bg"] = "moccasin"

# Define o preenchimento vertical (padding) do rótulo
rotulo["pady"] = 5

# Define o preenchimento horizontal (padding) do rótulo
rotulo["padx"] = 10

# Define a largura do rótulo em caracteres
rotulo["width"] = 20

# Define o alinhamento do texto no rótulo (oeste, neste caso)
rotulo["anchor"] = "w"

# Empacota o rótulo na janela para exibi-lo
rotulo.pack()

# Mantém a janela aberta e aguardando interações do usuário
window.mainloop()
