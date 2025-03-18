import random
import string

def generate_password(length=12, use_digits=True, use_special_chars=True):
    """Gera uma senha aleatória conforme as preferências do usuário."""
    chars = string.ascii_letters  # Letras maiúsculas e minúsculas
    if use_digits:
        chars += string.digits
    if use_special_chars:
        chars += string.punctuation
    
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    print("Gerador de Senhas Seguras")
    length = int(input("Digite o comprimento da senha desejada: "))
    use_digits = input("Incluir números? (s/n): ").strip().lower() == 's'
    use_special_chars = input("Incluir caracteres especiais? (s/n): ").strip().lower() == 's'
    
    password = generate_password(length, use_digits, use_special_chars)
    print(f"\nSenha gerada: {password}")

if __name__ == "__main__":
    main()
