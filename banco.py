#BANCO - CONTA CORRENTE E SAQUE
from ast import Break

#INÍCIO
p = "-" * 20
print(p)
print("BANCO ULTRA")
print(p)

#VARIÁVEIS
saldo1 = 1250
cont = 0

#FUNÇÕES
def saque():
    global saldo1
    saque1 = float(input("VALOR DO SAQUE: "))
    
    if saque1 > saldo1:
        print("VALOR MÁXIMO PARA SAQUE DE: ", saldo1)
        return chamaFuncao
    
    saldo1 -= saque1
    if saque1 <= saldo1:
        print("SAQUE REALIZADO!")
        return menuSaque()

def saldo():
    print("SEU SALDO É DE: ", saldo1)
    print(p)
    return menuSaldo()

def menuSaque():
    a = int(input("PARA CONSULTAR SEU NOVO SALDO: DIGITE 1 \n" "PARA VOLTAR AO INÍCIO: DIGITE 2 \n"))
    print(p)
    if a == 1:
        print("SEU NOVO SALDO É DE:", saldo1) 
        print(p)
        return chamaFuncao()
    if a == 2:
        return chamaFuncao()
    else:
        print("Número inválido!")
        return chamaFuncao()

def menuSaldo():
    for i in range(1):
        a = int(input("PARA VOLTAR AO INÍCIO: DIGITE 1 \n" "PARA ENCERRAR O PROGRAMA: DIGITE 2 \n"))
        print(p)
        if a == 1:
            return chamaFuncao()
        if a == 2:
            break
        else:
            print("Número inválido!")
            return chamaFuncao()

def chamaFuncao():
    b = int(input("PARA CONSULTAR SEU SALDO: DIGITE 1 \n" "PARA REALIZAR UM SAQUE: DIGITE 2 \n"))
    if b == 1:
        saldo()
    if b == 2:
        saque()
    else:
        print("Número inválido!")
        return chamaFuncao()
        
#CHAMANDO AS FUNÇÕES
chamaFuncao()
