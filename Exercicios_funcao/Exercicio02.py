def main():
    notas_alunos = []
    tam = int(input("Digite o tamanho da lista: "))
    ler_notas_alunos(notas_alunos, tam)
    media = media_notas(notas_alunos)
    print(f"A média dos alunos foi: {media} ")
    print(f"Nova lista com alunos com notas acima de 7.0 ------- {nova_lista_nota}")



def ler_notas_alunos(notas_alunos, tam):
    for i in range(tam):
        notas_alunos.append(float(input("Digite a nota do aluno ")))


def media_notas(notas_alunos):
    soma = sum(notas_alunos)
    media = soma/len(notas_alunos)
    return media


def nova_lista(notas_alunos, tam):
    nova_lista_nota = []
    for nota in notas_alunos:
        if nota > 7.0:
            nova_lista_nota.append(nota)
    return nova_lista_nota


if __name__ == "__main__":
    main()