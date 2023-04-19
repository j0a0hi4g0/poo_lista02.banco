class Conta:
    def __init__(self, agencia, numero):
        self.agencia = agencia
        self.histo = []
        self.limite = 1000
        self.saldo = 0
        self.numero = numero


    print("=-" * 12)
    print("SISTEMA BANCÁRIO:")


    def saque(self, quantia):
        print("=-" * 10)
        print("SAQUE")
        if quantia > (self.saldo + self.limite):
            print("saldo insuficiente.")
            return
        if quantia < 0:
            print("não é possível sacar valores negativos.")
            return
        self.saldo -= quantia
        self.histo.append(("Saque", quantia))


   
    
    def deposito(self, quantia):
        print("=-" * 10)
        print("DEPÓSITO")
        if quantia < 0:
            print('impossível depositar valores negativos.')
            return
        self.saldo += quantia
        self.histo.append(("Depósito", quantia))


    def verificar_saldo(self):
        print("=-" * 10)
        print("SALDO")
        print(f" R${self.saldo:.2f}")

    
    
    def transferir(self, quantia, outra_conta):
        print("=-" * 10)
        print("TRANSFERIR")
        if quantia > self.saldo:
            print("saldo insuficiente.")
            return
        if quantia < 0:
            print("não é possível transferir valores negativos.")
            return
        self.saldo -= quantia
        outra_conta.saldo += quantia
        self.histo.append(("Transferência", quantia, outra_conta.numero))


    def verificar_extrato(self):
        print("=-" * 10)
        print("EXTRATO")
        print("Seu extrato - ")
        for operacao in self.histo:
            if operacao[0] == "Transferência":
                print(f"- {operacao[0]} de R${operacao[1]:.2f} para a conta {operacao[2]}")
            else:
                print(f"- {operacao[0]} de R${operacao[1]:.2f}")

    def encerrar_conta(self):
        print("=-" * 10)
        print("ENCERRAR CONTA")
        if self.saldo != 0:
            print("sua conta não está negativada. Por isso, não é possível encerra-la.")
            return
        print("Conta encerrada.")

