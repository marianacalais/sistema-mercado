from backend.domain.categoria import Categoria
from backend.domain.produto import Produto

def limpar_dados():
    Categoria.categorias.clear()
    Produto.produtos.clear()


def criar_categoria():
    categoria = Categoria(
        nome="Alimentos",
        descricao="Produtos alimentícios"
    )
    categoria.salvar()

    return categoria


def criar_produto(categoria, codigo_barras="0789123456789"):
    return Produto(
        codigo_barras=codigo_barras,
        nome="Arroz 5 kg",
        categoria=categoria,
        preco_custo=20.00,
        preco_venda=27.50,
        unidade_medida="UN",
        estoque_minimo=5,
        descricao="Pacote de arroz de 5 kg"
    )


def testar_criacao_produto_valido():
    limpar_dados()
    categoria = criar_categoria()

    produto = criar_produto(categoria)

    passou = (
        produto.codigo_barras == "0789123456789"
        and produto.nome == "Arroz 5 kg"
        and produto.categoria is categoria
        and produto.preco_custo == 20.00
        and produto.preco_venda == 27.50
        and produto.quantidade_estoque == 0
        and produto.estoque_minimo == 5
        and produto.unidade_medida == "UN"
        and produto.ativo is True
    )

    if passou:
        print("[PASSOU] Criar produto válido")
    else:
        print("[FALHOU] Criar produto válido")


def testar_codigo_barras_inteiro():
    limpar_dados()
    categoria = criar_categoria()

    try:
        Produto(
            codigo_barras=789123456789,
            nome="Arroz",
            categoria=categoria,
            preco_custo=20,
            preco_venda=27,
            unidade_medida="UN",
            estoque_minimo=5
        )

        print("[FALHOU] Código de barras inteiro")

    except TypeError:
        print("[PASSOU] Código de barras inteiro")


def testar_zero_esquerda_codigo_barras():
    limpar_dados()
    categoria = criar_categoria()

    produto = criar_produto(
        categoria=categoria,
        codigo_barras="001234567890"
    )

    passou = produto.codigo_barras == "001234567890"

    if passou:
        print("[PASSOU] Zeros à esquerda no código de barras")
    else:
        print("[FALHOU] Zeros à esquerda no código de barras")


def testar_nome_vazio():
    limpar_dados()
    categoria = criar_categoria()

    try:
        Produto(
            codigo_barras="7891234567890",
            nome="   ",
            categoria=categoria,
            preco_custo=20,
            preco_venda=27,
            unidade_medida="UN",
            estoque_minimo=5
        )

        print("[FALHOU] Nome vazio")

    except ValueError:
        print("[PASSOU] Nome vazio")


def testar_categoria_invalida():
    limpar_dados()

    try:
        Produto(
            codigo_barras="7891234567890",
            nome="Arroz",
            categoria="Alimentos",
            preco_custo=20,
            preco_venda=27,
            unidade_medida="UN",
            estoque_minimo=5
        )

        print("[FALHOU] Categoria inválida")

    except TypeError:
        print("[PASSOU] Categoria inválida")


def testar_preco_custo_negativo():
    limpar_dados()
    categoria = criar_categoria()

    try:
        Produto(
            codigo_barras="7891234567890",
            nome="Arroz",
            categoria=categoria,
            preco_custo=-20,
            preco_venda=27,
            unidade_medida="UN",
            estoque_minimo=5
        )

        print("[FALHOU] Preço de custo negativo")

    except ValueError:
        print("[PASSOU] Preço de custo negativo")


def testar_preco_venda_texto():
    limpar_dados()
    categoria = criar_categoria()

    try:
        Produto(
            codigo_barras="7891234567890",
            nome="Arroz",
            categoria=categoria,
            preco_custo=20,
            preco_venda="27.50",
            unidade_medida="UN",
            estoque_minimo=5
        )

        print("[FALHOU] Preço de venda em texto")

    except TypeError:
        print("[PASSOU] Preço de venda em texto")


def testar_unidade_medida_invalida():
    limpar_dados()
    categoria = criar_categoria()

    try:
        Produto(
            codigo_barras="7891234567890",
            nome="Arroz",
            categoria=categoria,
            preco_custo=20,
            preco_venda=27,
            unidade_medida="PACOTE",
            estoque_minimo=5
        )

        print("[FALHOU] Unidade de medida inválida")

    except ValueError:
        print("[PASSOU] Unidade de medida inválida")


def testar_normalizacao_unidade_medida():
    limpar_dados()
    categoria = criar_categoria()

    produto = Produto(
        codigo_barras="7891234567890",
        nome="Feijão",
        categoria=categoria,
        preco_custo=7,
        preco_venda=10,
        unidade_medida="  kg  ",
        estoque_minimo=3
    )

    passou = produto.unidade_medida == "KG"

    if passou:
        print("[PASSOU] Normalizar unidade de medida para maiúscula e sem espaços")
    else:
        print("[FALHOU] Normalizar unidade de medida para maiúscula e sem espaços")


def testar_quantidade_estoque_negativa():
    limpar_dados()
    categoria = criar_categoria()
    produto = criar_produto(categoria)

    try:
        produto.quantidade_estoque = -1

        print("[FALHOU] Estoque negativo")

    except ValueError:
        print("[PASSOU] Estoque negativo")


def testar_codigo_barras_duplicado():
    limpar_dados()
    categoria = criar_categoria()

    primeiro_produto = criar_produto(
        categoria,
        codigo_barras="7891234567890"
    )
    primeiro_produto.salvar()

    segundo_produto = Produto(
        codigo_barras="7891234567890",
        nome="Outro produto",
        categoria=categoria,
        preco_custo=5,
        preco_venda=8,
        unidade_medida="UN",
        estoque_minimo=2
    )

    try:
        segundo_produto.salvar()

        print("[FALHOU] Código de barras duplicado")

    except ValueError:
        print("[PASSOU] Código de barras duplicado")


def testar_localizar_pelo_codigo_barras():
    limpar_dados()
    categoria = criar_categoria()

    produto = criar_produto(
        categoria,
        codigo_barras="001234567890"
    )
    produto.salvar()

    produto_encontrado = Produto.localizar_pelo_codigo_barras(
        "001234567890"
    )

    passou = produto_encontrado is produto

    if passou:
        print("[PASSOU] Localizar produto pelo código de barras")
    else:
        print("[FALHOU] Localizar produto pelo código de barras")


def testar_localizar_pelo_nome():
    limpar_dados()
    categoria = criar_categoria()

    produto = criar_produto(categoria)
    produto.salvar()

    produto_encontrado = Produto.localizar_pelo_nome(
        "  ARROZ 5 KG  "
    )

    passou = produto_encontrado is produto

    if passou:
        print("[PASSOU] Localizar produto pelo nome")
    else:
        print("[FALHOU] Localizar produto pelo nome")


def testar_desativar_produto():
    limpar_dados()
    categoria = criar_categoria()
    produto = criar_produto(categoria)

    produto.desativar()

    if produto.ativo is False:
        print("[PASSOU] Desativar produto")
    else:
        print("[FALHOU] Desativar produto")


if __name__ == "__main__":
    testar_criacao_produto_valido()
    testar_codigo_barras_inteiro()
    testar_zero_esquerda_codigo_barras()
    testar_nome_vazio()
    testar_categoria_invalida()
    testar_preco_custo_negativo()
    testar_preco_venda_texto()
    testar_unidade_medida_invalida()
    testar_normalizacao_unidade_medida()
    testar_quantidade_estoque_negativa()
    testar_codigo_barras_duplicado()
    testar_localizar_pelo_codigo_barras()
    testar_localizar_pelo_nome()
    testar_desativar_produto()
