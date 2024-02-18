
def main():
    palavras = []
    tam = 10
    lista_de_palavras(palavras)
    print(f"A quantidade de palavras que são palindromas é: {palindromo(palavras)}")


def lista_de_palavras(palavras):
    for i in range(10):
        palavras.append(input("Digite 10 palavras: "))


def palindromo(palavras):
    cont = 0
    for palavra in palavras:
        palavra = palavra.lower()
        palavra = palavra.replace(" ", "")
        if palavra == palavra[::-1]:
            cont += 1
    return cont


if __name__ == "__main__":
    main()