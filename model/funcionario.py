class Funcionario:
    def __init__(self, nome: str, idade: int, cpf: str, totalVendas: float):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.totalVendas = totalVendas

    def __str__(self):
        return f"Funcionário -> Nome: {self.nome} (CPF: {self.cpf} | Idade: {self.idade})\nTotal de Vendas: R${self.totalVendas:.2f}"