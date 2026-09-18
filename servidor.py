import numpy

def carregar_matriz(caminho_arquivo):
    try:
        matriz = numpy.loadtxt(caminho_arquivo, delimiter=';')
        return matriz
    except Exception as e:
        print(f"Erro ao carregar a matriz: {e}")
        return None


def main(argv=None):
    print("Servidor iniciado")
    M = carregar_matriz("Dados/M.csv")
    N = carregar_matriz("Dados/N.csv")
    a = carregar_matriz("Dados/a.csv")

    MN = carregar_matriz("Dados/MN.csv")
    aM = carregar_matriz("Dados/aM.csv")

    print("Matriz MN:")
    print(MN)
    print("Matriz aM:")
    print(aM)

    MN_calc = numpy.dot(M, N)
    aM_calc = numpy.dot(a, M)

    print("Matriz MN calculada:")
    print(MN_calc)
    print("Matriz aM calculada:")
    print(aM_calc)


if __name__ == "__main__":
    main()
