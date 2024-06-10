class AgendaTelefonica:
    def __init__(self):
        self.contatos = {}

    def adicionar_contato(self, nome, telefone):
        if nome in self.contatos:
            print("Um contato igual já foi adicionado na sua agenda.")
        else:
            self.contatos[nome] = telefone
            print("Contato adicionado.")

    def remover_contato(self, nome):
        if nome in self.contatos:
            del self.contatos[nome]
            print("Contato removido.")
        else:
            print("Contato não encontrado.")

    def pesquisar_contato(self, nome):
        if nome in self.contatos:
            print(f"Nome: {nome}, Telefone: {self.contatos[nome]}")
        else:
            print("Contato não encontrado.")

    def listar_contatos(self):
        if not self.contatos:
            print("Agenda vazia.")
        else:
            for nome, telefone in self.contatos.items():
                print(f"Nome: {nome}, Telefone: {telefone}")

def menu():
    agenda = AgendaTelefonica()
    while True:
        print("\n--- MENU ---")
        print("1. Adicionar Contato")
        print("2. Remover Contato")
        print("3. Pesquisar Contato")
        print("4. Listar Contatos")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone do contato: ")
            agenda.adicionar_contato(nome, telefone)
        elif opcao == "2":
            nome = input("Digite o nome do contato que deseja remover: ")
            agenda.remover_contato(nome)
        elif opcao == "3":
            nome = input("Digite o nome do contato que deseja pesquisar: ")
            agenda.pesquisar_contato(nome)
        elif opcao == "4":
            agenda.listar_contatos()
        elif opcao == "5":
            print("Obrigado por utilizar a Agenda. Até a próxíma")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    menu()
