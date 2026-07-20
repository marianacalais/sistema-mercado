def validar_nome(nome):
    # Verifica se o nome é uma string e se ela não está vazia, caso contrário retorna um erro

    if not isinstance(nome, str):
        raise TypeError("Seu nome deve ser uma string")
    
    nome = nome.strip()

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
