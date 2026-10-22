# Operação — Rotulim (nome provisório)

Base: `idea.md`, `offer.md` e `numbers.json` (trimestral R$129, Kit Teste R$39, ~316 assinantes no mês 12, ou seja, ~105 envios trimestrais por mês mais os kits). **Nenhum fornecedor abaixo foi cotado.** São pontos de partida para você pedir orçamento, e por isso o `numbers.json` **não mudou**: os custos continuam sendo as estimativas do documento. Quando chegarem as cotações, atualize os números e rode o `/founder-cfo` de novo.

## 1. O ciclo de cada dia

(👁 = o cliente vê)

1. **Pedidos entram** (loja + plataforma de assinatura): kits avulsos e cobranças trimestrais do dia. 👁 *e-mail de confirmação*
2. **Conferência de cobranças falhas** (cartão recusado): a régua de cobrança tenta de novo. 👁 *e-mail "atualize seu cartão"*
3. **Separação**: kit (frasco de 7 doses + cartão + Ficha para o Pediatra) ou envio trimestral (3 refis, e frasco e cartão se for o 1º envio). Cada pacote registra o **número do lote**.
4. **Embalagem e etiqueta** pelo agregador de frete. 👁 *código de rastreio*
5. **Postagem ou coleta** (Correios ou transportadora).
6. **Atendimento** (WhatsApp/e-mail): dúvidas de uso, pedidos de garantia de sabor, pausas e trocas de data. 👁
7. **CRM automático**: o dia 1, o dia 4 e o dia 7 do kit, e o aviso de cobrança 7 dias antes. 👁
8. **Fechamento do dia**: estoque por lote, devoluções e reclamações registradas (com lote, sintoma e ação).

Com ~100–150 pacotes por mês no ano 1, isso cabe em **1 a 2 horas por dia de operação própria**. A referência pública diz que a operação interna é eficiente abaixo de ~100 pedidos/mês ([Shopify](https://www.shopify.com/br/blog/fulfillment-no-e-commerce)). Avalie um operador logístico (3PL) quando passar de ~300 envios/mês.

## 2. Fornecedores (todos precisam de cotação)

| Item (linha do CFO) | Onde procurar | Por que | Pedir na cotação |
|---|---|---|---|
| **Produto e terceirização** (R$35, o item mais importante) | [Naturelab](https://ensun.io/search/private-label-vitamin-supplement/brazil) (SP, terceirização de suplementos) · [Hilê/ClinicMais](https://naturaltech.com.br/hile-e-clinicmais-25-anos-de-experiencia-no-mercado-de-suplementos-alimentares) (400+ fórmulas de marca própria) · [Promel](https://www.folhavitoria.com.br/economia/industria-capixaba-produz-nutraceuticos-para-terceirizacao/) (ES, 300+ nutracêuticos) · associação [ABMAPRO](https://www.abcdacomunicacao.com.br/private-label-avanca-no-brasil-e-pressiona-industria-a-se-reinventar-no-varejo-farmaceutico/) para mais nomes | Nenhum deles **confirma publicamente que faz comprimido mastigável infantil**. É a 1ª pergunta | Faz mastigável? Para criança de 4–8 anos? **Lote mínimo** (unidades e R$), prazo, preço por 30 doses em 3 volumes, quem faz a notificação, laudos inclusos, **opções de adoçante** (o painel rejeita sucralose), estabilidade e validade, condição de pagamento |
| **Laudos independentes** (contaminantes, microbiologia, teor) | [Eurofins Brasil](https://www.eurofins.com/pt-br/testes-de-alimentos-e-racoes/servicos/residuos-e-contaminantes/metais-e-elementos/) (metais: chumbo, arsênio, cádmio, mercúrio) · [TÜV SÜD Brasil](https://www.tuvsud.com/pt-br/industrias/produtos-de-consumo-e-varejo/alimentos/microscopia-de-alimentos) (60+ métodos ISO 17025) · confira a acreditação no [Inmetro/Cgcre](https://www.gov.br/inmetro/) | É a promessa da marca ("laudo de cada lote") | Preço por lote do pacote metais + micro + teor de vitaminas, prazo, e se o laudo pode ser publicado |
| **Frasco com tampa à prova de criança** e **refil (sachê/pouch)** | Fornecedores de embalagem farmacêutica em SP (peça indicação ao terceirizador, que costuma ter parceiros homologados) | A tampa resolve o "vira doce"; o refil barateia o trimestral | Preço por mil, lote mínimo, compatibilidade com a fórmula (umidade), arte inclusa? |
| **Frete** (R$15, ÷ 3 no trimestral) | [Melhor Envio](https://melhorenvio.com.br/transportadora-jadlog) (agrega Correios e Jadlog) · [SuperFrete](https://superfrete.com/como-enviar-encomendas) | O **Mini Envios** dos Correios aceita até 300 g e 4×16×24 cm. **Os refis provavelmente cabem**, e isso pode baixar o frete abaixo de R$15 | Simule com o peso e a medida reais do kit e do envio de 3 refis, de SP para as 5 capitais |
| **Gateway de assinatura** (R$6/cobrança) | [Iugu](https://www.b2bstack.com.br/compare/iugu-vs-vindi) (plano a partir de ~R$49/mês segundo o comparador) · [Pagar.me](https://www.b2bstack.com.br/compare/pagar-me-vs-vindi) · [Vindi](https://www.b2bstack.com.br/compare/vindi-vs-iugu) (a partir de ~R$1.399/mês, caro demais para o começo) | Cobrança trimestral recorrente, Pix e régua de cobrança | Taxa por transação no cartão, taxa de recorrência, antecipação e custo de chargeback. Os preços dos comparadores podem estar desatualizados |

**Perguntas abertas (só a cotação responde):** custo real por 30 doses, lote mínimo (se passar de R$25 mil, o caixa do `cfo.md` estoura), prazo do 1º lote, frete real dos refis.

## 3. Pessoas

| Papel | Quem | Horas | Custo |
|---|---|---|---|
| Fundadora: produto, marketing, pediatras, creators | você | tempo integral | **pró-labore não está nos números** (o documento também deixa de fora). Decida quanto precisa tirar e some ao fixo |
| **Responsável técnico** (nutricionista ou farmacêutico com experiência em suplementos) | contratado | ~8–16 h/mês | dentro dos R$5.500/mês de fixo (estimativa); peça proposta |
| Consultoria regulatória | projeto | antes do lançamento | dentro dos R$18 mil de regulatório |
| Operação e atendimento | fundadora no mês 1; freelancer de meio período quando passar de ~150 pacotes/mês | 10–20 h/semana | **estimativa a confirmar:** referência de mercado para auxiliar de e-commerce em SP |
| Contador | escritório | mensal | dentro do fixo |

**Escala na semana** (mês 1 e mês 12):
- **Seg–sex, 9h–11h:** separação, embalagem, postagem e atendimento. No mês 12, com o freelancer: 9h–13h.
- **Ter e qui à tarde:** visitas a consultórios e contato com creators.
- **Sex à tarde:** reposição, revisão dos números da semana e conteúdo.

Os encargos além do salário (INSS, FGTS, férias, 13º, ou o modelo de prestação de serviço) variam conforme o contrato. **Leve ao contador.**

## 4. Rotinas (uma página cada)

**R1: Abrir o dia**
1. Abrir o painel da loja e da assinatura e listar os pedidos e cobranças do dia.
2. Conferir as cobranças recusadas (a régua de cobrança já mandou e-mail? escalar quem passou de 3 tentativas).
3. Conferir o estoque por lote: há o suficiente para os envios de hoje e dos próximos 14 dias?
4. Responder a todas as mensagens da noite antes das 10h.

**R2: Separar e enviar**
1. Imprimir as etiquetas pelo agregador de frete.
2. **Kit:** frasco de 7 doses + cartão de adesivos + Ficha para o Pediatra impressa.
3. **1º envio trimestral:** frasco de 30 doses (tampa à prova de criança) + 3 refis + cartão de 30 adesivos.
4. **Envios seguintes:** 3 refis + cartão novo.
5. Anotar o **número do lote** de cada pacote na planilha ou no sistema. Sem isso não existe recolhimento possível.
6. Lacrar, etiquetar e postar até as 11h.

**R3: Reclamação ou garantia de sabor**
1. Responder em até 4 horas úteis com o modelo de `brand.md`: devolver primeiro e perguntar depois.
2. Devolver pelo mesmo meio de pagamento no mesmo dia. **Não pedir o produto de volta.**
3. Registrar o lote, a idade da criança, o que ela achou (sabor, textura, tamanho) e o canal de origem.
4. **Se a reclamação for de saúde** (reação, alergia, ingestão acidental de várias doses): **não diagnosticar.** Orientar a procurar o pediatra ou o CIATox, avisar o RT **no mesmo dia** e registrar o lote. Duas reclamações de saúde do mesmo lote: o RT avalia se aciona o plano de recolhimento.

**R4: Fechar o dia**
1. Baixar no estoque o que foi enviado, por lote.
2. Lançar as devoluções e garantias do dia.
3. Conferir se o CRM do dia saiu (dias 1, 4 e 7 dos kits e os avisos de cobrança).

**R5: Reposição semanal (sexta)**
1. Somar os envios previstos das próximas 8 semanas (as renovações trimestrais estão no sistema).
2. Comparar com o estoque. Se a cobertura for menor que o **prazo do fabricante mais 4 semanas**, pedir.
3. Conferir a validade: enviar sempre o lote mais antigo primeiro e nunca enviar com menos de 6 meses de validade.
4. Rever os 3 números da semana (`marketing.md`): custo por kit, kit → assinatura e cancelamento.

## 5. Ferramentas (o mínimo)

| Função | Opções | Por que |
|---|---|---|
| Loja + assinatura | Nuvemshop ou Shopify com app de assinatura, **ou** a página de pagamento da Iugu ou do Pagar.me | Precisa de cobrança trimestral, pausa e cancelamento em 1 clique. Teste o fluxo de cancelamento antes de escolher |
| Frete | Melhor Envio ou SuperFrete | Etiqueta com desconto e Mini Envios |
| CRM / e-mail / WhatsApp | ferramenta de e-mail com automação + WhatsApp Business | Sequência do kit e aviso de cobrança |
| Estoque por lote | planilha no mês 1, sistema de gestão (ERP) quando passar de ~300 envios/mês | Rastrear o lote é obrigação, não luxo |
| Contabilidade e nota fiscal | contador + emissor de NF-e | Venda de produto exige nota fiscal |

Não consegui abrir as páginas de preço da Nuvemshop, da Shopify e dos gateways daqui (bloqueio de rede). Confira os preços atuais nos sites oficiais. O custo deles está dentro dos R$5.500 de fixo estimado.

## 6. Licenças, registros e seguros (checklist)

As regras mudam e variam por município e estado. **Confirme cada item com o órgão ou com o consultor regulatório e o contador.** Isto não é aconselhamento jurídico.

- [ ] **CNPJ** com CNAE de comércio de alimentos e suplementos (Receita Federal, [gov.br/empresas](https://www.gov.br/empresas-e-negocios/pt-br)) e **inscrição estadual** (ICMS na venda de produto).
- [ ] **Notificação do suplemento na Anvisa** (RDC 843/2024 e IN 281/2024, documentos do Anexo X). Defina com o terceirizador **quem é a empresa detentora** da notificação. Base: [Mattos Filho](https://www.mattosfilho.com.br/unico/anvisa-regularizacao-alimentos/) e o [aviso da Anvisa sobre o prazo de adequação](https://legismap.com.br/conteudos/artigos-e-noticias/noticias-anvisa-em-01-09-2026). A **RDC 243/2018** (constituintes, limites e alegações por faixa etária) e a **RDC 727/2022** (rotulagem) continuam valendo.
- [ ] **Licença sanitária municipal** (Vigilância Sanitária) se você armazenar e expedir o produto. Confirme com a VISA do seu município se a sua atividade exige.
- [ ] **Responsável técnico** formalmente designado, se a VISA ou o modelo de notificação exigir.
- [ ] **Plano de recolhimento de alimentos.** Confirme a norma vigente com o consultor: a referência usual é a RDC 655/2022.
- [ ] **Código de Defesa do Consumidor**: direito de arrependimento de 7 dias em compra online (art. 49), cancelamento de assinatura tão fácil quanto a contratação, e preço total do trimestral (R$387) claro antes do pagamento.
- [ ] **LGPD com dados de crianças**: idade, nome no cartão e foto em post exigem **consentimento específico de um dos pais** (art. 14). Colete o mínimo.
- [ ] **Registro da marca no INPI**, classes 5 e 35 (`brand.md`).
- [ ] **Seguro de responsabilidade civil de produto**, que cobre reclamação de dano à saúde. Cote com uma corretora.
- [ ] **Revisão regulatória de cada peça de marketing** antes de publicar.

## 7. Registro de riscos

| # | Risco | Chance | Impacto | Plano |
|---|---|---|---|---|
| 1 | **Nenhum terceirizador faz mastigável infantil no lote mínimo que cabe no caixa** | média | **alto** | Cotar com 3 ou mais antes de gastar com marca. Plano B: outro formato (pó em sachê ou minicápsula), testado no painel antes de decidir |
| 2 | **Fórmula ou alegação reprovada**, ou exigência na notificação | média | alto | Consultor regulatório **antes** do design final (já no plano). Nenhuma alegação que não esteja na IN de constituintes autorizados |
| 3 | **Criança rejeita o sabor** (nota < 4,2) | média | **alto** | Teste de sabor com protótipo antes do lote. O Kit Teste filtra quem rejeita antes de assinar. Plano de reformulação acordado com o fabricante |
| 4 | **Incidente de saúde** (reação ou ingestão acidental) | baixa | **muito alto** | Tampa à prova de criança, rotina R3, RT no mesmo dia, rastreio por lote, plano de recolhimento e seguro de responsabilidade civil |
| 5 | **CAC acima de R$100** | média | alto | Metas semanais (`marketing.md`). Cortar o canal que passar de R$30 por kit. Pediatras e indicação como canais de baixo custo |
| 6 | **Estoque acaba** ou atrasa o refil (a assinatura perde a confiança) | média | alto | Rotina R5 com prazo do fabricante + 4 semanas. Avisar o cliente antes, nunca depois |
| 7 | **Estoque vence parado** (lote mínimo grande e venda lenta) | média | médio | Lote pequeno. Nunca enviar com menos de 6 meses de validade. Kits de amostra para pediatras usam o lote mais antigo |
| 8 | **Falha na cobrança recorrente** (cartões recusados, gateway fora do ar) | média | médio | Régua de cobrança com 3 tentativas + Pix. Ter um 2º gateway configurado |
| 9 | **Reclamação pública** (Reclame Aqui, Instagram) | alta | médio | Responder em até 4 horas, devolver primeiro e publicar o laudo do lote. Transparência é a marca |
| 10 | **Fundadora fica doente ou sem tempo** (operação de uma pessoa só) | média | médio | Rotinas escritas (seção 4), um freelancer treinado a partir do mês 3 e respostas automáticas para as dúvidas comuns |

**O que mudou nos números:** nada ainda, porque não há cotação real. **Duas lacunas que o CFO precisa incluir** quando houver dados: o **pró-labore** da fundadora (fora do modelo) e o **seguro de responsabilidade civil**.
