import random
import os

def filho():
    print(f"Filhos {os.getpid()}")
    os.execlp("/bin/firefox", "firefox")

def main():
    id_filhos = os.fork()
    if (id_filhos > 0):
        print(f"Processo pai. meu filho eh {id_filhos}")
    elif(id_filhos == 0):
        filho()

main()
        