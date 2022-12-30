class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto.....{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    def extrato(self):
        print("Saldo {} do titular{}".format(self.__saldo, self.__titular))
    def depositar(self,valor):
        self.__saldo += valor
    def transferir(self,valor,destino):
        self.saque(valor)
        destino.depositar(valor)
    def saque(self, valor):
        if(valor <= self.__pode_sacar(valor)):
            self.__saldo -= valor
        else: 
            print("O valo {} passou do limite".format(valor))
    
    def __pode_sacar(self,valor_a_sacar):
            valor_disponivel = (self.__saldo + self.__limite) 
            return valor_a_sacar <= valor_disponivel
        
     
    # era get_limite
    @property
    def saldo(self):
        return self.__saldo
    # era get_limite
    @property
    def titular(self):
        return self.__titular
    # era get_limite
    @property
    def limite(self):
        return self.__limite
    #era set_limite
    @limite.setter
    def limite(self, limite):
        self.__limite = limite
    @staticmethod
    def codigos_bancos():
        return {'BB':'001','CAIXA':'104'}

    
    