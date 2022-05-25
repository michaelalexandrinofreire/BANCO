#BANCO - CONTA CORRENTE E SAQUE
from ast import Break
import time
from unicodedata import numeric 

#INÍCIO
p = "-" * 20
print(p)
print("BANCO ULTRA")
print(p)
saldo1 = 1200

#FUNÇÕES
def saque():
    global saldo1
    saque1 = float(input("VALOR DO SAQUE: "))
    print(p)
    if saque1 > saldo1:
        print("VALOR MÁXIMO PARA SAQUE DE: {:.2f}R$".format(saldo1))
        print(p)
        return main()
    
    if saque1 <= saldo1:
        saldo1 -= saque1
        print("SAQUE REALIZADO!")
        return menuSaque()
    else:
        print("CARACTERE INVÁLIDO.")
        print(p)
        return main()

def saldo():
    print("SEU SALDO É DE: {:.2f}R$".format(saldo1))
    print(p)
    return menuSaldo()

def menuSaque():
    a = int(input("PARA CONSULTAR SEU NOVO SALDO: DIGITE 1 \n" "PARA VOLTAR AO MENU: DIGITE 2 \n"))
    print(p)
    if a == 1:
        time.sleep(1.1)
        print("SEU NOVO SALDO É DE: {:.2f}R$".format(saldo1)) 
        print(p)
        return main()
    if a == 2:
        return main()
    else:
        print("NÚMERO INVÁLIDO")
        print(p)
        return main()
    
def menuSaldo():
    a = int(input("PARA VOLTAR AO MENU: DIGITE 1 \n" "PARA ENCERRAR O PROGRAMA: DIGITE 2 \n"))
    for i in range(1):
        if a == 1:
            print(p)
            return main()
        if a == 2:
            break
        else: 
            print("NÚMERO INVÁLIDO")
            print(p)
            return main()
        
def main():
    b = int(input("PARA CONSULTAR SEU SALDO: DIGITE 1 \n" "PARA REALIZAR UM SAQUE: DIGITE 2 \n" "PARA ENCERRAR O PROGRAMA: DIGITE 3\n"))
    for i in range(1):
        if b == 1:
            saldo()
        if b == 2:
            saque()
        if b == 3:
            break
        else:
            print("NÚMERO INVÁLIDO")
            print(p)
            return main()
        
#CHAMANDO FUNÇÃO PRINCIPAL
main()