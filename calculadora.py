import tkinter as tk

def somar():
    try:
        numero1 = float(num1.get())
        numero2 = float(num2.get())
        resultado.set(f"Soma: {numero1 + numero2:.2f}")
    except ValueError:
        resultado.set("Digite números válidos!")

def subtrair():
    try:
        numero1 = float(num1.get())
        numero2 = float(num2.get())
        resultado.set(f"Subtração: {numero1 - numero2:.2f}")
    except ValueError:
        resultado.set("Digite números válidos!")

def multiplicar():
    try:
        numero1 = float(num1.get())
        numero2 = float(num2.get())
        resultado.set(f"Multiplicação: {numero1 * numero2:.2f}")
    except ValueError:
        resultado.set("Digite números válidos!")

def dividir():
    try:
        numero1 = float(num1.get())
        numero2 = float(num2.get())
        if numero2 != 0:
            resultado.set(f"Divisão: {numero1 / numero2:.2f}")
        else:
            resultado.set("Não é possível dividir por zero!")
    except ValueError:
        resultado.set("Digite números válidos!")

def dobrar_valor():
    try:
        numero = float(num1.get())
        resultado.set(f"Dobro do primeiro número: {numero * 2:.2f}")
    except ValueError:
        resultado.set("Digite um número válido!")

# Criando a janela principal
janela = tk.Tk()
janela.title("Calculadora Simples")
janela.geometry("300x400")

# Label e campo de entrada para o primeiro número
tk.Label(janela, text="Digite o primeiro número:").pack()
num1 = tk.Entry(janela)
num1.pack()

# Label e campo de entrada para o segundo número
tk.Label(janela, text="Digite o segundo número:").pack()
num2 = tk.Entry(janela)
num2.pack()

# Botões para as operações
tk.Button(janela, text="Somar", command=somar).pack(pady=5)
tk.Button(janela, text="Subtrair", command=subtrair).pack(pady=5)
tk.Button(janela, text="Multiplicar", command=multiplicar).pack(pady=5)
tk.Button(janela, text="Dividir", command=dividir).pack(pady=5)
tk.Button(janela, text="Dobrar o primeiro número", command=dobrar_valor).pack(pady=5)

# Área para exibir o resultado
resultado = tk.StringVar()
tk.Label(janela, textvariable=resultado, fg="blue", font=("Arial", 14)).pack(pady=20)

# Inicia o loop da interface gráfica
janela.mainloop()
