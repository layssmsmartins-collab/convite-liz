# Nota do CFO — Marca Kids Premium

> Leia assim: a ferramenta mostra o volume "por dia" e usa "$". Aqui a unidade é **assinante-mês**, então multiplique o "por dia" por 30 para ter assinantes ativos (11 por dia ≈ 316 assinantes), e "$" quer dizer **R$**. **Todos os custos são estimativas**, principalmente as do documento original, sem cotação de fabricante (veja `cfo-sources.md`). Isto não é aconselhamento financeiro, contábil ou tributário: um contador precisa validar o regime tributário (Simples Nacional ou outro), os 8% de tributos e a estrutura antes de qualquer dinheiro sair.

**Como montei a rampa:** pelo funil, não por palpite. O orçamento de aquisição é de R$4.000/mês. Cada Kit Teste custa R$30 (R$25 de mídia ou creator + R$5 de prejuízo do kit), 30% dos kits viram assinatura e saem 8% dos assinantes por mês (o teto do documento). Isso dá **CAC de R$100 por assinante** e uma base de 40 → 316 assinantes em 12 meses. O painel justifica o ponto de partida (50% comprariam o kit na versão 2), mas **a taxa kit → assinatura de 30% é palpite**: o painel deu 0% de assinatura imediata, e todos condicionaram ao pediatra.

## A margem
- **Contribuição: R$62,82 por assinante-mês** (49% do preço), depois de produto, frete, embalagem, pagamento, operação, tributos, garantia e tampa.
- **Ponto de equilíbrio: ~151 assinantes ativos**, com custo fixo de R$9.500/mês (R$5.500 de operação + R$4.000 de aquisição).
- **Margem de lucro no mês 12 (316 assinantes): 25%.**
- **Ano 1:** R$305 mil de receita e **R$34,5 mil de lucro operacional**. Depois dos R$76 mil de investimento inicial, o resultado é **−R$41,5 mil**. O dinheiro não volta no ano 1.

## A linha que mais pesa: o CAC
| Cenário | Assinantes no mês 12 | Ano 1 depois do investimento | Volta em | Caixa necessário |
|---|---:|---:|---|---:|
| **Base** (CAC R$100, saída 8%/mês) | 316 | **−R$41,5 mil** | depois do mês 12 | **R$90,8 mil** |
| CAC R$70 (a meta do documento) | 452 | **+R$22,2 mil** | mês 11 | R$84,5 mil |
| Ruim (CAC R$150, saída 12%/mês) | 174 | **−R$102,8 mil** | — | **R$105,9 mil** (estoura os R$100 mil) |
| Metade do marketing (R$2.000/mês) | 158 | −R$91,7 mil | — | R$98,4 mil |

O que prova a sensibilidade: **preço −10% derruba o lucro operacional do ano 1 de R$34,5 mil para R$4 mil**, e **volume −20% para R$4,8 mil**. A folga é pequena. Cortar marketing também não salva o caixa: com metade do orçamento, a base não passa do ponto de equilíbrio a tempo.

## Caixa
**São necessários ~R$91 mil antes de o negócio se pagar no cenário base.** Cabe nos R$100 mil, mas sobram só ~R$9 mil de folga (fora a reserva de R$5 mil que já está no investimento). No cenário ruim faltam ~R$6 mil.
- *A favor (não modelado):* o trimestral é cobrado adiantado (R$387 no 1º mês), o que melhora o caixa dos primeiros meses frente ao que está na tabela.
- *Contra (não modelado):* o primeiro lote mínimo pode ser maior que R$25 mil, e o fabricante pode exigir pagamento antecipado.

## Três jeitos de melhorar a margem (cada um rodado na ferramenta)
1. **Baixar o CAC de R$100 para R$70**, com indicação de pediatras e nutricionistas, programa de indicação entre pais e creators pagos por resultado. Ano 1 depois do investimento: **−R$41,5 mil → +R$22,2 mil**, e o dinheiro volta no mês 11. É a alavanca maior.
2. **Produto de R$35 para R$25 com uma cotação real.** Contribuição R$62,82 → **R$72,82**, ano 1 depois do investimento **−R$41,5 mil → −R$17,8 mil**, e o equilíbrio cai para ~130 assinantes.
3. **Preço de R$129 para R$139.** Mesmo efeito do item 2: contribuição **R$72,82** e ano 1 **−R$17,8 mil**. Só que o painel já põe o teto aceitável em ~R$131, então é arriscado. Prefira a alavanca 2.

Bônus que não mexe na margem, mas mexe no caixa: **gastar R$12 mil em identidade em vez de R$20 mil** (o documento recomenda no máximo R$20–25 mil antes de provar a demanda). São R$8 mil a menos de caixa necessário.

## As condições de dinheiro do conselho (`board.md`)
- [ ] **Contribuição ≥ R$70/pedido:** **não atendida.** Fica em R$62,82 na base e só chega a R$72,82 com o produto a R$25 ou o preço a R$139.
- [ ] **CAC < R$70:** **não medida.** A base supõe R$100, e só a pré-venda dirá o número real.
- [ ] **Custo unitário em cotação de fabricante:** **não atendida.** Os R$35 continuam hipótese.
- [x] **Liberar só os primeiros R$25 mil:** compatível. O caixa necessário mostra que gastar tudo de uma vez não deixa margem para errar.

---

# Unit economics: Marca Kids Premium (nome provisório) — trimestral R$129/mês + Kit Teste

Every number below comes from the input file. Nothing is looked up or guessed.

## One assinante-mês (1 criança, plano trimestral)

| line | per assinante-mês (1 criança, plano trimestral) |
| --- | ---: |
| Price | $129.00 |
| Tributos e perdas fiscais (8% do preço) — estimativa do documento | -$10.32 |
| Frete (R$15 por envio trimestral ÷ 3) — estimativa | -$5.00 |
| Produto e terceirização (30 doses) — estimativa, sem cotação | -$35.00 |
| Embalagem/refil — estimativa | -$8.00 |
| Pagamento (R$6 por cobrança trimestral ÷ 3) — estimativa | -$2.00 |
| Atendimento/picking/perdas (R$12 por envio ÷ 3) — estimativa | -$4.00 |
| Garantia do 1º envio (5% × ~R$193, em 6 meses) — estimativa | -$1.61 |
| Tampa à prova de criança (diluída) — estimativa | -$0.25 |
| **Contribution** (what each assinante-mês (1 criança, plano trimestral) leaves to pay the fixed costs) | **$62.82** (49%) |

## The margin that matters

Fixed costs: $9,500 a month (Operação fixa: ferramentas, RT, contador, armazenagem, conteúdo (R$66 mil/ano: R$90 mil do documento menos R$24 mil de lançamento) — estimativa $5,500, Aquisição: creators, mídia, Kit Teste (orçamento mensal) — estimativa $4,000).

- **Break-even: 6 assinante-mês (1 criança, plano trimestral)s a day.** Below that you lose money every month.
- **Profit margin at your plan** (11 a day): **25%** of every sale, after every cost.
- Capacity: 66.67 a day.

## Year 1, month by month

| month | assinante-mês (1 criança, plano trimestral)s a day | revenue | profit | cumulative (after $76,000 startup) |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 1 | $5,159 | -$6,988 | -$82,988 |
| 2 | 3 | $9,907 | -$4,675 | -$87,663 |
| 3 | 4 | $14,276 | -$2,548 | -$90,211 |
| 4 | 5 | $18,293 | -$591 | -$90,802 |
| 5 | 6 | $21,989 | $1,208 | -$89,594 |
| 6 | 7 | $25,391 | $2,865 | -$86,729 |
| 7 | 7 | $28,518 | $4,388 | -$82,342 |
| 8 | 8 | $31,397 | $5,790 | -$76,552 |
| 9 | 9 | $34,044 | $7,079 | -$69,473 |
| 10 | 9 | $36,482 | $8,266 | -$61,207 |
| 11 | 10 | $38,723 | $9,357 | -$51,850 |
| 12 | 11 | $40,786 | $10,362 | -$41,488 |

- **Year 1 operating profit: $34,512** on $304,968 of revenue.
- After the $76,000 startup spend: -$41,488.
- Startup money earned back: not within year 1.
- Cash you need before it pays for itself: **$90,802**.

## What if

| scenario | margin at plan | break-even a day | year 1 profit |
| --- | ---: | ---: | ---: |
| Base plan | 25% | 6 | $34,512 |
| Price -10% | 17% | 7 | $4,015 |
| Volume -20% | 20% | 6 | $4,810 |
| Unit costs +15% | 18% | 6 | $11,044 |

## Red flags

- The startup spend is not earned back within year 1.
