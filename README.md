# Apresentação Sistemas.br

Este repositório contém o projeto "Apresentação Sistemas.br"

## Funcionalidades

- **Apresentação Interativa**: Demonstração de sistemas e banco de dados com uma interface intuitiva e responsiva que leva para cada parte desejada do site Sistemas.br
- **Design Moderno**: Layout atraente que facilita a navegação e a compreensão dos conteúdos

## Tecnologias Utilizadas

- **Linguagem**: [Python]
- **Ferramentas de Desenvolvimento**: [VSCode]
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
