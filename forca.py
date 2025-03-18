import random

def escolher_palavra():
    """Seleciona uma palavra aleatória de uma lista predefinida."""
    palavras = ["python", "desenvolvimento", "programacao", "computador", "tecnologia"]
    return random.choice(palavras)

def exibir_palavra_oculta(palavra, letras_corretas):
    """Retorna a palavra com letras descobertas e underscores para as ocultas."""
    return " ".join(letra if letra in letras_corretas else "_" for letra in palavra)

def jogo_da_forca():
    palavra = escolher_palavra()
    letras_corretas = set()
    letras_erradas = set()
    tentativas = 6
    
    print("Bem-vindo ao Jogo da Forca!")
    
    while tentativas > 0:
        print("\nPalavra:", exibir_palavra_oculta(palavra, letras_corretas))
        print("Letras erradas:", " ".join(letras_erradas))
        print(f"Tentativas restantes: {tentativas}")
        
        tentativa = input("Digite uma letra: ").lower()
        
        if tentativa in letras_corretas or tentativa in letras_erradas:
            print("Você já tentou essa letra. Escolha outra.")
            continue
        
        if tentativa in palavra:
            letras_corretas.add(tentativa)
            if set(palavra) == letras_corretas:
                print(f"Parabéns! Você acertou a palavra: {palavra}")
                return
        else:
            letras_erradas.add(tentativa)
            tentativas -= 1
    
    print(f"Game Over! A palavra era: {palavra}")

if __name__ == "__main__":
    jogo_da_forca()
