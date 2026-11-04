---
name: formula-review
description: Avalia uma fórmula de suplemento alimentar (rótulo, ficha técnica, catálogo ou proposta) para mulheres na perimenopausa com uma única pergunta, respondida por queixa e olhando a fórmula inteira, não ingrediente por ingrediente: "uma mulher com esta queixa, tomando isto todo dia, resolve a queixa?". Também roda ao contrário: dado um conjunto de queixas, monta a fórmula que teria chance real de resolvê-las, dentro do que a Anvisa permite. Use sempre que a fundadora enviar foto de rótulo, tabela nutricional, ficha de fabricante, página de catálogo, lista de ingredientes com doses, ou perguntar "essa fórmula é boa?", "isso funciona?", "o que essa concorrente tem?", "o que eu coloco na minha fórmula?", "quanto de magnésio precisa?", ou qualquer comparação entre fórmulas (Períssima, SL 023, Menopausei, Dose Day, PRATIC, Ourocaps, Nutrion, Personalize, Ekobé etc.), mesmo que ela não peça "avaliação". Não use para precificação, marca ou canal; para isso há as skills founder-*.
---

# formula-review: a fórmula resolve a queixa?

## Por que esta skill existe

A fundadora da Períssima descobriu, depois de semanas de trabalho, que a avaliação anterior de fórmulas estava errada de um jeito específico: ela dava meio ponto para "ter o ingrediente" mesmo em dose que nenhum estudo usou, somava pontos por ingrediente e chegava a notas como 63/100 para fórmulas que uma mulher não sentiria. O erro custou uma decisão de MVP. Esta skill nasce para que isso não se repita.

A mulher na perimenopausa tem sintomas que ela percebe todo dia: dorme mal, esquece palavras, fica irritada, cansa. Ela compra para parar de sentir isso. Se em quatro semanas não mudou, ela não recompra, e tem razão. Então a única pergunta que importa é a dela: **resolveu?**

## A régua

### A pergunta, por queixa, olhando o todo

Para cada queixa que a fórmula promete (ou que o público-alvo tem), responda: **uma mulher de 35 a 52 anos com esta queixa, tomando esta fórmula como indicado por 4 a 8 semanas, tem chance razoável de perceber que a queixa diminuiu?**

A resposta é um veredito, não um número:

| Veredito | Significa |
|---|---|
| **Resolve** | A fórmula contém uma intervenção (um ingrediente ou uma combinação estudada) com evidência de ensaio clínico randomizado ou meta-análise, em população parecida (mulheres de meia-idade, ou a queixa em adultos), em dose igual ou acima da menor dose que mostrou efeito, sem nada na mesma fórmula que anule. O efeito esperado é pelo menos moderado em relação ao placebo. |
| **Ajuda em parte** | Há algo real, mas: a dose está na borda inferior; ou a evidência é de estudos pequenos; ou o efeito só aparece em quem tem deficiência (vitamina D, B12, ferro); ou o efeito é pequeno. A mulher pode sentir alguma coisa, mas não é a maioria. |
| **Não resolve** | Nada em dose eficaz. Os ingredientes "para" a queixa estão em dose simbólica, ou a evidência é de laboratório, ou de outra população. O que ela sentir é placebo, e placebo em sono e humor chega a 30 a 40% das pessoas, então depoimentos não contam. |
| **Atrapalha** | A fórmula contém algo que piora a queixa (cafeína, guaraná ou taurina em dose de energético para quem dorme mal; estimulante para quem tem ansiedade). |

Dê o veredito **por queixa**, nunca uma nota única para a fórmula. Uma fórmula pode resolver cansaço e não resolver sono. É assim que a mulher vive, e é assim que a marca vai ser cobrada.

### Recalibração (04/11/2026): as três premissas e a âncora da escala

A primeira versão desta régua pesava a mão: ancorava o "10" em efeito de medicamento, julgava todo produto contra as queixas da Períssima (mesmo produtos de beleza ou de esporte) e chamava de "placebo" o que a cliente sente. Isso fazia tudo parecer "não funciona". A fundadora apontou, com razão, que uma marca séria não vende placebo e que existe uma premissa legal diferente da clínica. A régua passa a perguntar três coisas, nesta ordem:

1. **Premissa legal: tem o mínimo para alegar?** No Brasil um suplemento "serve para" algo só com as frases do Anexo V da IN 28, e a condição é ter, na dose diária, pelo menos o mínimo do Anexo III (≈15% do VD para vitaminas e minerais; o mínimo definido para cada bioativo). Não se exige estudo. Um produto que cumpre isso é legal e honesto: é o padrão da indústria séria (Puravida, Essential), e vale nota 5 a 6 contra a própria promessa, não zero.
2. **Premissa clínica: tem a dose que os estudos usaram, para a cliente sentir?** É o que separa "pode alegar" de "a mulher percebe". Dose abaixo do piso dos estudos continua contando zero **para a queixa**, mas conta para a premissa 1.
3. **Premissa da brasileira A/B: repõe o que ela tem baixo contra o alvo da medicina atual?** Vitamina D (alvo 40 a 60), magnésio, ômega 3, colina, selênio e B12 estão abaixo na maioria mesmo com renda (`references/brasileira-ab-estado-nutricional.md`). Repor em dose plena é "ajuda a maioria", não "ajuda se deficiente".

Regras que decorrem disso:
- **A âncora do 10 é "o melhor que um suplemento legal consegue entregar para essa queixa, em dose real, para a maioria das clientes"**, não "cura". Com essa âncora, a fórmula v2 da Períssima fica perto de 8,5; um multivitamínico honesto, 5 a 6; uma fórmula de nomes em dose simbólica, 3 a 4.
- **Primeiro a nota contra a promessa do próprio produto; depois, separada, "e para a mulher da Períssima?".** Um café de energia e beleza não tira nota baixa por não tratar sono; ele tira nota pelo que promete, e à parte se diz o que faz para a perimenopausa.
- **Linha "benefício percebido esperado"**, que soma três coisas legítimas: correção de lacuna da A/B, ativo em dose de estudo, e ritual e expectativa (30 a 40% em sono e humor). A ciência desconta a terceira; a cliente e a recompra não. O relatório diz as três, separadas.
- **Vocabulário:** sai "não funciona", "placebo", "pó de fada"; entra "faz X, não faz Y" e "dose abaixo do estudo". "Simbólico" fica reservado a dose abaixo do mínimo legal ou abaixo de 20% do piso de estudo.
- Os limiares de dose não mudam: vêm dos estudos dos próprios ingredientes (ch-OSA 10 mg, Lactium 300 mg, magnésio 250 a 300). Quando um rótulo traz 7% disso, é fato, não rigor.

### Olhar o todo, não o ingrediente

A avaliação é da fórmula inteira. Isso muda a leitura em cinco pontos:

1. **Some o que age pelo mesmo mecanismo.** Magnésio bisglicinato 200 mg + magnésio dimalato 100 mg é 300 mg de magnésio (elementar; veja conversão abaixo). Glicina e magnésio para sono se somam; triptofano e 5-HTP competem pela mesma via.
2. **Conte a combinação só se ela foi estudada ou se o mecanismo é claramente aditivo.** "Dez ativos para o sono" em dose simbólica cada um não viram um ativo em dose real. Dose simbólica vezes dez continua simbólica.
3. **Procure o que anula.** Cafeína à noite anula magnésio para sono. Ferro e cálcio atrapalham a absorção de zinco e magnésio na mesma dose. Fibra fermentável em 3 a 4 g causa gases nas primeiras semanas e derruba a adesão.
4. **Veja o que a fórmula faz pela mulher como um todo.** Se ela dorme melhor, a névoa mental e a irritabilidade melhoram sem nenhum "nootrópico". Uma fórmula que resolve o sono pode "ajudar em parte" em memória e humor por via indireta; diga isso e marque como indireto.
5. **Se o efeito depende de deficiência, diga de quem.** Vitamina D em 2.000 UI muda a vida de quem tem 15 ng/mL e nada na de quem tem 40. No Brasil, deficiência de D e de B12 é comum em mulheres de 40+; isso vale "ajuda em parte", não "resolve".

### O que não entra na régua

Formato (pó, cápsula, goma), sabor, preço, marca, embalagem e adesão não entram no veredito. Entram, quando relevante, como observação separada no fim, porque uma fórmula que resolve mas exige 6 cápsulas por dia tem um problema que não é de fórmula.

## Como ler um rótulo

Antes de julgar, extraia a fórmula com cuidado. Rótulos brasileiros de terceirizador erram com frequência; dois erros já encontrados nesta pasta:

- **Coluna de %VD deslocada uma linha** (o percentual impresso ao lado de um nutriente pertence ao de baixo ou ao de cima). Confira: calcule o %VD de dois ou três nutrientes com os VD de adulto (IN 28 / RDC 429) e veja onde os números batem.
- **"Não contém fibra" e 3 g de fibra na tabela.** Contradições internas indicam revisão fraca do fabricante, e valem anotação de risco.

Regras de leitura:

1. Trabalhe sempre **por dose diária indicada**, não por 100 g. Se a porção é 5 g e o pote tem 150 g, são 30 doses.
2. **Converta sal em elementar** quando o rótulo não diz: magnésio bisglicinato tem cerca de 14% de magnésio; magnésio dimalato cerca de 15%; óxido 60%; citrato 16%; zinco bisglicinato cerca de 20%. Se o rótulo diz "magnésio (mg) 63", é elementar; se diz "magnésio bisglicinato 500 mg", é sal, e o elementar é ~70 mg. Na dúvida, apresente as duas leituras e diga qual assumiu.
3. **Extrato versus pó da planta.** "Feno-grego em pó 200 mg" é semente moída; os estudos usam extrato padronizado em dose e marcador definidos. Não são a mesma coisa.
4. **Lecitina de soja não é isoflavona.** Para contar como fitoestrógeno, o rótulo precisaria declarar isoflavonas em mg.
5. **Forma química** muda a leitura (metilfolato vs ácido fólico; metilcobalamina vs cianocobalamina; bisglicinato vs óxido). Anote a forma, mas não dê veredito por forma; a forma afeta a dose eficaz, e é a dose que decide.
6. Registre **o que o rótulo não diz** (dose de um ingrediente listado só nos ingredientes; marcador do extrato; grupo populacional; número de notificação). Ausência é informação.

## Onde está a evidência

Há duas bases, e a ordem de leitura importa.

**1. Os guias da fundadora** (`references/guias-fundadora.md`, índice consolidado; extrações completas em `references/guias/`, uma por guia, com dose e página; os PDFs originais em `founder/mercados/memoria-40/guias/`). São 48 guias clínicos da Dra. Priscila Antunes (Comunidade Saúde Conectada) que a fundadora decidiu tratar como **fonte de verdade**. Leia `guias-fundadora.md` inteiro antes de qualquer veredito. Onde ele contradiz a literatura, **o guia prevalece**, e o relatório anota a divergência numa linha ("guia diz X; literatura diz Y; usei X"). Se precisar da dose exata ou do contexto de um guia, abra a extração correspondente em `references/guias/`.

Decisão da fundadora (04/11/2026) que enquadra tudo: **a Períssima é um suplemento de prateleira, uma fórmula única, para venda; não vende consulta nem depende de exame.** A clínica é soberana e os sintomas da perimenopausa não aparecem em exame, o que é característico da fase. Por isso os alvos de exame dos guias (ferritina, B12, D, TSH, homocisteína) **não entram no veredito nem condicionam a fórmula**; podem aparecer, no máximo, numa linha de "Fora da régua" como conteúdo educativo. Calorão fica fora por ora.

Duas regras dos guias que mudam a leitura de qualquer fórmula:
- **Poucos ativos, por fase, com horário.** A autora usa 2 a 3 suplementos por 3 meses e rotaciona; separa manhã (energia: dimalato, CoQ10), 16h (teanina, chá) e noite (magnésio com glicina, glicina, fosfatidilserina). Uma fórmula "tudo em um, uma vez ao dia" contraria os guias; prefira dia/noite.
- **Inflamação, intestino e fígado como causa.** Despertar entre 1 e 4 h, "acorda cansada mesmo dormindo", vontade de doce à tarde, pavio curto: os guias leem isso como inflamação, cortisol e metilação antes de ler como "falta de ingrediente". O relatório deve dizer quando a queixa pede esse caminho, não um suplemento.

**2. Os dossiês de literatura**, que dão os limiares de dose dos ensaios clínicos, as populações estudadas, o tamanho de efeito e a resposta ao placebo. Leia o dossiê de cada queixa que a fórmula promete ou que o público tem. Não decida de memória: a memória foi exatamente o que falhou antes.

| Queixa | Arquivo |
|---|---|
| Dormir mal, acordar de madrugada; cansaço que o sono não resolve | `references/sono-cansaco.md` |
| Esquecer palavras, fio da meada, névoa mental; concentração | `references/memoria-concentracao.md` |
| Irritabilidade, impaciência, oscilação de humor; ansiedade | `references/humor-ansiedade.md` |
| Ondas de calor; ganho de peso e inchaço; libido | `references/calorao-peso-libido.md` |
| O que a Anvisa permite: constituintes, limites para 19+, alegações, o que é proibido dizer | `references/regulatorio-brasil.md` |
| Dose que funciona × dose legal, por queixa; o teto do que uma fórmula brasileira consegue; a fórmula-base do modo inverso | `references/matriz-legal-eficaz.md` |

Leia primeiro `matriz-legal-eficaz.md`: é curta e diz, por queixa, o que é alcançável, o que fica na borda, o que é inalcançável por lei e o que é proibido. Os dossiês por queixa dão a evidência e os números por trás; o regulatório dá a norma e o que ainda não foi confirmado.

Duas verdades que os dossiês deixaram claras e que o relatório precisa carregar:
- **Para sono, memória, irritabilidade, cansaço e ansiedade, o teto legal no Brasil é "Ajuda em parte".** Os ingredientes com efeito moderado ou grande (ashwagandha, açafrão, lavanda Silexan, triptofano em 1 g, curcumina em 500 mg) estão proibidos ou têm máximo legal abaixo do piso dos estudos. Uma fórmula brasileira honesta promete melhora pequena, perceptível para parte das mulheres, em 4 a 8 semanas. Dar "Resolve" a uma fórmula brasileira para essas queixas exige evidência que hoje não existe; se um dia aparecer, atualize o dossiê.
- **A alegação "o zinco auxilia na função cognitiva" não foi encontrada no Anexo V da IN 28** por dois pesquisadores independentes, embora conste na ficha técnica da Ourocaps. Trate como "a confirmar com o RT", não como permitida.

Cada dossiê termina com um "Resumo para a régua" que diz o mínimo que uma fórmula precisa ter para aquela queixa. Use esse mínimo como piso do veredito "Resolve". Se o dossiê diz "não encontrado" para um ingrediente ou dose, diga "não checado" no relatório; não preencha com opinião.

Quando a fórmula tiver um ingrediente que nenhum dossiê cobre, pesquise na web em fonte primária (PubMed, meta-análise) antes de julgar, cite o link, e anote no fim do relatório que o dossiê precisa ser atualizado.

## Formato de saída

Use sempre esta estrutura. A fundadora lê isso para decidir onde pôr dinheiro; ela precisa achar o veredito em dez segundos e a justificativa em dois minutos.

```
# Avaliação: [nome da fórmula] ([fonte: rótulo / ficha / catálogo / proposta], [data])

## Veredito por queixa
| Queixa | Veredito | Por quê, em uma linha | O que teria de mudar |
|---|---|---|---|
| Dormir mal | Não resolve | magnésio 63 mg e triptofano 200 mg: ambos abaixo do piso dos estudos (300 mg e 1 g) | magnésio ≥300 mg + glicina 3 g, ou triptofano ≥1 g |
| ... | | | |

## O que uma mulher deve esperar sentir
[3 a 5 linhas honestas: o que a maioria sentirá, o que só quem tem deficiência sentirá, o que é placebo. Esta é a frase que a marca não pode escrever no rótulo, mas que a fundadora precisa saber.]

## A fórmula, lida
[Tabela: ingrediente | forma | dose por dia (elementar quando aplicável) | %VD 19+ | para qual queixa foi colocado | dose mínima com efeito nos estudos (com o dossiê de origem) | leitura: real / borda / simbólico / sem evidência]

## O todo
[O que se soma, o que anula, o que é indireto, o que depende de deficiência. 1 parágrafo.]

## O que os guias da fundadora dizem sobre esta fórmula
[Onde a fórmula segue ou contraria as regras dos guias: horário, número de ativos, forma do magnésio, exame prévio, o que a autora receitaria para estas queixas e não está aqui. Divergências guia × literatura usadas no veredito, uma linha cada.]

## Regulatório (Brasil)
[Constituinte fora da lista? Dose acima do máximo para 19+? Alegação proibida na comunicação? Erro de rótulo? Cada item com a norma e o que falta confirmar com o RT.]

## Fora da régua
[Formato, adesão, gosto, preço, lote: só o que for relevante.]

## Não checado
[Tudo o que não deu para confirmar: dose não declarada, dossiê sem o ingrediente, norma não aberta.]
```

Escreva em português do Brasil, direto, sem adjetivos de marketing. "Fraco" e "simbólico" são palavras permitidas; "excelente" não ajuda ninguém.

## Modo inverso: das queixas para a fórmula

Quando a pergunta for "o que eu coloco na fórmula?", faça o caminho contrário:

1. Liste as queixas-alvo em ordem de prioridade (na Períssima, pela pesquisa de 71 mulheres: dormir mal 72%, esquecer palavras 70%, irritabilidade 66%, cansaço 62%, ansiedade 61%, concentração 52%, peso 52%, libido 39%, calor 17%).
2. Para cada queixa, pegue da `matriz-legal-eficaz.md` o que é **alcançável dentro da lei** e dá "Resolve" ou, se não existir (é o caso das cinco queixas principais), o melhor "Ajuda em parte", e diga qual dos dois é. Nunca proponha o que está "não permitido" ou "inalcançável", mesmo com evidência boa; cite-o na lista do que ficou de fora e por quê.
3. Monte a fórmula somando, e depois **leia o todo**: elimine competição, cheque interações, some o que age junto, veja o volume por dose (2,9 g de glicina + 2,3 g de sal de magnésio + 3 g de creatina já são 8 g: é pó, não cápsula).
4. Passe cada ingrediente pelo `references/regulatorio-brasil.md`: dose entre o mínimo e o máximo para 19+ (creatina é 3 g exatos; fibra só conta a partir de 5,7 g); que alegação sobra; que advertência entra. Marque o que precisa de confirmação do RT.
5. Entregue a fórmula com a mesma tabela da seção "A fórmula, lida", mais o veredito esperado por queixa, mais uma lista do que **não** dá para resolver com suplemento e precisa de médico (terapia hormonal, ISRS, TCC-i), porque a marca precisa dizer isso com honestidade.

## Armadilhas que esta skill existe para evitar

- **Somar pontos por ingrediente.** Dez nomes em dose simbólica não valem um em dose real. O veredito é por queixa, olhando o todo.
- **Meio ponto por "ter".** Abaixo da dose mínima dos estudos, o ingrediente conta zero para a queixa. Pode contar para outra coisa (rotulagem, nutrição de base), e isso vai em "Fora da régua" ou em "Ajuda em parte, se deficiente".
- **Confiar em depoimento.** Em sono, humor e cansaço, 30 a 40% do grupo placebo melhora. Depoimento não distingue.
- **Confundir população.** Estudo em idosos com declínio cognitivo não vale para mulher de 42 com névoa mental. Estudo em insônia clínica vale em parte para "acordo de madrugada". Diga de onde veio a evidência.
- **Confundir "permitido" com "funciona".** A alegação da Anvisa ("o zinco auxilia na função cognitiva") é o que o rótulo pode dizer, não evidência de que 5 mg de zinco resolvem a névoa mental.
- **Esquecer o teto.** Para calorão e para humor perimenopausal, a terapia hormonal e os antidepressivos têm efeito muito maior que qualquer suplemento. O relatório deve dizer isso quando a queixa é dessas, para que a marca nunca prometa o que só a médica resolve.
