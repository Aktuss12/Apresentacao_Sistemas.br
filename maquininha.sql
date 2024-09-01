CREATE TABLE Cliente (
    id_cliente INT IDENTITY (1, 1) PRIMARY KEY,
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
    id_transacao INT IDENTITY (1, 1) PRIMARY KEY,
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
('Dinheiro', '2024-08-31', 50.00);

CREATE TABLE Vendas (
    id_vendas INT IDENTITY (1, 1) PRIMARY KEY,
    id_cliente INT,
    id_transacao INT,
    FOREIGN KEY (id_cliente) REFERENCES Cliente (id_cliente),
    FOREIGN KEY (id_transacao) REFERENCES Transacao (id_transacao)
);

INSERT INTO Vendas (id_cliente, id_transacao)
VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5);

SELECT * FROM Cliente
SELECT * FROM Transacao
SELECT * FROM Vendas

DROP TABLE Cliente
DROP TABLE Transacao
DROP TABLE Vendas
