#trabalhando com threads 

'''
PROBLEMA
considere um progrmaa mulyithread onde o usuario ira determinar a qtd  de threade e qtd de vez que cada uma tgread ira executar.
'''
import time
import threading

class ThreadUsuario(threading.Thread):

    def __init__ (self, identificador, nr_vezes): #construtor classe
        threading.Thread.__init__(self)#Fazer classe rodar em uma thread
        self.identificador = identificador
        self.nr_vezes = nr_vezes

    def run(self):
        for i in range(self.nr_vezes):
            print(f"Thread {self.identificador}\nExecutando: {i+1}/{self.nr_vezes}\n")
            time.sleep(0.5)

def main():
    threads = []
    qtd_thread = int(input("Quantas Thread quer criar? "))
    
    
    for i in range(qtd_thread):
        qtd_vezes = int(input("Quantas vezes quer rodar cada thread? "))
        threads.append(ThreadUsuario(i,qtd_vezes))#add thread em uma lista para ter controle/manter historico de todas os dados enviado, como qtd vezes cada um vai ser executado
    
    for i in range(qtd_thread):
        threads[i].start()


    
main()
