# Casos de Uso

## Atores do Sistema

### Administrador

Responsável pelo gerenciamento de produtos, categorias, fornecedores, compras, estoque, clientes, caixa e relatórios.

### Operador do Caixa

Responsável pela abertura e fechamento do caixa, registro de vendas, recebimento de pagamentos, sangrias e consultas relacionadas ao atendimento.

> Como o estabelecimento possui poucos funcionários, uma mesma pessoa poderá exercer os dois papéis. A separação representa as responsabilidades existentes no sistema, e não necessariamente pessoas diferentes.

---

## Sumário:
UC01 Cadastrar Produto
UC02 Alterar Produto
UC03 Consultar Produto
UC04 Gerenciar Categorias
UC05 Gerenciar Fornecedores
UC06 Registrar Compra
UC07 Realizar Ajuste de Estoque
UC08 Registrar Perda
UC09 Cadastrar Cliente
UC10 Registrar Pagamento de Débito
UC11 Registrar Venda
UC12 Cancelar Venda
UC13 Abrir Caixa
UC14 Fechar Caixa
UC15 Registrar Sangria
UC16 Emitir Relatórios

---

## UC01 - Cadastrar Produto

### Objetivo

Permitir o cadastro de um novo produto comercializado pelo estabelecimento.

### Atores

Administrador.

### Pré-condições

- O usuário deverá estar autenticado no sistema.
- A categoria do produto deverá estar previamente cadastrada, quando aplicável.

### Fluxo Principal

1. O administrador acessa a área de produtos.
2. O administrador seleciona a opção de cadastrar produto.
3. O sistema apresenta o formulário de cadastro.
4. O administrador informa os dados do produto.
5. O administrador associa o produto a uma categoria.
6. O administrador confirma o cadastro.
7. O sistema valida os dados informados.
8. O sistema registra o produto.
9. O sistema informa que o cadastro foi realizado com sucesso.

### Fluxos Alternativos

#### 7A - Código de barras já cadastrado

1. O sistema identifica que o código de barras já está associado a outro produto.
2. O sistema informa que não podem existir dois produtos com o mesmo código de barras.
3. O produto não é cadastrado.
4. O administrador corrige o código ou cancela a operação.

#### 7B - Dados obrigatórios não informados

1. O sistema identifica que existem campos obrigatórios não preenchidos.
2. O sistema informa quais campos devem ser preenchidos.
3. O administrador corrige os dados.
4. O fluxo retorna ao passo 6.

#### 7C - Valores inválidos

1. O sistema identifica valores inválidos, como preços ou estoque mínimo negativos.
2. O sistema informa quais valores devem ser corrigidos.
3. O administrador corrige os dados.
4. O fluxo retorna ao passo 6.

### Pós-condições

- O produto fica cadastrado e disponível para utilização no sistema.

---

## UC02 - Alterar Produto

### Objetivo

Permitir a alteração dos dados de um produto cadastrado.

### Atores

Administrador.

### Pré-condições

- O usuário deverá estar autenticado.
- O produto deverá estar cadastrado.

### Fluxo Principal

1. O administrador acessa a área de produtos.
2. O administrador localiza o produto desejado.
3. O sistema apresenta os dados do produto.
4. O administrador seleciona a opção de alteração.
5. O administrador modifica os dados desejados.
6. O administrador confirma as alterações.
7. O sistema valida os dados informados.
8. O sistema atualiza o cadastro.
9. O sistema informa que a alteração foi realizada com sucesso.

### Fluxos Alternativos

#### 2A - Produto não encontrado

1. O sistema não encontra um produto correspondente à pesquisa.
2. O sistema informa que nenhum produto foi localizado.
3. O caso de uso é encerrado.

#### 7A - Código de barras já utilizado

1. O sistema identifica que o novo código de barras pertence a outro produto.
2. O sistema informa o conflito.
3. O administrador corrige o código.
4. O fluxo retorna ao passo 6.

#### 7B - Dados inválidos

1. O sistema identifica dados obrigatórios ausentes ou valores inválidos.
2. O sistema apresenta os erros encontrados.
3. O administrador corrige os dados.
4. O fluxo retorna ao passo 6.

### Pós-condições

- Os dados do produto ficam atualizados.

---

## UC03 - Consultar Produto

### Objetivo

Permitir a consulta das informações de um produto cadastrado.

### Atores

Administrador e Operador do Caixa.

### Pré-condições

- O usuário deverá estar autenticado.

### Fluxo Principal

1. O usuário acessa a área de consulta de produtos.
2. O usuário informa o nome ou o código de barras do produto.
3. O sistema realiza a pesquisa.
4. O sistema apresenta os produtos correspondentes.
5. O usuário seleciona o produto desejado.
6. O sistema apresenta os dados completos do produto.

### Fluxos Alternativos

#### 4A - Produto não encontrado

1. O sistema não encontra produtos correspondentes.
2. O sistema informa que nenhum produto foi localizado.
3. O usuário poderá realizar uma nova pesquisa.

### Pós-condições

- Nenhuma informação é alterada.

---

## UC04 - Gerenciar Categorias

### Objetivo

Permitir cadastrar, alterar, consultar, listar e desativar categorias de produtos.

### Atores

Administrador.

### Pré-condições

- O usuário deverá estar autenticado.

### Fluxo Principal

1. O administrador acessa a área de categorias.
2. O sistema apresenta as categorias cadastradas.
3. O administrador seleciona a operação desejada.
4. O sistema apresenta os campos correspondentes à operação.
5. O administrador informa ou altera os dados da categoria.
6. O administrador confirma a operação.
7. O sistema valida os dados.
8. O sistema registra a operação.
9. O sistema informa que a operação foi concluída com sucesso.

### Fluxos Alternativos

#### 7A - Dados obrigatórios não informados

1. O sistema identifica campos obrigatórios não preenchidos.
2. O sistema informa os campos pendentes.
3. O administrador corrige os dados.
4. O fluxo retorna ao passo 6.

#### 7B - Categoria vinculada a produtos

1. O administrador solicita a desativação de uma categoria vinculada a produtos.
2. O sistema solicita a confirmação da operação.
3. O administrador confirma ou cancela a desativação.

### Pós-condições

- A categoria é cadastrada, alterada ou desativada conforme a operação escolhida.

---

## UC05 - Gerenciar Fornecedores

### Objetivo

Permitir cadastrar, alterar, consultar, listar e desativar fornecedores.

### Atores

Administrador.

### Pré-condições

- O usuário deverá estar autenticado.

### Fluxo Principal

1. O administrador acessa a área de fornecedores.
2. O sistema apresenta os fornecedores cadastrados.
3. O administrador seleciona a operação desejada.
4. O sistema apresenta o formulário correspondente.
5. O administrador informa ou altera os dados.
6. O administrador confirma a operação.
7. O sistema valida os dados.
8. O sistema registra a operação.
9. O sistema informa que a operação foi realizada com sucesso.

### Fluxos Alternativos

#### 7A - Dados obrigatórios não informados

1. O sistema identifica campos obrigatórios não preenchidos.
2. O sistema informa os campos pendentes.
3. O administrador corrige os dados.
4. O fluxo retorna ao passo 6.

#### 7B - Fornecedor não encontrado

1. O sistema não encontra o fornecedor pesquisado.
2. O sistema informa que nenhum fornecedor foi localizado.
3. O administrador poderá realizar uma nova pesquisa.

### Pós-condições

- O fornecedor é cadastrado, alterado ou desativado conforme a operação escolhida.

---

## UC06 - Registrar Compra

### Objetivo

Permitir o registro de uma compra de mercadorias realizada junto a um fornecedor.

### Atores

Administrador.

### Pré-condições

- O usuário deverá estar autenticado.
- O fornecedor deverá estar cadastrado e ativo.
- Os produtos deverão estar cadastrados.

### Fluxo Principal

1. O administrador acessa a área de compras.
2. O administrador seleciona a opção de registrar compra.
3. O sistema cria uma compra em andamento.
4. O administrador seleciona o fornecedor.
5. O administrador adiciona um produto.
6. O administrador informa a quantidade e o preço de compra.
7. O sistema adiciona o produto à compra.
8. O sistema calcula o valor parcial e o valor total da compra.
9. O administrador repete os passos 5 e 6 para os demais produtos.
10. O administrador confirma a compra.
11. O sistema valida os dados.
12. O sistema registra a compra.
13. O sistema atualiza o estoque dos produtos.
14. O sistema informa que a compra foi registrada com sucesso.

### Fluxos Alternativos

#### 5A - Produto não encontrado

1. O sistema não encontra o produto informado.
2. O sistema apresenta a opção de realizar uma nova pesquisa.
3. O fluxo retorna ao passo 5.

#### 6A - Quantidade ou preço inválido

1. O sistema identifica que a quantidade ou o preço informado é inválido.
2. O sistema solicita a correção dos valores.
3. O fluxo retorna ao passo 6.

#### 7A - Remoção de produto

1. O administrador seleciona um produto adicionado à compra.
2. O administrador informa a quantidade a ser removida.
3. O sistema reduz a quantidade do item.
4. Caso toda a quantidade seja removida, o sistema exclui o item da compra.
5. O sistema recalcula o valor total.

#### 10A - Compra sem produtos

1. O sistema identifica que a compra não possui produtos.
2. O sistema impede sua conclusão.
3. O administrador deverá adicionar pelo menos um produto.

#### 10B - Cancelamento do registro

1. O administrador solicita o cancelamento.
2. O sistema solicita confirmação.
3. O administrador confirma.
4. O sistema descarta a compra em andamento.

### Pós-condições

- A compra fica registrada.
- O estoque dos produtos é atualizado.
- O histórico de compras é atualizado.

---

## UC07 - Realizar Ajuste de Estoque

### Objetivo

Permitir a correção da quantidade registrada de um produto no estoque.

### Atores

Administrador.

### Pré-condições

- O usuário deverá estar autenticado.
- O produto deverá estar cadastrado.

### Fluxo Principal

1. O administrador acessa a área de estoque.
2. O administrador localiza o produto.
3. O sistema apresenta a quantidade registrada.
4. O administrador seleciona a opção de ajustar estoque.
5. O administrador informa a quantidade correta.
6. O administrador informa o motivo do ajuste.
7. O administrador confirma a operação.
8. O sistema valida os dados.
9. O sistema atualiza o estoque.
10. O sistema registra a movimentação no histórico.
11. O sistema informa que o ajuste foi realizado com sucesso.

### Fluxos Alternativos

#### 2A - Produto não encontrado

1. O sistema não encontra o produto informado.
2. O sistema informa que nenhum produto foi localizado.
3. O caso de uso é encerrado.

#### 8A - Quantidade inválida

1. O sistema identifica que a quantidade informada é inválida.
2. O sistema solicita a correção.
3. O fluxo retorna ao passo 5.

#### 8B - Motivo não informado

1. O sistema identifica que o motivo não foi preenchido.
2. O sistema solicita que o administrador informe o motivo.
3. O fluxo retorna ao passo 6.

### Pós-condições

- A quantidade do produto é atualizada.
- O ajuste fica registrado no histórico de movimentações.

---

## UC08 - Registrar Perda de Produto

### Objetivo

Permitir o registro de produtos perdidos, vencidos, quebrados ou impróprios para venda.

### Atores

Administrador.

### Pré-condições

- O usuário deverá estar autenticado.
- O produto deverá estar cadastrado.
- O produto deverá possuir estoque disponível.

### Fluxo Principal

1. O administrador acessa a área de estoque.
2. O administrador seleciona a opção de registrar perda.
3. O administrador localiza o produto.
4. O sistema apresenta a quantidade disponível.
5. O administrador informa a quantidade perdida.
6. O administrador informa o motivo da perda.
7. O administrador confirma a operação.
8. O sistema valida os dados.
9. O sistema reduz a quantidade do estoque.
10. O sistema registra a perda no histórico.
11. O sistema informa que a perda foi registrada com sucesso.

### Fluxos Alternativos

#### 5A - Quantidade superior ao estoque

1. O sistema identifica que a quantidade informada é superior ao estoque disponível.
2. O sistema impede o registro.
3. O administrador corrige a quantidade.

#### 5B - Quantidade inválida

1. O sistema identifica uma quantidade igual ou inferior a zero.
2. O sistema solicita a correção.
3. O fluxo retorna ao passo 5.

#### 6A - Motivo não informado

1. O sistema solicita o preenchimento do motivo da perda.
2. O fluxo retorna ao passo 6.

### Pós-condições

- O estoque do produto é reduzido.
- A perda fica registrada no histórico.

---

## UC09 - Cadastrar Cliente

### Objetivo

Permitir o cadastro de clientes, especialmente aqueles autorizados a realizar compras a prazo.

### Atores

Administrador e Operador do Caixa.

### Pré-condições

- O usuário deverá estar autenticado.

### Fluxo Principal

1. O usuário acessa a área de clientes.
2. O usuário seleciona a opção de cadastrar cliente.
3. O sistema apresenta o formulário de cadastro.
4. O usuário informa os dados do cliente.
5. O usuário confirma o cadastro.
6. O sistema valida os dados.
7. O sistema registra o cliente.
8. O sistema informa que o cadastro foi realizado com sucesso.

### Fluxos Alternativos

#### 6A - Dados obrigatórios não informados

1. O sistema identifica campos obrigatórios não preenchidos.
2. O sistema informa os campos pendentes.
3. O usuário corrige os dados.
4. O fluxo retorna ao passo 5.

#### 6B - Cliente já cadastrado

1. O sistema identifica outro cliente com os mesmos dados de identificação.
2. O sistema informa a possível duplicidade.
3. O usuário poderá consultar o cadastro existente ou corrigir os dados.

### Pós-condições

- O cliente fica cadastrado e disponível para consultas e vendas a prazo.

---

## UC10 - Registrar Pagamento de Débito

### Objetivo

Permitir o registro do pagamento total ou parcial de um débito de cliente.

### Atores

Administrador e Operador do Caixa.

### Pré-condições

- O usuário deverá estar autenticado.
- O caixa deverá estar aberto.
- O cliente deverá possuir débito pendente.

### Fluxo Principal

1. O usuário acessa a área de clientes.
2. O usuário localiza o cliente.
3. O sistema apresenta os débitos pendentes.
4. O usuário seleciona o débito.
5. O usuário informa o valor pago.
6. O usuário informa a forma de pagamento.
7. O usuário confirma o recebimento.
8. O sistema valida o valor informado.
9. O sistema registra o pagamento.
10. O sistema reduz o saldo devedor do cliente.
11. O sistema registra a entrada no caixa.
12. O sistema informa que o pagamento foi registrado com sucesso.

### Fluxos Alternativos

#### 3A - Cliente sem débitos

1. O sistema identifica que o cliente não possui débitos pendentes.
2. O sistema informa a situação.
3. O caso de uso é encerrado.

#### 5A - Pagamento parcial

1. O valor informado é inferior ao saldo devedor.
2. O sistema registra o pagamento parcial.
3. O débito permanece pendente com o valor restante.
4. O fluxo segue para o passo 11.

#### 5B - Valor superior ao débito

1. O sistema identifica que o valor informado é superior ao saldo devedor.
2. O sistema informa o valor máximo permitido.
3. O usuário corrige o valor.

#### 5C - Valor inválido

1. O sistema identifica um valor igual ou inferior a zero.
2. O sistema solicita a correção.
3. O fluxo retorna ao passo 5.

### Pós-condições

- O pagamento fica registrado.
- O saldo devedor do cliente é atualizado.
- O caixa recebe a movimentação financeira correspondente.

---

## UC11 - Registrar Venda

### Objetivo

Permitir o registro de uma venda de produtos.

### Atores

Operador do Caixa.

### Pré-condições

- O usuário deverá estar autenticado.
- O caixa deverá estar aberto.
- Os produtos deverão estar cadastrados e ativos.

### Fluxo Principal

1. O operador acessa a área de vendas.
2. O operador seleciona a opção de iniciar venda.
3. O sistema cria uma venda em andamento.
4. O operador lê o código de barras ou pesquisa o produto pelo nome.
5. O sistema localiza o produto.
6. O operador informa a quantidade a ser adicionada.
7. O sistema verifica a disponibilidade em estoque.
8. O sistema adiciona o produto à venda.
9. O sistema calcula o subtotal do item e o valor total da venda.
10. O operador repete os passos 4 a 6 para os demais produtos.
11. O operador informa eventual desconto.
12. O sistema recalcula o valor total.
13. O operador seleciona a forma de pagamento.
14. O operador informa os valores recebidos.
15. O sistema valida o pagamento.
16. O operador confirma a conclusão.
17. O sistema registra a venda.
18. O sistema reduz o estoque dos produtos.
19. O sistema registra a movimentação financeira no caixa.
20. O sistema emite o comprovante.
21. O sistema informa que a venda foi concluída com sucesso.

### Fluxos Alternativos

#### 5A - Produto não encontrado

1. O sistema informa que o produto não foi localizado.
2. O operador poderá realizar uma nova pesquisa.
3. O fluxo retorna ao passo 4.

#### 7A - Produto sem estoque

1. O sistema informa que o produto está sem estoque.
2. O produto não é adicionado.
3. O fluxo retorna ao passo 4.

#### 7B - Quantidade superior ao estoque

1. O sistema informa a quantidade disponível.
2. O operador corrige a quantidade.
3. O fluxo retorna ao passo 6.

#### 8A - Produto já adicionado

1. O sistema identifica que o produto já está na venda.
2. O sistema soma a nova quantidade à quantidade existente.
3. O sistema recalcula o subtotal e o total.

#### 8B - Remoção de produto

1. O operador seleciona um produto da venda.
2. O operador informa a quantidade a ser removida.
3. O sistema reduz a quantidade.
4. Caso toda a quantidade seja removida, o sistema exclui o item.
5. O sistema recalcula o valor total.

#### 13A - Múltiplas formas de pagamento

1. O operador seleciona mais de uma forma de pagamento.
2. O operador informa o valor correspondente a cada forma.
3. O sistema verifica se a soma corresponde ao total da venda.
4. O fluxo segue para o passo 16.

#### 13B - Venda a prazo

1. O operador seleciona a forma de pagamento a prazo.
2. O sistema solicita a identificação do cliente.
3. O operador seleciona um cliente cadastrado.
4. O sistema registra o valor como débito do cliente.
5. O fluxo segue para o passo 16.

#### 15A - Valor recebido insuficiente

1. O sistema identifica que o valor recebido é inferior ao valor da venda.
2. O sistema informa o valor restante.
3. O operador corrige ou complementa o pagamento.

#### 15B - Pagamento em dinheiro superior ao total

1. O sistema calcula o valor do troco.
2. O sistema apresenta o troco ao operador.
3. O fluxo segue para o passo 16.

#### 16A - Venda sem produtos

1. O sistema identifica que a venda não possui produtos.
2. O sistema impede sua conclusão.
3. O operador deverá adicionar pelo menos um produto.

### Pós-condições

- A venda fica registrada.
- O estoque é atualizado.
- O caixa é atualizado.
- O comprovante é emitido.
- Caso seja uma venda a prazo, o débito é associado ao cliente.

---

## UC12 - Cancelar Venda

### Objetivo

Permitir o cancelamento de uma venda em andamento ou já concluída.

### Atores

Administrador e Operador do Caixa.

### Pré-condições

- O usuário deverá estar autenticado.
- A venda deverá existir.
- Para vendas concluídas, o cancelamento deverá estar autorizado.

### Fluxo Principal

1. O usuário acessa a área de vendas.
2. O usuário localiza a venda.
3. O sistema apresenta os dados da venda.
4. O usuário seleciona a opção de cancelar.
5. O sistema solicita o motivo do cancelamento.
6. O usuário informa o motivo.
7. O sistema solicita confirmação.
8. O usuário confirma o cancelamento.
9. O sistema altera o status da venda para cancelada.
10. O sistema registra o motivo e a data do cancelamento.
11. O sistema informa que a venda foi cancelada.

### Fluxos Alternativos

#### 2A - Venda não encontrada

1. O sistema informa que a venda não foi localizada.
2. O caso de uso é encerrado.

#### 4A - Venda em andamento

1. O sistema descarta os itens e pagamentos ainda não confirmados.
2. O fluxo segue para o passo 10.

#### 4B - Venda concluída

1. O sistema devolve os produtos ao estoque.
2. O sistema registra a movimentação de estorno no caixa.
3. Caso a venda seja a prazo, o sistema remove ou ajusta o débito do cliente.
4. O fluxo segue para o passo 10.

#### 6A - Motivo não informado

1. O sistema solicita o preenchimento do motivo.
2. O fluxo retorna ao passo 6.

### Pós-condições

- A venda fica registrada como cancelada.
- O estoque, o caixa e os débitos são ajustados quando necessário.
- O cancelamento permanece no histórico.

---

## UC13 - Abrir Caixa

### Objetivo

Permitir o início das operações financeiras do estabelecimento.

### Atores

Operador do Caixa.

### Pré-condições

- O usuário deverá estar autenticado.
- Não poderá existir outro caixa aberto.

### Fluxo Principal

1. O operador acessa a área de caixa.
2. O operador seleciona a opção de abertura.
3. O sistema solicita o valor inicial em dinheiro.
4. O operador informa o valor.
5. O operador confirma a abertura.
6. O sistema valida os dados.
7. O sistema registra a data, a hora, o operador e o valor inicial.
8. O sistema altera o status do caixa para aberto.
9. O sistema informa que o caixa foi aberto com sucesso.

### Fluxos Alternativos

#### 2A - Caixa já aberto

1. O sistema identifica que existe um caixa aberto.
2. O sistema impede uma nova abertura.
3. O sistema apresenta os dados do caixa atual.

#### 4A - Valor inicial inválido

1. O sistema identifica um valor negativo.
2. O sistema solicita a correção.
3. O fluxo retorna ao passo 4.

### Pós-condições

- O caixa fica aberto.
- O sistema passa a permitir o registro de vendas e movimentações financeiras.

---

## UC14 - Fechar Caixa

### Objetivo

Permitir o encerramento das operações financeiras do período.

### Atores

Administrador e Operador do Caixa.

### Pré-condições

- O usuário deverá estar autenticado.
- Deverá existir um caixa aberto.

### Fluxo Principal

1. O usuário acessa a área de caixa.
2. O usuário seleciona a opção de fechamento.
3. O sistema apresenta o resumo financeiro do período.
4. O sistema apresenta o valor esperado em cada forma de pagamento.
5. O usuário informa o valor contado em dinheiro.
6. O sistema calcula possíveis diferenças.
7. O usuário confere as informações.
8. O usuário confirma o fechamento.
9. O sistema registra a data e a hora do fechamento.
10. O sistema registra os valores apurados.
11. O sistema altera o status do caixa para fechado.
12. O sistema informa que o caixa foi fechado com sucesso.

### Fluxos Alternativos

#### 2A - Nenhum caixa aberto

1. O sistema informa que não existe caixa aberto.
2. O caso de uso é encerrado.

#### 6A - Diferença de caixa

1. O sistema identifica diferença entre o valor esperado e o contado.
2. O sistema apresenta o valor da diferença.
3. O usuário informa uma observação.
4. O fluxo retorna ao passo 7.

#### 8A - Cancelamento do fechamento

1. O usuário decide não confirmar o fechamento.
2. O sistema mantém o caixa aberto.
3. O caso de uso é encerrado.

### Pós-condições

- O caixa fica fechado.
- O resumo financeiro permanece armazenado no histórico.
- Novas vendas não podem ser realizadas até uma nova abertura.

---

## UC15 - Registrar Sangria

### Objetivo

Permitir a retirada de dinheiro em espécie do caixa durante o expediente.

### Atores

Administrador e Operador do Caixa.

### Pré-condições

- O usuário deverá estar autenticado.
- O caixa deverá estar aberto.
- Deverá existir saldo suficiente em dinheiro.

### Fluxo Principal

1. O usuário acessa a área de caixa.
2. O usuário seleciona a opção de registrar sangria.
3. O sistema apresenta o saldo atual em dinheiro.
4. O usuário informa o valor da retirada.
5. O usuário informa o motivo.
6. O usuário confirma a operação.
7. O sistema valida os dados.
8. O sistema registra a sangria.
9. O sistema reduz o saldo em dinheiro do caixa.
10. O sistema informa que a sangria foi registrada com sucesso.

### Fluxos Alternativos

#### 4A - Valor superior ao saldo

1. O sistema identifica que o valor informado é superior ao saldo disponível.
2. O sistema impede a operação.
3. O usuário corrige o valor.

#### 4B - Valor inválido

1. O sistema identifica um valor igual ou inferior a zero.
2. O sistema solicita a correção.
3. O fluxo retorna ao passo 4.

#### 5A - Motivo não informado

1. O sistema solicita o preenchimento do motivo.
2. O fluxo retorna ao passo 5.

### Pós-condições

- A sangria fica registrada.
- O saldo em dinheiro do caixa é atualizado.
- A movimentação permanece disponível no histórico.

---

## UC16 - Emitir Relatórios

### Objetivo

Permitir a geração e consulta de relatórios gerenciais do estabelecimento.

### Atores

Administrador.

### Pré-condições

- O usuário deverá estar autenticado.
- Deverão existir dados registrados para o relatório solicitado.

### Fluxo Principal

1. O administrador acessa a área de relatórios.
2. O sistema apresenta os tipos de relatórios disponíveis.
3. O administrador seleciona o relatório desejado.
4. O sistema solicita os filtros aplicáveis.
5. O administrador informa os filtros.
6. O administrador solicita a geração.
7. O sistema valida os filtros.
8. O sistema consulta os dados.
9. O sistema gera o relatório.
10. O sistema apresenta o relatório ao administrador.

### Tipos de Relatórios

- Relatório de estoque.
- Relatório de vendas por período.
- Relatório de compras por período.
- Relatório de produtos com estoque baixo.
- Relatório de produtos sem estoque.
- Relatório de produtos mais vendidos.
- Relatório de lucro por período.
- Relatório de clientes com pagamentos pendentes.
- Relatório do histórico financeiro do caixa.
- Relatório de movimentações de estoque.

### Fluxos Alternativos

#### 7A - Período inválido

1. O sistema identifica que a data inicial é posterior à data final.
2. O sistema informa o erro.
3. O administrador corrige o período.
4. O fluxo retorna ao passo 6.

#### 8A - Nenhum dado encontrado

1. O sistema não encontra registros correspondentes aos filtros.
2. O sistema informa que não existem dados para o período ou critério selecionado.
3. O administrador poderá alterar os filtros.

### Pós-condições

- O relatório é apresentado.
- Nenhuma informação do sistema é alterada.