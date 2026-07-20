# Requisitos Não Funcionais

## RNF01 - Usabilidade

**RNF01.01** O sistema deverá possuir uma interface simples e intuitiva, adequada para usuários com conhecimentos básicos em informática.

**RNF01.02** O sistema deverá apresentar mensagens claras para orientar o usuário durante a utilização.

**RNF01.03** O sistema deverá informar ao usuário quando uma operação for realizada com sucesso ou quando ocorrer algum erro.

**RNF01.04** O sistema deverá manter um padrão visual entre todas as telas do sistema.

---

## RNF02 - Desempenho

**RNF02.01** O sistema deverá apresentar os resultados das consultas em até 2 segundos, considerando condições normais de utilização.

**RNF02.02** O sistema deverá processar a leitura de um código de barras em até 2 segundos após sua captura.

**RNF02.03** O sistema deverá calcular automaticamente o valor total de uma venda sem atrasos perceptíveis ao usuário.

---

## RNF03 - Segurança

**RNF03.01** O sistema deverá permitir o acesso apenas a usuários previamente cadastrados.

**RNF03.02** O sistema deverá exigir autenticação por usuário e senha para acesso às funcionalidades do sistema.

**RNF03.03** O sistema deverá impedir o acesso de usuários não autenticados às informações do sistema.

**RNF03.04** O sistema deverá preservar a integridade dos dados armazenados, impedindo alterações não autorizadas.

---

## RNF04 - Confiabilidade e Integridade dos Dados

**RNF04.01** O sistema deverá garantir que todas as informações registradas sejam armazenadas de forma consistente.

**RNF04.02** O sistema deverá manter o histórico das compras, vendas, movimentações de estoque e movimentações financeiras.

**RNF04.03** O sistema não deverá permitir registros inconsistentes que comprometam a integridade dos dados.

---

## RNF05 - Compatibilidade

**RNF05.01** O sistema deverá ser compatível com o sistema operacional Windows 11.

**RNF05.02** O sistema deverá ser compatível com leitores de código de barras que operem como dispositivo de entrada USB (HID).

**RNF05.03** O sistema deverá permitir a impressão de comprovantes em impressoras térmicas compatíveis com o sistema operacional utilizado.

---

## RNF06 - Disponibilidade

**RNF06.01** O sistema deverá permanecer disponível durante todo o horário de funcionamento do estabelecimento.

**RNF06.02** O sistema deverá preservar os dados armazenados mesmo após desligamentos inesperados do computador.

---

## RNF07 - Backup e Recuperação

**RNF07.01** O sistema deverá permitir a realização de backup do banco de dados.

**RNF07.02** O sistema deverá permitir a restauração dos dados a partir de um backup previamente realizado.

---

## RNF08 - Manutenibilidade

**RNF08.01** O sistema deverá possuir código organizado e modular, facilitando futuras manutenções.

**RNF08.02** O sistema deverá permitir a inclusão de novas funcionalidades sem necessidade de alterações significativas na arquitetura do sistema.

---

## RNF09 - Portabilidade

**RNF09.01** O sistema deverá ser executado em computadores que atendam aos requisitos mínimos do sistema operacional Windows 11.

**RNF09.02** O sistema deverá permitir a migração do banco de dados para outro computador sem perda das informações.

---

## RNF10 - Escalabilidade

**RNF10.01** O sistema deverá suportar o crescimento da quantidade de produtos, clientes, fornecedores e vendas sem necessidade de alterações estruturais.

**RNF10.02** O sistema deverá permitir a inclusão de novos módulos futuramente, preservando a arquitetura existente.
