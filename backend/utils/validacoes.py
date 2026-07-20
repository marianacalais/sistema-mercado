def validar_nome(nome):
    # Verifica se o nome é uma string e se ela não está vazia, caso contrário retorna um erro

    if not isinstance(nome, str):
        raise TypeError("Seu nome deve ser uma string")
    
    nome = ' '.join(
        palavra.capitalize()
        for palavra in nome.split()
        )

    if not (nome):
        raise ValueError("Seu nome não pode estar vazio")

    return nome


def validar_descricao(descricao):
    # Transforma a descrição em uma string diferente de espaços, ou uma string vazia
    
    if descricao is None:
        descricao = ''
        
    descricao = str(descricao).strip()

    return descricao


def validar_codigo_barras(codigo_barras):
    # Verifica se o código de barras é uma string que possui somente números
    
    if not isinstance(codigo_barras, str):
        raise TypeError("O código de barras deve ser uma string")

    codigo_barras = codigo_barras.strip()

    if not codigo_barras:
        raise ValueError("O código de barras não pode estar vazio")

    if not codigo_barras.isnumeric():
        raise ValueError("O código de barras deve apresentar somente números")

    return codigo_barras


def validar_telefone(telefone):

    if not isinstance(telefone, str):
        raise TypeError("O número de telefone deve ser uma string")
    
    telefone = telefone.strip()

    if not telefone.isnumeric():
        raise ValueError("O número de telefone deve conter apenas números")
    
    if len(telefone) != 11:
        raise ValueError("O telefone deve conter 11 dígitos")
    
    return telefone


def validar_observacao(observacao):

    if not isinstance(observacao, str):
        raise TypeError("A observação deve ser uma string")
    
    observacao = observacao.strip()

    if not observacao:
        raise ValueError("A observação não pode ser uma string vazia")
    
    return observacao

def validar_cpf_cnpj(cpf_cnpj):
    if not isinstance(cpf_cnpj, str):
        raise TypeError("O CPF ou CNPJ deve ser uma string")
    
    cpf_cnpj = cpf_cnpj.strip()

    if not cpf_cnpj.isnumeric():
        raise ValueError("O CPF ou CNPJ deve conter apenas números")
    
    if len(cpf_cnpj) != 11 and len(cpf_cnpj) != 14:
        raise ValueError("O CPF ou CNPJ deve conter 11 ou 14 dígitos")
    
    return cpf_cnpj