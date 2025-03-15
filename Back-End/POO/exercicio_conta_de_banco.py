from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, numero_do_conta, saldo=0):
        self._agencia = agencia
        self._numero_do_conta = numero_do_conta
        self._saldo = saldo

    @abstractmethod
    def depositar(self, valor):
        pass

    @abstractmethod
    def sacar(self, valor):
        pass

    def __repr__(self):
        return f'Conta - Agencia: {self._agencia}, Número: {self._numero_do_conta}, Saldo: {self._saldo}'


class ContaPoupanca(Conta):
    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        if self._saldo < valor:
            raise ValueError('Saldo insuficiente')
        self._saldo -= valor

    def __repr__(self):
        return f'ContaPoupanca - Agencia: {self._agencia}, Número: {self._numero_do_conta}, Saldo: {self._saldo}'


class ContaCorrente(Conta):
    def __init__(self, agencia, numero_do_conta, saldo=0, limite_de_cheque_especial=500):
        super().__init__(agencia, numero_do_conta, saldo)
        self._limite_de_cheque_especial = limite_de_cheque_especial

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        if self._saldo - valor < -self._limite_de_cheque_especial:
            raise ValueError('Você atingiu o limite de cheque especial')
        self._saldo -= valor

    def __repr__(self):
        return f'ContaCorrente - Agencia: {self._agencia}, Número: {self._numero_do_conta}, Saldo: {self._saldo}, Limite de Cheque Especial: {self._limite_de_cheque_especial}'


class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        self._idade = idade

    def __repr__(self):
        return f'Pessoa(nome={self._nome}, idade={self._idade})'


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self._contas = []

    def adicionar_conta(self, conta):
        self._contas.append(conta)

    def listar_contas(self):
        return "\n".join(str(conta) for conta in self._contas)

    def depositar(self, valor, conta_index=0):
        self._contas[conta_index].depositar(valor)

    def sacar(self, valor, conta_index=0):
        self._contas[conta_index].sacar(valor)

    def __repr__(self):
        contas = "\n".join(str(conta) for conta in self._contas)
        return f'Cliente(nome={self.nome}, idade={self.idade}, Contas:\n{contas})'


class Banco:
    def __init__(self, nome_do_banco):
        self._clientes = []
        self.nome_do_banco = nome_do_banco

    def inserir_cliente(self, cliente):
        self._clientes.append(cliente)

    def listar_contas(self):
        print(f'Banco: {self.nome_do_banco}')
        for cliente in self._clientes:
            print(cliente)

    def __repr__(self):
        return f'Banco {self.nome_do_banco} com {len(self._clientes)} clientes'


# Teste do sistema
gustavo = Cliente('Gustavo', 20)
gustavo.adicionar_conta(ContaPoupanca('123', '12345678', saldo=1000))

pedro = Cliente('Pedro', 25)
pedro.adicionar_conta(ContaCorrente(
    '456', '87654321', saldo=500, limite_de_cheque_especial=1000))
pedro.adicionar_conta(ContaPoupanca('456', '87654322', saldo=2000))

gustavo.depositar(500)
pedro.depositar(1000, conta_index=1)  # Deposita na conta poupança

bradesco = Banco('Bradesco')
bradesco.inserir_cliente(gustavo)
bradesco.inserir_cliente(pedro)

bradesco.listar_contas()
