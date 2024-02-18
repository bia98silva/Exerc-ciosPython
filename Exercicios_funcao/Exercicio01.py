
def main():
    lista = []
    tam = int(input("Digite o tamanho da lista: "))
    carregar_lista(lista, tam)
    print(f"A soma dos impares da lista é {media_impares(lista)}")
    print(f"O indice do numero buscado na lista é {buscar_numero(lista, tam)}")


def carregar_lista(lista, tam):
    for i in range(tam):
        lista.append(int(input("Digite um elemento da lista: ")))

def buscar_numero(lista,tam):
    busca = int(input("Digite o numero que deseja buscar na lista: "))
    if busca in lista:
        elemento = lista.index(busca)
    else:
        elemento = -1
    return elemento


def media_impares(lista):
    soma = 0
    for i in range(len(lista)):
        if lista[i] % 2 != 0:
            soma += lista[i]
    return soma

if __name__ == "__main__":
    main()