from backend.utils.validacoes import validar_nome
from backend.utils.validacoes import validar_telefone
from backend.utils.validacoes import validar_observacao
from backend.utils.validacoes import validar_cpf_cnpj

class Fornecedor:
    fornecedores = []

    def __init__(self, nome, cpf_cnpj, telefone):
        self.id = None
        self.nome = nome
        self.cpf_cnpj = cpf_cnpj
        self.telefone = telefone
        self._observacoes = []
        self.ativo = True

    def __str__(self):
        
        observacoes = '\n'.join(f'- {observacao}' for observacao in self.observacoes) if self.observacoes else '- Não tem observações'
        cpf_cnpj = f'CPF: {self.cpf_cnpj}\n' if len(self.cpf_cnpj) == 11 else f'CNPJ: {self.cpf_cnpj}\n'

        return(
            f'Fornecedor: {self.nome}\n'
            f'{cpf_cnpj}'
            f'Telefone: {self.telefone}\n'
            f'Ativo? {"Sim" if self.ativo else "Não"}\n'
            f'Observações:\n{observacoes}\n'
        )


    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = validar_nome(nome)


    @property
    def cpf_cnpj(self):
        return self._cpf_cnpj
    
    @cpf_cnpj.setter
    def cpf_cnpj(self, cpf_cnpj):
        self._cpf_cnpj = validar_cpf_cnpj(cpf_cnpj)

    
    @property
    def telefone(self):
        return self._telefone
    
    @telefone.setter
    def telefone(self, telefone):
        self._telefone = validar_telefone(telefone)

    
    @property
    def observacoes(self):
        return self._observacoes.copy()


    @property
    def ativo(self):
        return self._ativo
    
    @ativo.setter
    def ativo(self, status):

        if not isinstance(status, bool):
            raise TypeError("Esse status é inválido")
        
        self._ativo = status


    @classmethod
    def listar(cls):
        return cls.fornecedores.copy()


    def salvar(self):
        for fornecedor in type(self).fornecedores:
            if self.cpf_cnpj == fornecedor.cpf_cnpj:
                raise ValueError("Esse fornecedor já existe")
        
        type(self).fornecedores.append(self)


    def desativar(self):
        self.ativo = False

    def ativar(self):
        self.ativo = True


    def adicionar_observacao(self, observacao):
        self._observacoes.append(validar_observacao(observacao))

