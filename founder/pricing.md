# Preço — Marca Kids Premium

Fontes: `founder/pricing-curve.md` (100 compradores simulados), `founder/competitors.md` e a ferramenta do CFO rodada sobre `founder/numbers.json`. **Todos os custos são as hipóteses do documento original, sem cotação de fabricante.** As respostas dos compradores simulados servem para escolher o que testar, não provam nada.

## O que os três lados dizem

**Compradores (Van Westendorp):** a faixa aceitável vai de **R$45 a R$131/mês**. Abaixo de ~R$45 o produto parece ruim, e acima de ~R$131 muita gente não compra. O preço "normal" na cabeça deles (IPP) é **≈ R$80**. Os **R$149 ficam acima da faixa**, e para 34 dos 100 compradores R$149 já é "caro demais, não compro".

**Concorrentes:** o premium líder (Alpha Kids) custa **≈ R$58/mês** por criança. O Mult-AZ sai por ≈ R$50 e os de farmácia por R$15–33.

**A conta do negócio:** com os custos do documento, cada pedido mensal custa **≈ R$84–88** antes de qualquer marketing.

| Preço (envio mensal) | Contribuição por pedido | Ponto de equilíbrio |
|---|---:|---:|
| R$149 | **R$61** | 123 assinantes |
| R$129 | R$43 | 176 |
| R$109 | R$24 | 309 |
| R$99 | R$15 | 497 |
| R$89 | R$6 | 1.275 |
| R$79 | **−R$3** (prejuízo por pedido) | nunca |

> **Correção no documento:** ele diz que sobram ~R$73 por pedido a R$149. Somando os custos que ele mesmo lista (8% de tributos, R$15 de frete, R$35 de produto, R$8 de embalagem, R$6 de pagamento e R$12 de operação), sobram **R$61**, e isso antes do CAC. Com CAC de R$70, a assinante só começa a dar lucro no 2º mês.

**O choque:** o preço que os compradores aceitam (~R$80) fica abaixo do custo por pedido (~R$83). Com envio mensal e esses custos, não existe preço que agrade os compradores e pague a operação.

## A saída: mudar o custo, não só o preço

O frete, o atendimento e a taxa de pagamento são cobrados **por envio**. Se a assinatura padrão enviar 3 refis a cada 3 meses (cobrança trimestral), esses custos caem para um terço:

| Plano trimestral | Custo por mês | Contribuição/mês | Ano 1 (antes de CAC) |
|---|---:|---:|---|
| R$129/mês, produto R$35 | R$64 | **R$65** | recupera o investimento no mês 12 |
| R$119/mês, produto R$35 | R$64 | R$55 | não recupera no ano 1 (−R$23 mil) |
| R$119/mês, produto R$25 | R$54 | R$65 | recupera no mês 12 |
| R$109/mês, produto R$35 | R$63 | R$46 | não recupera (−R$47 mil) |
| R$99/mês, produto R$25 | R$52 | R$47 | não recupera (−R$45 mil) |

(Rampa de 30 a 350 assinantes em 12 meses e R$7.500/mês de custo fixo + lançamento, conforme o documento. O "ano 1" da ferramenta não inclui o CAC.)

## 1. O preço recomendado

**Assinatura trimestral a R$129/mês por criança (R$387 a cada 3 meses).** Essa é a assinatura padrão.
- Fica dentro da faixa aceitável (até R$131), mas no topo, no ponto do "começa a ficar caro" para muitos. Isso é deliberado: a marca precisa justificar o preço, e não esconder a diferença.
- Sai ~2,2× o Alpha Kids por mês. É alto, e a diferença precisa vir do que o Alpha Kids não tem: garantia de sabor, transparência por lote e ritual.
- Contribuição de **R$65/mês** pela ferramenta, e o investimento volta no mês 12 se a rampa e os custos se confirmarem.

**A variável que mais pesa é o custo do produto.** Cada R$10 a menos no produto vale o mesmo que R$10 a mais no preço. Uma cotação real de fabricante decide se dá para descer para R$109–119.

## 2. A escada de preços

| Degrau | Preço | Por que existe |
|---|---|---|
| **Kit de teste** (7 doses, avulso, sem assinatura) | R$39 | Responde ao pedido mais repetido depois do pediatra: 41 de 100 queriam testar o sabor sem assinar. O valor é abatido do 1º trimestre. |
| **Mensal flexível** | R$149/mês | Para quem não quer se comprometer. Paga o frete mensal, e o preço mostra por que o trimestral compensa. |
| **Trimestral** (padrão) | **R$129/mês** (R$387/envio) | O plano que fecha a conta. Pode pausar ou cancelar antes do próximo envio. |
| **2º filho** (no trimestral) | R$99/mês | 35 compradores pediram desconto de irmão. O frete é compartilhado, então a contribuição fica em ~R$48. |

Recomendo não lançar o avulso de R$179 do documento. O kit de teste já cumpre esse papel, e três preços parecidos confundem (o conselho já pediu uma oferta só no lançamento).

## 3. A oferta de lançamento

**Kit de teste por R$39, abatido do 1º trimestre, com garantia de sabor:** se a criança não aceitar nas 2 primeiras semanas, você devolve o valor do 1º envio. Vale só para a pré-venda, com data de fim fixa. Não há desconto no preço de referência e não há "de R$X por R$Y" com um preço que nunca foi cobrado.

O custo do kit (produto, embalagem, frete) não está nos números. Se ele custar mais de R$39, a diferença é custo de aquisição e entra no CAC, e o `/founder-cfo` precisa contar isso.

## 4. O que testar com compradores reais

**Dois preços na mesma pré-venda, em duas páginas idênticas:** trimestral a **R$129** contra **R$109**, os dois com o kit de teste de R$39. Meça quantos pagam o kit (ou um depósito reembolsável) e quantos convertem para o trimestre.
- Se R$109 converter mais de 1,4× R$129, o R$109 ganha, **desde que** a cotação traga o produto para ≤ R$25.
- Abaixo de R$99 não testar: com os custos atuais, a margem não paga o CAC.

## 5. As objeções de preço do painel (para o marketing responder)

1. "Na farmácia tem por R$30, qual a diferença de verdade? Sem ver a lista de ingredientes, as quantidades de cada vitamina e o que usam para adoçar, não sei se estou pagando por fórmula melhor ou por frasco bonito e adesivo." (P005)
2. "E se ele cuspir igual cuspiu a última vitamina? Não vou pagar R$149 para descobrir, e o frasco com adesivo não muda o gosto." (P008)
3. "R$149 por criança por mês é caro demais para um multivitamínico, e assinatura sempre promete 'cancela quando quiser', mas na prática dá trabalho e eu acabo pagando meses sem usar." (P081)

Respostas que a oferta precisa ter: a fórmula completa no site, com dose, adoçante e comparação lado a lado; a garantia de sabor com o kit de teste; e o cancelamento em um clique, mostrado antes da compra.
