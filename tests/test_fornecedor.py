from backend.domain.fornecedor import Fornecedor


def limpar_fornecedores():
    Fornecedor.fornecedores.clear()


def test_criar_fornecedor():
    print("=== Criando fornecedor ===")

    fornecedor = Fornecedor(
        "Moises Silva",
        "52998224725",
        "31999999999"
    )

    print(fornecedor)


def test_salvar_fornecedor():
    print("\n=== Salvando fornecedor ===")

    limpar_fornecedores()

    fornecedor = Fornecedor(
        "Moises Silva",
        "52998224725",
        "31999999999"
    )

    fornecedor.salvar()

    for fornecedor in Fornecedor.listar():
        print(fornecedor)


def test_adicionar_observacao():
    print("\n=== Adicionando observação ===")

    fornecedor = Fornecedor(
        "Moises Silva",
        "52998224725",
        "31999999999"
    )

    fornecedor.adicionar_observacao("Entrega às sextas")

    print(fornecedor)


def test_ativar_desativar():
    print("\n=== Desativando fornecedor ===")

    fornecedor = Fornecedor(
        "Moises Silva",
        "52998224725",
        "31999999999"
    )

    fornecedor.desativar()
    print(fornecedor)

    print("\n=== Ativando fornecedor ===")

    fornecedor.ativar()
    print(fornecedor)


def test_fornecedor_duplicado():
    print("\n=== Testando fornecedor duplicado ===")

    limpar_fornecedores()

    fornecedor1 = Fornecedor(
        "Moises Silva",
        "52998224725",
        "31999999999"
    )

    fornecedor2 = Fornecedor(
        "Outro Nome",
        "52998224725",
        "31988888888"
    )

    fornecedor1.salvar()

    try:
        fornecedor2.salvar()

    except ValueError as erro:
        print(erro)


def test_protecao_observacoes():
    print("\n=== Testando proteção da lista de observações ===")

    fornecedor = Fornecedor(
        "Moises Silva",
        "52998224725",
        "31999999999"
    )

    fornecedor.adicionar_observacao("Entrega às sextas")

    observacoes = fornecedor.observacoes
    observacoes.append("Isso não deve aparecer")

    print(fornecedor)


if __name__ == "__main__":
    test_criar_fornecedor()
    test_salvar_fornecedor()
    test_adicionar_observacao()
    test_ativar_desativar()
    test_fornecedor_duplicado()
    test_protecao_observacoes()