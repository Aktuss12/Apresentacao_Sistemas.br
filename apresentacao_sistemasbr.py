from tkinter import *
import webbrowser

# Configurações da janela
janela = Tk()
janela.title("Entrevista")
janela.geometry("400x450")
janela.configure(bg="#6959CD")

# Funções
def home():
    webbrowser.open("https://sistemasbr.com.br/")

def solucoes():
    webbrowser.open("https://sistemasbr.com.br/solucoes/sigecom/")

def quem_somos():
    webbrowser.open("https://sistemasbr.com.br/sobre-nos/")

def parceria():
    webbrowser.open("https://sistemasbr.com.br/seja-parceiro/")

def servicos():
    webbrowser.open("https://sistemasbr.com.br/segmentos/prestadores-de-servicos/")

def central_atendimento():
    webbrowser.open("https://api.whatsapp.com/send/?phone=551736223222&text&type=phone_number&app_absent=0")

def blog():
    webbrowser.open("https://sistemasbr.com.br/nossoblog/")

# Frames 
frame_tela = Frame(janela, width=400, height=135, bg="#7CFC00")
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=0, height=0, bg="#6959CD",
                    relief=FLAT, bd=0)
frame_corpo.grid(row=1, column=0)

# Titulo
texto = Label(text="Sistemas.br", width=15, height=2, bg="#000000", fg="#FFFF00",
              font='Consolas 20 bold', relief=FLAT, bd=0)
texto.place(x=92, y=35)

# Botões
home = Button(frame_corpo, text="Home", command=home, font='Consolas 15 bold', bg="#FFFF00")
home.pack(pady=11)

solucoes = Button(frame_corpo, text="Soluções", command=solucoes, font='Consolas 15 bold', bg="#FFFF00")
solucoes.pack(pady=11)

quem_somos = Button(frame_corpo, text="Quem Somos", command=quem_somos, font='Consolas 15 bold', bg="#FFFF00")
quem_somos.pack(pady=11)

parceria = Button(frame_corpo, text="Parceria", command=parceria, font='Consolas 15 bold', bg="#FFFF00")
parceria.pack(pady=11)

servicos = Button(janela, text="Serviços", command=servicos, font='Consolas 14 bold', bg="#FFFF00")
servicos.place(relx=1.0, rely=1.0, anchor='se', x=-275, y=-15)

central_atendimento = Button(janela, text="Contato", command=central_atendimento, font='Consolas 14 bold', bg="#FFFF00")
central_atendimento.place(relx=1.0, rely=1.0, anchor='se', x=-160, y=-15)

blog = Button(janela, text="Nosso blog", command=blog, font='Consolas 14 bold', bg="#FFFF00")
blog.place(relx=1.0, rely=1.0, anchor='se', x=-16, y=-15)

janela.mainloop()