# Oferta — Marca Kids Premium

Método: a lente Offers (resumo de um framework publicado, em `founder-board/lenses.md`). Matéria-prima: as objeções do painel de 100 (`founder/panel/results.md`), as reclamações dos concorrentes (`founder/competitors.md`) e os custos de `founder/numbers.json`.

## 1. Lista de problemas (na voz do comprador)

**Antes de comprar**
1. "O pediatra não pediu isso." (o bloqueio nº 1: 76 de 100 disseram que a indicação do pediatra mudaria a decisão)
2. "Meu filho come bem, será que precisa?"
3. "Marca nova que eu nunca ouvi falar, para dar todo dia ao meu filho?"
4. "Só vende pelo site, não consigo comparar na prateleira."
5. "Na farmácia tem por R$30, qual a diferença de verdade?"
6. "Não vejo a dose de cada vitamina nem a lista de ingredientes."
7. "'Sem açúcar adicionado' pode querer dizer adoçante que eu não quero."
8. "Quem é esse laboratório do QR code? Qualquer um põe um QR code."
9. "E se ele cuspir? Já perdi dinheiro com vitamina."
10. "R$149 por criança, e com dois filhos vira R$300."
11. "Assinatura sempre dá trabalho para cancelar."
12. "Não quero assinar sem testar."
13. "Nenhuma criadora que eu sigo usa."

**Durante o uso**
14. "Mastigável vira doce e ele vai pedir mais de um."
15. "O irmão mais novo vai querer também."
16. "A rotina de manhã já é corrida, é mais uma coisa para lembrar."
17. "Esqueço de repor e fico sem."
18. "E se a entrega atrasar?"

**Depois**
19. "Depois de um mês ele enjoa do sabor."
20. "Não vejo diferença nenhuma no meu filho, para que continuar?"
21. "Cobrança que chega sem eu lembrar."
22. "E se a marca mudar a fórmula ou sumir?"

## 2. Soluções, pontuadas (valor 1–5 · custo 1–5) e cortadas

| Problema | Solução | Valor | Custo | Fica? |
|---|---|:-:|:-:|:-:|
| 1, 2, 3 | **Ficha para o Pediatra**: fórmula, doses por idade e laudo do lote, para levar na consulta | 5 | 1 | ✅ |
| 5, 6, 7 | **Fórmula completa publicada** com dose, adoçante e comparação lado a lado com as marcas de farmácia | 5 | 1 | ✅ |
| 9, 12 | **Kit Teste de 7 doses por R$39**, sem assinatura | 5 | 2 | ✅ |
| 9 | **Garantia de sabor** (devolução dos R$39 do kit; devolução do 1º envio em até 30 dias) | 5 | 2 | ✅ |
| 11, 21 | **Pausa/cancelamento em 1 clique** + aviso 7 dias antes de cada cobrança | 4 | 1 | ✅ |
| 14, 15 | **Tampa à prova de criança** + cartão com 1 adesivo por dia | 4 | 1 | ✅ |
| 10 | **2º filho a R$99/mês** no trimestral | 4 | 2 | ✅ (já em pricing) |
| 17 | Trimestral com 3 refis num envio | 3 | 1 | ✅ (já em pricing) |
| 8 | Nome do laboratório e número do laudo no frasco e no site | 4 | 1 | ✅ (no núcleo) |
| 13 | Criadoras usando de verdade | 4 | 3 | ➡️ marketing |
| 19 | 2º sabor | 3 | 4 | ❌ depois da prova de recompra (o documento pede um SKU) |
| 20 | "Resultado visível" | 4 | — | ❌ **proibido**: não há alegação permitida que prometa isso a uma criança |
| 1 | Consulta com nutricionista inclusa | 4 | 5 | ❌ caro, e arrisca parecer prescrição (o documento desaconselha) |
| 22 | Aviso por e-mail antes de qualquer mudança de fórmula | 3 | 1 | ✅ (nos termos) |

## 3. A oferta

**Nome: "Teste de 7 Dias"**, a porta de entrada. A assinatura vem depois.

- **Núcleo:** uma dose diária que a criança aceita, com tudo à vista. O comprimido mastigável é sem açúcar adicionado e sem corante artificial. A fórmula fica publicada lado a lado com as de farmácia, e cada lote tem laudo de laboratório nomeado. A comunicação é "complementa a alimentação; não é remédio", sem nenhuma promessa de resultado.
- **Bônus 1, Ficha para o Pediatra:** ataca "o pediatra não pediu" e "será que precisa?". Não pede ao médico que prescreva. Dá ao pai o material para perguntar.
- **Bônus 2, Tampa à prova de criança + cartão de 1 adesivo/dia:** ataca "vira doce, ele vai pedir mais de um".
- **Bônus 3, Aviso 7 dias antes de cada cobrança + cancelamento em 1 clique:** ataca "assinatura dá trabalho para cancelar".
- **Garantia:** se a criança não aceitar o sabor do kit, devolvemos os R$39. Se deixar de aceitar no 1º envio da assinatura, devolvemos o valor em até 30 dias.
- **Urgência real:** o primeiro lote é pequeno e vendido em pré-venda. Não tem contagem regressiva nem "restam 3".
- **Depois do kit:** trimestral a R$129/mês (R$387 a cada 3 meses, com os R$39 do kit descontados), 2º filho a R$99/mês, ou mensal a R$149.

## 4. Quanto custa a pilha (ferramenta do CFO)

Rodei `unit_economics.py` com os extras somados ao custo por mês. As estimativas estão marcadas como estimativas.

| | Antes da pilha | Com a pilha |
|---|---:|---:|
| Custo variável/mês (trimestral R$129) | R$64,32 | R$66,18 |
| Contribuição/mês | R$64,68 | **R$62,82** |
| Ano 1 depois do investimento (antes de CAC) | +R$215 | **−R$4.565** |

Os extras modelados foram a garantia do 1º envio (5% de acionamento × ~R$193, diluído em 6 meses = R$1,61/mês) e a tampa à prova de criança (R$0,25/mês). A pilha custa ~R$1,86/mês e empurra a recuperação do investimento um pouco para depois do mês 12.

O **Kit Teste dá prejuízo e é custo de aquisição**. Estimo ≈ R$36 por kit (7 doses ≈ R$8, embalagem ≈ R$4, frete R$15, pagamento R$2, separação R$4, tributos R$3) mais 20% de devoluções (≈ R$8), contra R$39 cobrados. São ≈ **R$5 de prejuízo por kit**, e isso entra no CAC no `/founder-cfo`. Se a taxa de kit → assinatura for baixa, esse custo se multiplica por cada assinante conquistado.

## 5. Equação de valor (1–10, antes → depois)

| Elemento | Antes | Depois | O que mexeu |
|---|:-:|:-:|---|
| Resultado dos sonhos | 4 | 5 | Pouco. A regulação não deixa prometer resultado, então o "sonho" vira rotina tranquila e confiança. |
| Probabilidade percebida | 3 | 6 | Fórmula publicada, laudo nomeado, Ficha para o Pediatra, garantia de sabor |
| Tempo até o resultado | 5 | 7 | Kit de 7 dias: em uma semana o pai sabe se a criança aceita |
| Esforço e sacrifício | 4 | 7 | Kit sem assinatura, cancelamento em 1 clique, aviso antes da cobrança, tampa à prova de criança |

## 6. Reteste (`/founder-consumer --quick`, 20 compradores, semente 20502)

| | v1 (painel de 100) | v2 (20, nova oferta) |
|---|---:|---:|
| Compram algo | **6%** (assinatura) | **50%** (10 de 20) |
| …dos quais **assinam já** | 6% | **0%**: os 10 compram só o Kit Teste de R$39 |

**Leitura honesta:**
- **A oferta mexeu no primeiro passo.** Metade topa pagar R$39 para testar. A garantia de sabor e o "sem assinatura" foram citados por quase todos que compraram.
- **A assinatura não mexeu.** Quase todos os compradores do kit condicionam a assinatura a duas coisas: a criança aceitar a semana inteira e **o pediatra aprovar a Ficha**. Dois deles dizem que não assinam nem assim por causa do preço (P013, P014).
- **Continuam em 0%:** "Segue o pediatra" (0 de 4) e "Já usa um concorrente" (0 de 3). O primeiro grupo nem compra o kit antes da consulta, e o segundo já está satisfeito com o Alpha Kids ou o Lavitan.
- **Objeção nova que apareceu:** o adoçante. Três compradores disseram que desistem se o site mostrar sucralose ou outro adoçante artificial. **Isso é decisão de fórmula**, para levar ao formulador antes de fechar o produto.
- As amostras são diferentes: o v2 tem 20 cartas e o v1 tem 100, então as pessoas não são as mesmas. Os números são finos (as linhas marcadas "thin" no resultado têm 2–4 pessoas). Use como direção, não como medida.

**Conclusão:** o problema da assinatura não é a oferta, é a **recomendação profissional** e o **preço contra o Alpha Kids**. A oferta põe o pai na porta, e a taxa de kit → assinatura é o número que a pré-venda real precisa medir. Se ela ficar abaixo de ~30%, o custo por assinante explode.

Arquivos: `founder/pitch.md` (v2), `founder/pitch-v1.md` (original) e `founder/panel-v2/`.
