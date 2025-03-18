import requests

def obter_taxas():
    """Obtém taxas de câmbio da API de câmbio aberta."""
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    try:
        resposta = requests.get(url)
        dados = resposta.json()
        return dados["rates"]
    except Exception as e:
        print("Erro ao obter taxas de câmbio:", e)
        return None

def converter_moeda(valor, moeda_origem, moeda_destino, taxas):
    """Converte um valor de uma moeda para outra com base nas taxas de câmbio."""
    if moeda_origem not in taxas or moeda_destino not in taxas:
        print("Moeda inválida.")
        return None
    taxa_conversao = taxas[moeda_destino] / taxas[moeda_origem]
    return valor * taxa_conversao

def main():
    print("Conversor de Moedas")
    taxas = obter_taxas()
    if not taxas:
        return
    
    moeda_origem = input("Digite a moeda de origem (ex: USD, EUR, BRL): ").upper()
    moeda_destino = input("Digite a moeda de destino (ex: USD, EUR, BRL): ").upper()
    valor = float(input("Digite o valor a ser convertido: "))
    
    resultado = converter_moeda(valor, moeda_origem, moeda_destino, taxas)
    if resultado:
        print(f"{valor:.2f} {moeda_origem} equivale a {resultado:.2f} {moeda_destino}")

if __name__ == "__main__":
    main()
