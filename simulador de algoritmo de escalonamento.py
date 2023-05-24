# simulador de algoritmo de escalonamento de processos usando threads

import threading
import time 
import random

class Processo:  # classe que representa o processo
    def __init__(self, id, chegada, cpu):
        self.id = id
        self.chegada = chegada
        self.cpu = cpu
    
    def get_cpu(self):
        return self.cpu
    
    def get_chegada(self):
        return self.chegada
    
    def get_id(self):
        return self.id
    
class FilaAptos: # classe que representa a fila de aptos 
    listaProcessos = [] 

    def __init__(self):
        pass

    def insere_processo(self, processo):
        self.listaProcessos.append(processo)
    
    def mostra_dado_processo(self, posicao):
        print(f'Identificação: {self.listaProcessos[posicao].get_id()}')
        print(f'Chegada......: {self.listaProcessos[posicao].get_chegada()}')
        print(f'CPU..........: {self.listaProcessos[posicao].get_cpu()}')

    def get_proximo_processo(self):
        return self.listaProcessos.pop(0)

    def mostra_processo_lista(self):
        for i in range(len(self.listaProcessos)):
            self.mostra_dado_processo(i)

    def tamanho_lista(self):
        return len(self.listaProcessos.count())
    
    def ordenar_por_cpu(self):
        self.listaProcessos = sorted(self.listaProcessos, key=lambda Processo:Processo.cpu)
    
#Thread algoritimo FCFS
class threadFCFS(threading.Thread):

    tempo_relogio = 0
    media = 0.0

    def __init__(self, fila_aptos):
        self.fila_aptos = fila_aptos
        threading.Thread.__init__(self)

    def escalonar(self):
        #i = 0
        qtd_processos = self.fila_aptos.tamanho_lista()
        
        for i in range(self.fila_aptos.tamanho_lista()):
            proc = self.fila_aptos.get_proximo_processo()
            self.tempo_relogio += proc.get_cpu()
        
        
        media = (self.tempo_relogio - proc.get_cpu()) / qtd_processos

        return media 
        
    def run(self): 
        print('Algoritmo FSFC')
        print(f'Media de espera: {self.escalonar()}')

#Thread algoritimo SJF
class threadSJF(threading.Thread):

    tempo_relogio = 0
    media = 0.0

    def __init__(self, fila_aptos):
        self.fila_aptos = fila_aptos
        threading.Thread.__init__(self)

    def escalonar(self):
        self.fila_aptos.ordenar_por_cpu()
        qtd_processos = self.fila_aptos.tamanho_lista()
        
        for i in range(self.fila_aptos.tamanho_lista()):
            proc = self.fila_aptos.get_proximo_processo()
            self.tempo_relogio += proc.get_cpu()
        
        
        media = (self.tempo_relogio - proc.get_cpu()) / qtd_processos

        return media 

#funcao principal
def main():
    p1 = Processo(1,0,24)
    p2 = Processo(2,0,3)
    p3 = Processo(3,0,3)

    f_aptos = FilaAptos()
    f_aptos.insere_processo(p1)
    f_aptos.insere_processo(p2)
    f_aptos.insere_processo(p3)

    f_aptos.mostra_processo_lista()

    fcfs = threadFCFS(f_aptos)
    fcfs.start()
    fcfs.join()

    sjf = threadSJF(f_aptos)
    sjf.start()
    sjf.join()

main()