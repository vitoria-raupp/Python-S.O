class Calculadora:
    
    # Atributos
    val_a = 0
    val_b = 0

    
    # Metodos
    def __init__(self, a, b):
        self.val_a = a
        self.val_b = b

    def soma(self):
        return (self.val_a + self.val_b)
    
    def subtracao(self):
        return (self.val_a - self.val_b )
    
    def multiplicacao(self):
        return (self.val_a * self.val_b )
    
    def divisao(self):
        return (self.val_a % self.val_b)
    

class Interface(Calculadora):

    # Atributos
    opcao = 0

    # Metodos
    def __init__(self, a, b):
        Calculadora.__init__(self, a, b)

    def menu(self):
        print("1. Somar dois numeros\n")
        print("2. Subtrair dois numeros\n")
        print("3. Multiplicar dois numeros\n")
        print("4. Dividir dois numeros\n")
        self.opcao = int(input("Qual a sua opcao? "))

        if self.opcao == 1:
            print(self.soma())
        if self.opcao == 2:
            print(self.subtracao())
        if self.opcao == 3:
            print(self.multiplicacao()) 
        if self.opcao == 4:
            print(self.divisao()) 

def main():
    a = int(input("Digite um valor: "))
    b = int(input("Digite um outro valor: "))
    
    # Instanciando um objeto do tipo interface
    i = Interface(a, b)
    i.menu()
    
#Chamar a rotina main
main()