# Modelo de Domínio

## Produto

### Descrição

Representa uma mercadoria comercializada pelo estabelecimento.

### Atributos

- id;
- codigo_barras;
- nome;
- descricao;
- preco_custo;
- preco_venda;
- quantidade_estoque;
- estoque_minimo;
- unidade_medida;
- vendido_por_peso;
- ativo.

### Responsabilidades

- armazenar os dados do produto;
- informar o preço de custo;
- informar o preço de venda;
- indicar a quantidade disponível em estoque;
- indicar quando o estoque estiver abaixo do mínimo;
- indicar se o produto é vendido por unidade ou por peso;
- controlar se o produto está ativo para novas compras e vendas.

### Relacionamentos

- pertence a uma Categoria;
- pode estar associado a vários Fornecedores;
- pode participar de vários Itens de Compra;
- pode participar de vários Itens de Venda;
- possui várias Movimentações de Estoque.

---

## Categoria

### Descrição

Representa uma classificação utilizada para organizar os produtos do estabelecimento.

Exemplos:

- bebidas;
- alimentos;
- produtos de limpeza;
- higiene pessoal;
- frios;
- doces.

### Atributos

- id;
- nome;
- descricao;
- ativo.

### Responsabilidades

- armazenar os dados da categoria;
- permitir a organização dos produtos;
- facilitar consultas e relatórios;
- controlar se a categoria está disponível para novos produtos.

### Relacionamentos

- pode possuir vários Produtos;
- cada Produto pertence a uma Categoria.

---

## Fornecedor

### Descrição

Representa uma pessoa ou empresa responsável pelo fornecimento de produtos ao estabelecimento.

### Atributos

- id
- nome
- cpf_cnpj
- telefone
- observacoes
- ativo

### Responsabilidades

- armazenar os dados do fornecedor;
- permitir sua associação às compras;
- permitir a consulta do histórico de fornecimento;
- controlar se o fornecedor está disponível para novas compras.

### Relacionamentos

- pode fornecer vários Produtos;
- pode estar associado a várias Compras;
- uma Compra pertence a um Fornecedor.

### Decisões de Modelagem

> **NOTA:** O modelo inicial previa atributos adicionais para a classe Fornecedor, como nome fantasia, endereço e e-mail. Entretanto, durante o desenvolvimento do sistema e a análise do funcionamento do Mercadinho Caparaó, verificou-se que essas informações não são utilizadas na operação diária do estabelecimento. Para manter o modelo do MVP consistente com a realidade do negócio e evitar o cadastro de dados desnecessários, a classe foi simplificada para conter apenas os atributos efetivamente utilizados: nome, CPF/CNPJ, telefone, observações e status.

---

## Compra

### Descrição

Representa uma aquisição de mercadorias realizada pelo estabelecimento junto a um fornecedor.

### Atributos

- id;
- data_hora;
- numero_documento;
- valor_total;
- observacoes;
- status.

### Responsabilidades

- armazenar os dados da compra;
- manter a lista de produtos adquiridos;
- calcular o valor total da compra;
- associar a compra a um fornecedor;
- atualizar o estoque após sua conclusão;
- preservar o histórico de compras realizadas.

### Relacionamentos

- pertence a um Fornecedor;
- possui um ou vários Itens de Compra;
- gera uma ou várias Movimentações de Estoque;
- é registrada por um Usuário.

---

## Item de Compra

### Descrição

Representa um produto específico incluído em uma compra.

A entidade é necessária porque cada produto de uma compra possui informações próprias, como quantidade, preço de aquisição e subtotal.

### Atributos

- id;
- quantidade;
- preco_unitario;
- subtotal.

### Responsabilidades

- armazenar a quantidade adquirida de um produto;
- armazenar o preço de compra praticado na transação;
- calcular o subtotal do item;
- associar um produto a uma compra.

### Relacionamentos

- pertence a uma Compra;
- referencia um Produto;
- uma Compra possui um ou vários Itens de Compra;
- um Produto pode participar de vários Itens de Compra.

---

## Cliente

### Descrição

Representa uma pessoa que realiza compras no estabelecimento e que poderá ser identificada para consultas de histórico ou realização de compras a prazo.

O cadastro do cliente não será obrigatório para vendas comuns, mas será obrigatório para vendas realizadas a prazo.

### Atributos

- id;
- nome;
- cpf;
- telefone;
- endereco;
- observacoes;
- ativo.

### Responsabilidades

- armazenar os dados do cliente;
- permitir a associação do cliente às vendas;
- permitir a consulta do histórico de compras;
- permitir a consulta dos débitos pendentes;
- identificar clientes autorizados a comprar a prazo.

### Relacionamentos

- pode possuir várias Vendas;
- pode possuir vários Débitos;
- pode realizar vários Pagamentos de Débito.

---

## Venda

### Descrição

Representa uma operação de venda realizada pelo estabelecimento.

### Atributos

- id;
- data_hora;
- valor_bruto;
- desconto;
- valor_total;
- status;
- observacoes;
- data_hora_cancelamento;
- motivo_cancelamento.

### Responsabilidades

- armazenar os dados da venda;
- manter os produtos adicionados;
- calcular o valor bruto;
- aplicar descontos;
- calcular o valor total;
- registrar as formas de pagamento utilizadas;
- reduzir o estoque após sua conclusão;
- permitir o cancelamento;
- permitir a emissão de comprovante.

### Relacionamentos

- possui um ou vários Itens de Venda;
- possui um ou vários Pagamentos;
- pode estar associada a um Cliente;
- está associada a um Caixa;
- gera várias Movimentações de Estoque;
- gera uma ou várias Movimentações de Caixa;
- pode gerar um Débito;
- é registrada por um Usuário.

---

## Item de Venda

### Descrição

Representa um produto específico incluído em uma venda.

Essa entidade preserva as informações da transação, mesmo que o preço do produto seja alterado posteriormente.

### Atributos

- id;
- quantidade;
- preco_unitario;
- desconto;
- subtotal.

### Responsabilidades

- armazenar a quantidade vendida;
- armazenar o preço praticado no momento da venda;
- armazenar eventual desconto aplicado ao item;
- calcular o subtotal;
- associar um produto a uma venda.

### Relacionamentos

- pertence a uma Venda;
- referencia um Produto;
- uma Venda possui um ou vários Itens de Venda;
- um Produto pode participar de vários Itens de Venda.

---

## Pagamento

### Descrição

Representa um valor utilizado para pagar uma venda.

Uma venda poderá possuir vários pagamentos quando forem utilizadas diferentes formas de pagamento.

### Atributos

- id;
- data_hora;
- forma_pagamento;
- valor;
- status;
- observacoes.

### Formas de pagamento possíveis

- dinheiro;
- Pix;
- cartão de débito;
- cartão de crédito;
- pagamento a prazo.

### Responsabilidades

- armazenar a forma de pagamento utilizada;
- armazenar o valor pago;
- permitir pagamentos divididos;
- permitir o cálculo do valor restante;
- informar quando o pagamento da venda estiver completo;
- gerar a movimentação financeira correspondente.

### Relacionamentos

- pertence a uma Venda;
- está associado a um Caixa;
- gera uma Movimentação de Caixa;
- pode estar relacionado a um Cliente quando representar pagamento de débito.

---

## Débito

### Descrição

Representa um valor devido por um cliente em decorrência de uma venda realizada a prazo.

### Atributos

- id;
- data_criacao;
- valor_original;
- valor_pago;
- saldo_devedor;
- data_vencimento;
- status;
- observacoes.

### Status possíveis

- pendente;
- parcialmente pago;
- quitado;
- cancelado.

### Responsabilidades

- armazenar o valor original da dívida;
- controlar os pagamentos realizados;
- calcular o saldo devedor;
- indicar se o débito está pendente, parcialmente pago ou quitado;
- preservar o histórico das compras realizadas a prazo.

### Relacionamentos

- pertence a um Cliente;
- é originado por uma Venda;
- pode possuir vários Pagamentos de Débito.

---

## Pagamento de Débito

### Descrição

Representa um pagamento total ou parcial realizado por um cliente para reduzir um débito existente.

### Atributos

- id;
- data_hora;
- valor;
- forma_pagamento;
- observacoes.

### Responsabilidades

- registrar o valor recebido;
- reduzir o saldo devedor;
- permitir pagamentos parciais;
- registrar a entrada financeira no caixa;
- preservar o histórico de pagamentos do cliente.

### Relacionamentos

- pertence a um Débito;
- é realizado por um Cliente;
- está associado a um Caixa;
- gera uma Movimentação de Caixa;
- é registrado por um Usuário.

---

## Caixa

### Descrição

Representa um período de funcionamento financeiro do ponto de venda, iniciado pela abertura e encerrado pelo fechamento.

### Atributos

- id;
- data_hora_abertura;
- data_hora_fechamento;
- valor_inicial;
- valor_esperado;
- valor_contado;
- diferenca;
- status;
- observacoes_abertura;
- observacoes_fechamento.

### Status possíveis

- aberto;
- fechado.

### Responsabilidades

- controlar a abertura do caixa;
- controlar o fechamento do caixa;
- armazenar o valor inicial;
- receber movimentações financeiras;
- calcular o saldo esperado;
- calcular possíveis diferenças no fechamento;
- impedir novas vendas quando estiver fechado;
- fornecer um resumo financeiro do período.

### Relacionamentos

- possui várias Vendas;
- possui vários Pagamentos;
- possui várias Movimentações de Caixa;
- possui várias Sangrias;
- é aberto e fechado por um Usuário.

---

## Movimentação de Caixa

### Descrição

Representa qualquer entrada ou saída financeira registrada durante o período de funcionamento do caixa.

### Atributos

- id;
- data_hora;
- tipo;
- categoria;
- descricao;
- valor;
- forma_pagamento;
- observacoes.

### Tipos possíveis

- entrada;
- saída.

### Categorias possíveis

- venda;
- recebimento de débito;
- sangria;
- despesa;
- suprimento;
- estorno;
- outra movimentação.

### Responsabilidades

- registrar entradas financeiras;
- registrar saídas financeiras;
- identificar a origem da movimentação;
- permitir o cálculo do saldo do caixa;
- manter o histórico financeiro;
- permitir a geração de relatórios.

### Relacionamentos

- pertence a um Caixa;
- pode ser originada por uma Venda;
- pode ser originada por um Pagamento;
- pode ser originada por um Pagamento de Débito;
- pode ser originada por uma Sangria;
- é registrada por um Usuário.

---

## Sangria

### Descrição

Representa uma retirada de dinheiro em espécie do caixa durante o expediente.

### Atributos

- id;
- data_hora;
- valor;
- motivo;
- observacoes.

### Responsabilidades

- registrar uma retirada de dinheiro;
- reduzir o saldo disponível em espécie;
- armazenar o motivo da retirada;
- manter o histórico de sangrias realizadas.

### Relacionamentos

- pertence a um Caixa;
- gera uma Movimentação de Caixa;
- é registrada por um Usuário.

---

## Movimentação de Estoque

### Descrição

Representa qualquer alteração ocorrida na quantidade disponível de um produto.

### Atributos

- id;
- data_hora;
- tipo;
- quantidade;
- quantidade_anterior;
- quantidade_posterior;
- motivo;
- observacoes.

### Tipos possíveis

- entrada por compra;
- saída por venda;
- entrada por cancelamento de venda;
- perda;
- ajuste de entrada;
- ajuste de saída;
- devolução;
- outra movimentação.

### Responsabilidades

- registrar alterações no estoque;
- identificar o tipo da movimentação;
- armazenar a quantidade anterior;
- armazenar a quantidade movimentada;
- armazenar a quantidade resultante;
- preservar o histórico de estoque;
- permitir o rastreamento da origem de diferenças.

### Relacionamentos

- pertence a um Produto;
- pode ser originada por uma Compra;
- pode ser originada por uma Venda;
- pode ser originada por uma perda ou ajuste;
- é registrada por um Usuário.

---

## Usuário

### Descrição

Representa uma pessoa autorizada a acessar e utilizar o sistema.

### Atributos

- id;
- nome;
- nome_usuario;
- senha;
- perfil;
- ativo.

### Perfis possíveis

- administrador;
- operador do caixa.

### Responsabilidades

- permitir a autenticação no sistema;
- controlar o acesso às funcionalidades;
- identificar quem realizou cada operação;
- impedir o acesso de usuários desativados;
- preservar a rastreabilidade das operações.

### Relacionamentos

- pode registrar várias Compras;
- pode registrar várias Vendas;
- pode abrir e fechar vários Caixas;
- pode registrar Movimentações de Estoque;
- pode registrar Movimentações de Caixa;
- pode registrar Sangrias;
- pode registrar Pagamentos de Débito.

---