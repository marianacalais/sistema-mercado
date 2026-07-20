from backend.utils.validacoes import validar_nome
from backend.utils.validacoes import validar_descricao
from backend.utils.validacoes import validar_codigo_barras
from backend.domain.categoria import Categoria

class Produto:
    UNIDADES_MEDIDA_POSSIVEIS = ['UN', 'KG', 'L', 'M', 'CX']
    produtos = []
    
    def __init__(self, codigo_barras: str, nome, categoria, preco_custo, preco_venda, unidade_medida, estoque_minimo, descricao=''):
        self.id = None
        self.codigo_barras = codigo_barras
        self.nome = nome
        self.categoria = categoria
        self.descricao = descricao
        self.preco_custo = preco_custo
        self.preco_venda = preco_venda
        self.unidade_medida = unidade_medida
        self.quantidade_estoque = 0
        self.estoque_minimo = estoque_minimo
        self.ativo = True

    def __str__(self):
       
        descricao = f'Descrição: {self.descricao}\n' if self.descricao else ''

        return (
            f'Produto: {self.nome}\n'
            f'{descricao}'
            f'Categoria: {self.categoria}\n'
            f'Preço de Custo: {self.preco_custo}\n'
            f'Preço de Venda: {self.preco_venda}\n'
            f'Tem no Estoque: {self.quantidade_estoque} {self.unidade_medida}\n'
            f'Está Ativo? {"Sim" if self.ativo else "Não"}\n \n'
        )


    @property
    def codigo_barras(self):
        return self._codigo_barras
    
    @codigo_barras.setter
    def codigo_barras(self, codigo_barras):
        self._codigo_barras = validar_codigo_barras(codigo_barras)


    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome: str):
        self._nome = validar_nome(nome)


    @property
    def categoria(self):
        return self._categoria
    
    @categoria.setter
    def categoria(self, categoria):
        if not isinstance(categoria, Categoria):
            raise TypeError("A categoria não pertence a classe Categoria")

        self._categoria = categoria


    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, descricao):
        self._descricao = validar_descricao(descricao)


    @property
    def preco_custo(self):
        return self._preco_custo
    
    @preco_custo.setter
    def preco_custo(self, preco):

        if isinstance(preco, bool) or not isinstance(preco, (int, float)):
            raise TypeError("O preço deve ser numérico")

        if preco < 0:
            raise ValueError("O preço de custo não pode ser negativo")
        
        self._preco_custo = preco


    @property
    def preco_venda(self):
        return self._preco_venda
    
    @preco_venda.setter
    def preco_venda(self, preco):

        if isinstance(preco, bool) or not isinstance(preco, (int, float)):
            raise TypeError("O preço deve ser numérico")

        if preco <= 0:
            raise ValueError("O preço de venda deve ser um valor positivo")
        
        self._preco_venda = preco


    @property
    def quantidade_estoque(self):
        return self._quantidade_estoque
    
    @quantidade_estoque.setter
    def quantidade_estoque(self, quant):

        if isinstance(quant, bool) or not isinstance(quant, (int, float)):
            raise TypeError("O quantidade do item no estoque deve ser numérica")

        if quant < 0:
            raise ValueError("Não podem existir quantidades negativas de um item no estoque")
        
        self._quantidade_estoque = quant
    

    @property
    def estoque_minimo(self):
        return self._estoque_minimo
    
    @estoque_minimo.setter
    def estoque_minimo(self, quant):

        if isinstance(quant, bool) or not isinstance(quant, (int, float)):
            raise TypeError("O valor de estoque mínimo deve ser numérico")

        if quant < 0:
            raise ValueError("O estoque mínimo não pode ser um valor negativo")
        
        self._estoque_minimo = quant


    @property
    def unidade_medida(self):
        return self._unidade_medida
    
    @unidade_medida.setter
    def unidade_medida(self, unidade: str):
        
        if not isinstance(unidade, str):
            raise TypeError("Unidade inválida, digite uma string")

        unidade = unidade.strip().upper()

        if unidade not in self.UNIDADES_MEDIDA_POSSIVEIS:
            raise ValueError("Essa unidade não está disponível")
        
        self._unidade_medida = unidade


    @property
    def ativo(self):
        return self._ativo
    
    @ativo.setter
    def ativo(self, status: bool):
        if not isinstance(status, bool):
            raise TypeError("Esse status é inválido")
        
        self._ativo = status

    @classmethod
    def listar(cls):
        return cls.produtos.copy()
    
    
    @classmethod
    def localizar_pelo_codigo_barras(cls, codigo_barras):

        codigo_barras = validar_codigo_barras(codigo_barras)

        for produto in cls.produtos:
            if codigo_barras == produto.codigo_barras:
                return produto
        
        raise ValueError("Esse produto não está cadastrado")


    @classmethod
    def localizar_pelo_nome(cls, nome):

        nome = validar_nome(nome)

        for produto in cls.produtos:
            if nome.casefold() == produto.nome.casefold():
                return produto
        
        raise ValueError("Esse produto não está cadastrado")


    def salvar(self):
        for produto in type(self).produtos:
            if self.codigo_barras == produto.codigo_barras:
                raise ValueError("Já existe um produto com esse código de barras")
        
        type(self).produtos.append(self)

    def desativar(self):
        self.ativo = False

    def ativar(self):
        self.ativo = True
