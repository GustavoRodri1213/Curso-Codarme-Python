class Usuario():
    quantidade = 0 #Atributo de classe
    def __init__(self,nome,email): #Construtor
        self.nome = nome
        self.email = email
        Usuario.quantidade += 1

    
    def imprime_usuario(self): #Método de instância
        print(f"{self.nome} ({self.email})")





    

