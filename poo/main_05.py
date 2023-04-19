from conta import *

#criando contas
conta01 = Conta("387", "23972")
conta02 = Conta("456", "53321")

conta01.verificar_saldo()  
conta02.verificar_saldo()  

conta01.deposito(3000)

conta01.saque(200)

conta01.verificar_saldo()




#ALGUMAS MELHORIAS:
# - Solicitação de empréstimos e financiamentos.
# - Depósitos em contas correntes ou de poupança.




















