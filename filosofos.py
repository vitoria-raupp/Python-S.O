import time
import threading
import random

#Declara recursos
garfos = []

#criar semaforos 

def criaGarfos():
    for i in range(5):
        garfos.append(threading.Semaphore(1))

# Ações dos filosofos 
def comer (id):
    print(f'Filosofo {id} comendo ...')
    time.sleep(random.randit(0,5))

def pensar(id):
    print(f'Filosofo {id} pensandon ...')
    time.sleep(random.randint(0,5))

#thread
def filosofo(id):
    while True:
        pensar(id)
        garfos[id].acquire()
        garfos[(id + 1)%5].acquire()
        comer(id)
        garfos[id].release()
        garfos[(id + 1)%5].release()

#Função principal 
def main():
    criaGarfos()
    for i in range(5):
        threading.Thread(target = filosofo, args=(1)).start()

main()