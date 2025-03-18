def calcular_imc(peso, altura):
    """Calcula o IMC e retorna a classificação."""
    imc = peso / (altura ** 2)
    if imc < 18.5:
        classificacao = "Magreza"
    elif 18.5 <= imc < 24.9:
        classificacao = "Normal"
    elif 25 <= imc < 29.9:
        classificacao = "Sobrepeso"
    elif 30 <= imc < 34.9:
        classificacao = "Obesidade Grau 1"
    elif 35 <= imc < 39.9:
        classificacao = "Obesidade Grau 2"
    else:
        classificacao = "Obesidade Grau 3"
    
    return imc, classificacao

def main():
    print("Calculadora de IMC")
    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): "))
    
    imc, classificacao = calcular_imc(peso, altura)
    print(f"\nSeu IMC é {imc:.2f} - {classificacao}")

if __name__ == "__main__":
    main()
