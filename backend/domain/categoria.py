from backend.utils.validacoes import validar_nome
from backend.utils.validacoes import validar_descricao

class Categoria:
    categorias = []

    def __init__(self, nome, descricao=''):
        self.id = None
        self.nome = nome
        self.descricao = descricao
        self._ativo = True


    def __str__(self):
            
            return (
                f'Categoria: {self.nome}\n'
                f'Descrição: {self.descricao}\n' if self.descricao else ''
                f'Está Ativo? {"Sim" if self.ativo else "Não"}\n \n'
            )


    @property
    def ativo(self):
        return self._ativo
    
    @ativo.setter
    def ativo(self, status: bool):
        if not isinstance(status, bool):
            raise TypeError("Esse status é inválido")
        
        self._ativo = status


    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome: str):

        nome = validar_nome(nome)
    
        if nome.isnumeric():
            raise ValueError("Seu nome não pode conter apenas números")

        self._nome = nome


    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, descricao):
        
        descricao = validar_descricao(descricao)
        self._descricao = descricao


    def desativar(self):
        self.ativo = False

    def ativar(self):
        self.ativo = True

    def salvar(self):
        for categoria in self.categorias:
            if self.nome.casefold() == categoria.nome.casefold():
                raise ValueError("A categoria já existe")
        
        self.categorias.append(self)


    @classmethod
    def listar(cls):
        return cls.categorias.copy()
