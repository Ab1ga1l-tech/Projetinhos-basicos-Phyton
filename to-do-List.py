# Lista para armazenar as tarefas
tarefas = []

# Função para adicionar tarefa
def adicionar_tarefa(descricao):
    tarefa = {
        'descricao': descricao,
        'concluida': False
    }
    tarefas.append(tarefa)
    print(f"Tarefa '{descricao}' adicionada com sucesso!")

# Função para listar tarefas
def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa na lista.")
    else:
        for idx, tarefa in enumerate(tarefas, start=1):
            status = 'Concluída' if tarefa['concluida'] else 'Pendente'
            print(f"{idx}. {tarefa['descricao']} - {status}")

# Função para concluir tarefa
def concluir_tarefa(id_tarefa):
    if 0 < id_tarefa <= len(tarefas):
        tarefas[id_tarefa - 1]['concluida'] = True
        print(f"Tarefa {id_tarefa} marcada como concluída!")
    else:
        print("ID de tarefa inválido.")

# Função para remover tarefa
def remover_tarefa(id_tarefa):
    if 0 < id_tarefa <= len(tarefas):
        removed = tarefas.pop(id_tarefa - 1)
        print(f"Tarefa '{removed['descricao']}' removida!")
    else:
        print("ID de tarefa inválido.")

# Função para exibir o menu
def exibir_menu():
    print("\nEscolha uma opção:")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Concluir tarefa")
    print("4. Remover tarefa")
    print("5. Sair")

# Função principal
def main():
    while True:
        exibir_menu()
        opcao = input("Digite o número da opção: ")

        if opcao == '1':
            descricao = input("Digite a descrição da tarefa: ")
            adicionar_tarefa(descricao)
        elif opcao == '2':
            listar_tarefas()
        elif opcao == '3':
            listar_tarefas()
            try:
                id_tarefa = int(input("Digite o ID da tarefa para marcar como concluída: "))
                concluir_tarefa(id_tarefa)
            except ValueError:
                print("Por favor, insira um número válido.")
        elif opcao == '4':
            listar_tarefas()
            try:
                id_tarefa = int(input("Digite o ID da tarefa para remover: "))
                remover_tarefa(id_tarefa)
            except ValueError:
                print("Por favor, insira um número válido.")
        elif opcao == '5':
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Rodar o programa
if __name__ == "__main__":
    main()
