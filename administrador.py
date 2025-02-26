from usuario import Usuario

class Administrador(Usuario):

    def imprime_usuario(self): #Método de Instância
        print(f"{self.nome} ({self.email}) - Administrador")


