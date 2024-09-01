# Apresentação Sistemas.br

Este repositório contém o projeto "Apresentação Sistemas.br"

## Funcionalidades

- **Apresentação Interativa**: Demonstração de sistemas e banco de dados com uma interface intuitiva e responsiva
- **Design Moderno**: Layout atraente que facilita a navegação e a compreensão dos conteúdos
- **Integração de Dados**: Mostra como os sistemas interagem com dados reais
- **Suporte a Múltiplas Plataformas**: A aplicação é compatível com dispositivos móveis e desktops

## Tecnologias Utilizadas

- **Linguagem**: [Python]
- **Ferramentas de Desenvolvimento**: [VSCode]

## Código em Python

### Descrição

Esta seção contém o código Python utilizado para criar uma interface gráfica com o `tkinter`. A aplicação apresenta um menu com botões que direcionam para diferentes seções do site Sistemas.br e outras funcionalidades de contato.

### Código

```python
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

parceria = Button(frame_corpo, text="Parceria", command=parceria, font='Consolas 15 bold', bg="#FFFF00")
parceria.pack(pady=11)

solucoes = Button(frame_corpo, text="Soluções", command=solucoes, font='Consolas 15 bold', bg="#FFFF00")
solucoes.pack(pady=11)

quem_somos = Button(frame_corpo, text="Quem Somos", command=quem_somos, font='Consolas 15 bold', bg="#FFFF00")
quem_somos.pack(pady=11)

servicos = Button(janela, text="Serviços", command=servicos, font='Consolas 14 bold', bg="#FFFF00")
servicos.place(relx=1.0, rely=1.0, anchor='se', x=-275, y=-15)

central_atendimento = Button(janela, text="Contato", command=central_atendimento, font='Consolas 14 bold', bg="#FFFF00")
central_atendimento.place(relx=1.0, rely=1.0, anchor='se', x=-160, y=-15)

blog = Button(janela, text="Nosso blog", command=blog, font='Consolas 14 bold', bg="#FFFF00")
blog.place(relx=1.0, rely=1.0, anchor='se', x=-16, y=-15)

janela.mainloop()

- ## Captura de Tela

Aqui está uma imagem do projeto em execução:

![sistemasbr1](https://i.postimg.cc/QdFKk78k/image.png)

## Banco de Dados Sistemas.br

### Visão Geral

O projeto "Banco de Dados Sistemas.br" demonstra a estrutura e a funcionalidade de um banco de dados relacional, simulando a operação de uma maquininha de vendas. A implementação abrange o gerenciamento de clientes, transações e vendas, ilustrando como esses componentes interagem com os dados.

### Estrutura do Banco de Dados

O banco de dados é composto por três tabelas principais:

1. **Cliente**
   - Armazena informações dos clientes, incluindo nome e CPF.
   - **Campos**:
     - `id_cliente` 
     - `nome` 
     - `cpf` 

   ```sql
   CREATE TABLE Cliente (
       id_cliente INT IDENTITY(1,1) PRIMARY KEY,
       nome VARCHAR(50),
       cpf VARCHAR(11)
   );

   INSERT INTO Cliente (nome, cpf)
   VALUES 
   ('Reinaldo Henrique', '98374617283'),
   ('Cleber Machado', '73647182938'),
   ('Luiz Rocha', '81736472634'),
   ('Felipe Soares', '15374881723'),
   ('Julia Lisboa', '88736172334');

   CREATE TABLE Transacao (
    id_transacao INT IDENTITY(1,1) PRIMARY KEY,
    metodo VARCHAR(20),
    data_transacao DATE,
    valor DECIMAL(10, 2)
   );

2. **Transações**
   - Registra as transações realizadas, com detalhes sobre o método de pagamento, data e valor.
   - **Campos**:
     - `transacao` 
     - `metodo` 
     - `data_transacao` 
     - `valor` 

   ```sql
   CREATE TABLE Transacao (
       id_transacao INT IDENTITY(1,1) PRIMARY KEY,
       metodo VARCHAR(20),
       data_transacao DATE,
       valor DECIMAL(10, 2)
   );

   INSERT INTO Transacao (metodo, data_transacao, valor)
   VALUES
   ('Crédito', '2024-11-19', 339.90),
   ('Crédito', '2024-06-21', 109.99),
   ('Débito', '2024-07-05', 619.89),
   ('Pix', '2023-01-11', 14.00),
   ('Dinheiro', '2024-08-31', 50.00)

3. **Vendas**
   - Relaciona os clientes com as transações realizadas.
   - **Campos**:
     - `id_vendas` 
     - `id_cliente` 
     - `id_transacao` 

   ```sql
   CREATE TABLE Vendas (
    id_vendas INT IDENTITY(1,1) PRIMARY KEY,
    id_cliente INT,
    id_transacao INT,
    FOREIGN KEY (id_cliente) REFERENCES Cliente(id_cliente),
    FOREIGN KEY (id_transacao) REFERENCES Transacao(id_transacao)
   );

   INSERT INTO Vendas (id_cliente, id_transacao)
   VALUES
   (1, 1),
   (2, 2),
   (3, 3),
   (4, 4),
   (5, 5);
   
Aqui está uma imagem do projeto em execução:

![sistemasbr2](https://i.postimg.cc/650ssWkS/image.png)
![sistemasbr3](https://i.postimg.cc/PqNnzgF7/image.png)
![sistemasbr4](https://i.postimg.cc/bvYwXVV0/image.png)
