import os
import random

class Numeros():

    listagem = []
    quantidade = 0

    def __init__(self, quantidade) -> None:
        self.quantidade = quantidade
    
    def preencherListagem(self):
        for i in range(self.quantidade):
            self.listagem.append(random.randint(0, 999))
    
    def mostrarLista(self):
        print(self.listagem)

    def mostraPares(self):
        for i in range(self.quantidade):
            if(self.listagem[i] % 2 == 0):
                print(self.listagem[i])

    def mostraImpares(self):
        for i in range(self.quantidade):
            if(self.listagem[i] % 2 != 0):
                print(self.listagem[i])   

def main():
    n = Numeros(10)
    n.preencherListagem()
    n.mostrarLista()

    if(os.fork() == 0):
        print("- pares -")
        n.mostraPares()
    else:
        os.wait()
        if(os.fork() == 0):
            print("- impares -")
            n.mostraImpares()
        else: 
            os.wait()

main()