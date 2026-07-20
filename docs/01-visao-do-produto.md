# Visão do Produto

## Nome do Projeto

Mercadinho Caparaó

**Tipo:** Sistema de Gestão para Pequenos Mercados

## Contexto

O projeto consiste no desenvolvimento de um sistema de gestão para um mercadinho de bairro administrado por uma proprietárias e uma funcionária que trabalham em turnos separados. Durante cada turno, apenas uma pessoa é responsável por todas as atividades do estabelecimento.

Atualmente, o controle das vendas, do estoque e das compras é realizado de forma predominantemente manual. Os produtos possuem etiquetas de preço, o estoque é controlado visualmente pelas prateleiras e não existe um registro das movimentações de entrada e saída de mercadorias.

Essa forma de gerenciamento dificulta o controle do estoque, aumenta a ocorrência de perdas, dificulta a análise financeira do negócio e reduz a confiabilidade das informações utilizadas para a tomada de decisões.

## Problema

CONTROLE DE ESTOQUE
- dificuldade em controlar a quantidade real de produtos disponíveis;
- dificuldade em registrar as entradas e saídas de mercadorias;
- dificuldade em identificar perdas por vencimento, deterioração ou quebra;
- dificuldade em saber quando um produto está acabando;
- dificuldade em controlar produtos vendidos por unidade e por peso.

CONTROLE DE COMPRAS
- dificuldade em registrar a entrada de novas mercadorias;
- dificuldade em manter o histórico de preços de compra;
- dificuldade em comparar preços entre diferentes fornecedores;
- dificuldade em identificar o melhor fornecedor para cada produto.

CONTROLE DE VENDAS
- processo manual para localizar os produtos durante o atendimento;
- ausência de integração entre as vendas e o controle de estoque;
- necessidade de registrar diferentes formas de pagamento;
- necessidade de aplicar descontos quando necessário;
- necessidade de emitir comprovantes das vendas realizadas.
- dificuldade em controlar vendas realizadas a prazo (fiado);
- dificuldade em acompanhar clientes com pagamentos pendentes.
- dificuldade em registrar cancelamentos de vendas;
- dificuldade em consultar o histórico de vendas.

GESTÃO
- dificuldade em calcular o lucro obtido com cada produto;
- dificuldade em identificar os produtos mais vendidos;
- dificuldade em analisar o desempenho financeiro do estabelecimento;
- dificuldade em tomar decisões sobre compras e reposição de estoque.


## Solução Proposta

Desenvolver um sistema web para gerenciamento de pequenos mercados que centralize o cadastro de produtos, fornecedores, compras, estoque e vendas.

O sistema deverá utilizar leitura de código de barras para agilizar o atendimento, atualizar automaticamente o estoque após cada venda ou entrada de mercadorias e fornecer informações gerenciais que auxiliem na administração do estabelecimento.

## Objetivos

- Organizar o controle de estoque;
- Automatizar o processo de vendas;
- Integrar as vendas ao estoque;
- controlar vendas realizadas a prazo;
- acompanhar pagamentos pendentes dos clientes.
- Registrar compras de mercadorias;
- Controlar fornecedores e preços de compra;
- Calcular o lucro aproximado das vendas;
- Reduzir perdas de mercadorias;
- Facilitar a reposição de produtos;
- Agilizar o atendimento aos clientes;
- Gerar relatórios que auxiliem na gestão do mercadinho.


## Público-Alvo

O sistema será utilizado inicialmente pela proprietária do mercadinho e sua funcionária, responsáveis por todas as atividades do estabelecimento, incluindo atendimento ao cliente, operação do caixa, cadastro de produtos, compras de mercadorias e controle financeiro.

## Escopo Inicial

A primeira versão do sistema terá como foco informatizar as principais operações do mercadinho, implementando apenas as funcionalidades essenciais para o funcionamento diário do estabelecimento.

Nesta versão serão implementadas as seguintes funcionalidades:

### Produtos
- cadastrar produtos;
- alterar produtos;
- consultar produtos;
- cadastrar categorias.

### Fornecedores
- cadastrar fornecedores;
- consultar fornecedores.

### Compras
- registrar entrada de mercadorias;
- consultar histórico de compras.

### Estoque
- controlar estoque automaticamente;
- consultar quantidade disponível.

### Vendas
- registrar vendas;
- registrar descontos;
- registrar diferentes formas de pagamento;
- registrar vendas a prazo;
- registrar pagamento de vendas a prazo;
- emitir comprovantes.

### Clientes
- cadastrar clientes;
- consultar clientes;
- consultar pagamentos pendentes.

### Caixa
- registrar movimentações;
- consultar histórico.

### Relatórios
- estoque;
- vendas;
- lucro.

Funcionalidades como emissão de nota fiscal eletrônica, acesso pelo celular, controle de usuários, controle de validade por lote, integração com maquininhas de cartão, programa de fidelidade e dashboards gerenciais poderão ser implementadas em versões futuras.

## Observações

Este sistema será desenvolvido inicialmente para atender às necessidades do mercadinho dos proprietários do projeto. Entretanto, durante seu desenvolvimento, a arquitetura será planejada para permitir futuras expansões, possibilitando a adaptação do sistema para outros pequenos estabelecimentos comerciais.
