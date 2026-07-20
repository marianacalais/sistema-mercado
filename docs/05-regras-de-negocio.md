# Regras de Negócio

## RN01 - Produtos

**RN01.01** Apenas produtos ativos poderão ser utilizados em novas compras e vendas.

**RN01.02** Produtos desativados deverão permanecer disponíveis para consulta no histórico do sistema.

**RN01.03** Não poderão existir dois produtos cadastrados com o mesmo código de barras.

---

## RN02 - Categorias

**RN02.01** Uma categoria poderá estar associada a vários produtos.

**RN02.02** Uma categoria não poderá ser removida enquanto existir produto vinculado a ela.

---

## RN03 - Fornecedores

**RN03.01** Um fornecedor poderá fornecer diversos produtos.

**RN03.02** Um fornecedor desativado não poderá ser utilizado em novas compras.

---

## RN04 - Compras

**RN04.01** Toda compra deverá estar vinculada a um fornecedor cadastrado e ativo.

**RN04.02** Toda compra deverá possuir pelo menos um produto.

**RN04.03** A quantidade informada para cada item da compra deverá ser maior que zero.

**RN04.04** O preço de compra informado deverá ser maior que zero.

**RN04.05** Após a conclusão da compra, o estoque dos produtos adquiridos deverá ser atualizado automaticamente.

---

## RN05 - Estoque

**RN05.01** O estoque deverá ser atualizado automaticamente após a conclusão de compras.

**RN05.02** O estoque deverá ser atualizado automaticamente após a conclusão de vendas.

**RN05.03** Ajustes de estoque deverão registrar o motivo da alteração.

**RN05.04** O estoque de um produto não poderá assumir valor negativo.

**RN05.05** As perdas registradas deverão reduzir automaticamente o estoque do produto.

---

## RN06 - Clientes

**RN06.01** Apenas clientes cadastrados poderão realizar compras a prazo.

**RN06.02** O pagamento de um débito deverá reduzir automaticamente o saldo devedor do cliente.

**RN06.03** Quando todos os débitos forem quitados, o cliente não deverá possuir pendências financeiras.

---

## RN07 - Vendas

**RN07.01** Toda venda deverá possuir pelo menos um produto.

**RN07.02** Apenas produtos ativos poderão ser vendidos.

**RN07.03** Apenas produtos com estoque disponível poderão ser vendidos.

**RN07.04** O valor total da venda deverá ser calculado automaticamente com base nos produtos adicionados.

**RN07.05** O valor total da venda deverá ser recalculado sempre que houver alteração nos produtos ou nas quantidades.

**RN07.06** A venda somente poderá ser concluída após o registro do pagamento ou do lançamento como venda a prazo.

**RN07.07** Vendas canceladas não deverão gerar movimentação financeira.

**RN07.08** Vendas canceladas deverão retornar os produtos ao estoque, caso já tenham sido baixados.

---

## RN08 - Caixa

**RN08.01** Apenas um caixa poderá permanecer aberto por vez.

**RN08.02** Não será permitido registrar vendas com o caixa fechado.

**RN08.03** Toda movimentação financeira deverá permanecer registrada no histórico.

**RN08.04** O fechamento do caixa deverá considerar todas as entradas e saídas realizadas durante o expediente.

**RN08.05** Sangrias deverão reduzir o saldo disponível do caixa.

---

## RN09 - Relatórios

**RN09.01** Os relatórios deverão utilizar apenas dados registrados no sistema.

**RN09.02** Os relatórios por período deverão considerar apenas registros compreendidos entre as datas informadas.

**RN09.03** O relatório de lucro deverá considerar o preço de venda e o preço de custo registrados para cada produto.
