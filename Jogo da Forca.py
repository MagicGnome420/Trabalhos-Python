import random

def escolher_palavra():
    palavras = ["desenvolvimento", "tecnologia", "logica", "programacao", "tendencias"]
    return random.choice(palavras)

def exibir_forca(tentativas):
    estagios = [
        """
           -----
           |   |
               |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        --------
        """
    ]
    return estagios[tentativas]

def jogar():
    palavra = escolher_palavra()
    palavra_oculta = ["_"] * len(palavra)
    tentativas = 0
    letras_tentadas = []

    print("Bem-vindo ao jogo!")
    print(exibir_forca(tentativas))
    print("Palavra: " + " ".join(palavra_oculta))
    
    while True:
        letra = input("Escolha uma letra: ").lower()
        
        if letra in letras_tentadas:
            print("Você já usou essa letra.")
            continue
        else:
            letras_tentadas.append(letra)
        
        if letra in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    palavra_oculta[i] = letra
        else:
            tentativas += 1
        
        print(exibir_forca(tentativas))
        print("Palavra: " + " ".join(palavra_oculta))
        
        if "_" not in palavra_oculta:
            print("Parabéns! Voçê conseguiu acertar a palavra!")
            break
        if tentativas >= 6:
            print("Você perdeu! A palavra certa era: " + palavra)
            break

    print("Até algum dia")

jogar()
