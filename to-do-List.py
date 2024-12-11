lista = []
# Função para adicionar uma tarefa
def adicionar_tarefa():
    tarefa = input("Digite a tarefa a adicionar: ")
    lista.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada.")

# Função para ver as tarefas
def ver_tarefas():  
    if lista:
        print("\nTarefas pendentes:")
        for idx, tarefa in enumerate(lista, start=1):
            print(f"{idx}. {tarefa}")
    else:
        print("Nenhuma tarefa pendente.")

# Função para excluir uma tarefa
def excluir_tarefa():
    if lista:
        print("\nTarefas:")
        for idx, tarefa in enumerate(lista, start=1):
            print(f"{idx}. {tarefa}")
        try:
            excluir = int(input("Digite o número da tarefa a excluir: ")) - 1
            if 0 <= excluir < len(lista):
                excluída = lista.pop(excluir)
                print(f"Tarefa '{excluída}' excluída.")
            else:
                print("Número inválido.")
        except ValueError:
            print("Por favor, digite um número válido.")
    else:
        print("Nenhuma tarefa para excluir.")

# Função para marcar tarefa como concluída
def concluir_tarefa():
    if lista:
        print("\nTarefas:")
        for idx, tarefa in enumerate(lista, start=1):
            print(f"{idx}. {tarefa}")
        try:
            concluir = int(input("Digite o número da tarefa concluída: ")) - 1
            if 0 <= concluir < len(lista):
                concluída = lista[concluir]
                print(f"Tarefa '{concluída}' marcada como concluída.")
                lista[concluir] = concluída + " (concluída)"
            else:
                print("Número inválido.")
        except ValueError:
            print("Por favor, digite um número válido.")
    else:
        print("Nenhuma tarefa para marcar como concluída.")

# Função principal para gerenciar as opções
def menu():
    print("Bem-vindo à sua to-do list \nDigite:")
    print("[1] Adicionar tarefa")
    print("[2] Ver tarefas")
    print("[3] Excluir tarefa")
    print("[4] Marcar como concluído")
    print("[5] Sair")

    while True:
        valor = input("Digite um valor: ")

        if valor == '1':
            adicionar_tarefa()
        elif valor == '2':
            ver_tarefas()
        elif valor == '3':
            excluir_tarefa()
        elif valor == '4':
            concluir_tarefa()
        elif valor == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Chama o menu para iniciar o programa
menu()" \
        ""




