class Conta:
    def __init__(self, usuario, cpf, senha):
        self.usuario = usuario
        self.__cpf = cpf
        self.__senha = senha
        self.saldo = 0

    def get_cpf(self):
        return self.__cpf
        
    def self_cpf(self, cpf):
        self.__cpf = cpf

    def get_senha(self):
        return self.__senha

    def self_senha(self, senha):
        self.__senha = senha

    def depositar(self, dinheiro, senha):
        if senha == self.__senha:
            self.saldo = self.saldo + dinheiro
            print('Você depositou',dinheiro,'e o saldo é',self.saldo)
        else:
            print('Senha errada!')

    def sacar(self, saque, senha):
        if senha == self.__senha:
            self.saldo = self.saldo - saque
            print('Você sacou',saque,'o saldo é',self.saldo)
        else:
            print('Senha errada')

class Conta_Admin(Conta):
    def __init__(self, usuario, cpf, senha):
        super().__init__(usuario, cpf, senha)

    def mandar_cartão(self):
        if self.saldo >= 500:
            print('Cartão aprovado')
        else:
            print('Cartão reprovado')

    def mudar_senha(self, senha):
        self.self_senha(senha)
        print(senha)





