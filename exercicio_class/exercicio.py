class ContaBancaria:
    def __init__(self, numero_conta, titular_conta):
        self.numero_conta = numero_conta
        self.titular_conta = titular_conta
        self.saldo = 0.0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
        else:
            print("Valor de depósito inválido. Informe um valor positivo.")

    def sacar(self, valor):
        if valor <= 0:
            print("Valor de saque inválido. Informe um valor positivo.")
        elif valor > self.saldo:
            print("Saldo insuficiente para o saque.")
        else:
            self.saldo -= valor

conta = ContaBancaria(12345, "João da Silva")
print(f"Saldo inicial da conta de {conta.titular_conta}: R${conta.saldo}")

conta.depositar(1000)
print(f"Saldo após depósito: R${conta.saldo}")

conta.sacar(500)
print(f"Saldo após saque: R${conta.saldo}")
        