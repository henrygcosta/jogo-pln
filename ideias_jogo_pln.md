# Brainstorm — Jogo com IA Generativa (Projeto PLN)

Grupo de 3 estudantes. Prioridade: **simplicidade > uso inteligente da IA > originalidade > diversão > qualidade visual**.

---

## ETAPA 1 — 10 Ideias

### 1. O Interrogatório (Detetive de Mentiras)

**Conceito:** A IA gera um caso (crime + suspeito) com uma "verdade oculta" e uma "versão oficial" que o suspeito conta. O jogador interroga o suspeito por texto e precisa encontrar contradições para decidir se ele é culpado.

**Como o jogador joga:** Jogador → digita uma pergunta → IA responde como o suspeito (mantendo o personagem, mas com falhas plantadas) → jogador anota pistas → após N perguntas, jogador acusa e justifica → IA compara a acusação com a verdade oculta e dá o veredito.

**Onde entra a IA generativa:**
- *Entrada:* prompt inicial pedindo um caso (crime, suspeito, motivo, verdade oculta, versão oficial) +, a cada turno, a pergunta do jogador + histórico da conversa.
- *Processamento:* o modelo mantém um system prompt com a verdade oculta (invisível ao jogador) e instruções para responder em personagem, sendo evasivo mas plantando pequenas inconsistências quando pressionado.
- *Resposta gerada:* fala do suspeito em primeira pessoa, coerente com o personagem.
- *Influência no jogo:* as respostas são a única fonte de pistas; no final, uma chamada extra à IA (ou checagem simples de texto) compara a acusação do jogador com a verdade oculta gerada, produzindo o resultado (acertou/errou e por quê).

**Por que a IA é necessária:** sem geração de linguagem natural, não existiria personagem para interrogar — seria só um formulário de múltipla escolha. A IA permite perguntas livres e respostas coerentes e únicas a cada partida.

**Complexidade:** **3**

**Tecnologias:** Python, Streamlit (chat UI), API de LLM (Gemini/Groq free tier).

**Tempo estimado MVP:** 1 a 2 semanas.

**Diferencial:** mostra uso real de PLN (geração + manutenção de persona + extração/comparação de fatos), é fácil de demonstrar ao vivo e gera uma história diferente a cada partida.

---

### 2. Enigma Vivo (Charadas Adaptativas)

**Conceito:** A IA gera enigmas de dificuldade crescente, ajustando o próximo enigma conforme o desempenho do jogador.

**Como o jogador joga:** Jogador recebe enigma → digita resposta → IA avalia se está certa (mesmo com sinônimos/erros de digitação) → dá dica ou gera próximo enigma mais fácil/difícil.

**Onde entra a IA generativa:**
- *Entrada:* tema escolhido + histórico de acertos/erros.
- *Processamento:* gera um enigma novo e avalia a resposta do jogador por similaridade semântica (não exata).
- *Resposta gerada:* texto do enigma + feedback ("quase lá", "errou feio") + dica opcional.
- *Influência:* dificuldade adaptativa; sem repetição de enigmas prontos.

**Por que a IA é necessária:** permite enigmas infinitos e avaliação flexível de respostas (não precisa bater exatamente com um gabarito).

**Complexidade:** **2**

**Tecnologias:** Python, Streamlit, API de LLM.

**Tempo estimado MVP:** 3 a 5 dias.

**Diferencial:** extremamente rápido de implementar; bom "plano B" se o tempo apertar.

---

### 3. O Impostor entre Nós

**Conceito:** A IA controla vários "suspeitos" (personas) em um grupo, um deles é o impostor com um objetivo oculto. O jogador entrevista os personagens por texto e tenta descobrir quem é.

**Como o jogador joga:** Jogador escolhe com quem falar → digita pergunta → IA responde como aquele personagem específico (cada um com personalidade e informações diferentes) → jogador cruza informações → aponta o impostor.

**Onde entra a IA generativa:**
- *Entrada:* prompt gerando N personas com traços, relações e um impostor com objetivo secreto; depois, pergunta do jogador + qual persona está sendo interrogada.
- *Processamento:* o modelo alterna "papéis" mantendo consistência por personagem (cada um com seu próprio bloco de system prompt/contexto).
- *Resposta gerada:* fala do personagem selecionado.
- *Influência:* divergências entre relatos dos personagens são a pista central.

**Por que a IA é necessária:** múltiplas personas coerentes e reativas só são viáveis com geração de texto; sem IA seria preciso escrever manualmente dezenas de diálogos.

**Complexidade:** **4**

**Tecnologias:** Python, Streamlit, API de LLM.

**Tempo estimado MVP:** 2 a 3 semanas.

**Diferencial:** gameplay social dedution (tipo "Among Us" textual) é visualmente atraente para apresentação, mas exige gerenciar mais estado que as outras ideias.

---

### 4. Cartas do Destino

**Conceito:** Jogo de cartas narrativo: cada carta tem um tema, e a IA gera o texto de um evento de história toda vez que uma carta é jogada, continuando a narrativa anterior.

**Como o jogador joga:** Jogador puxa carta → carta tem palavra-chave (ex: "traição") → IA gera parágrafo de história incorporando a palavra e continuando o enredo → jogador decide próxima carta.

**Onde entra a IA generativa:**
- *Entrada:* palavra-chave da carta + resumo da história até então.
- *Processamento:* gera continuação narrativa coerente.
- *Resposta gerada:* parágrafo de história.
- *Influência:* a história muda completamente conforme as cartas puxadas.

**Por que a IA é necessária:** gera continuidade narrativa coerente a partir de palavras soltas, coisa que regras fixas não fariam bem.

**Complexidade:** **3**

**Tecnologias:** Python, Streamlit, API de LLM.

**Tempo estimado MVP:** 1 a 2 semanas.

**Diferencial:** visual de cartas é simples de fazer e bonito de mostrar; mecânica fácil de explicar.

---

### 5. Negociador Implacável

**Conceito:** O jogador negocia por texto com um vendedor/comprador controlado pela IA, que tem um preço-alvo oculto e uma personalidade (durão, ingênuo, etc.).

**Como o jogador joga:** Jogador envia proposta em texto → IA responde negociando, mantendo-se dentro de limites definidos (preço mínimo/máximo ocultos) → jogo termina quando acordo é fechado ou jogador desiste → sistema extrai o valor final acordado do texto.

**Onde entra a IA generativa:**
- *Entrada:* persona do NPC (personalidade, preço-alvo oculto) + mensagem do jogador + histórico.
- *Processamento:* gera resposta de negociação coerente com a persona e os limites; ao final, uma extração de informação identifica o valor combinado dentro da conversa.
- *Resposta gerada:* fala do NPC negociando.
- *Influência:* determina se o jogador "venceu" a negociação (conseguiu preço melhor que a média).

**Por que a IA é necessária:** simula um oponente de negociação flexível e reativo a argumentos, algo que árvores de diálogo fixas não replicam bem.

**Complexidade:** **3**

**Tecnologias:** Python, Streamlit, API de LLM.

**Tempo estimado MVP:** 1 a 2 semanas.

**Diferencial:** aplicação prática (soft skills de negociação), fácil de conectar com extração de entidades (PLN clássico).

---

### 6. Sobrevivente: Texto e Escolhas

**Conceito:** Aventura de sobrevivência pós-apocalíptica onde cada cena é gerada pela IA a partir das escolhas do jogador, com recursos (vida, comida) controlados em Python.

**Como o jogador joga:** Jogador lê cena → escolhe ação (texto livre ou opções) → IA gera a próxima cena e consequência → Python atualiza status (vida/recursos) → repete até fim.

**Onde entra a IA generativa:**
- *Entrada:* estado atual (vida, inventário) + ação escolhida.
- *Processamento:* gera cena seguinte coerente com o estado.
- *Resposta gerada:* narrativa + opções.
- *Influência:* narrativa nunca se repete.

**Por que a IA é necessária:** infinitas variações de história sem escrever um roteiro ramificado gigante à mão.

**Complexidade:** **3**

**Tecnologias:** Python, Streamlit, API de LLM.

**Tempo estimado MVP:** 1 a 2 semanas.

**Diferencial:** gênero popular (CYOA), fácil de entender, mas corre risco de parecer "só um ChatGPT com tema".

---

### 7. Repórter Investigativo

**Conceito:** Igual à ideia do interrogatório, mas com múltiplos suspeitos e retratos gerados por IA de imagem para cada um.

**Como o jogador joga:** Jogador recebe caso com fotos geradas dos suspeitos → entrevista cada um por texto → resolve o caso.

**Onde entra a IA generativa:**
- *Entrada:* descrição do suspeito.
- *Processamento:* gera imagem (retrato) + texto (diálogo).
- *Resposta gerada:* imagem + fala.
- *Influência:* engajamento visual + pistas textuais.

**Por que a IA é necessária:** combina texto e imagem para reforçar a investigação.

**Complexidade:** **5**

**Tecnologias:** Python, Streamlit, API de LLM + API de geração de imagem.

**Tempo estimado MVP:** 3 a 4 semanas.

**Diferencial:** visualmente mais impressionante, mas exige orquestrar duas IAs e mais estado (vários suspeitos) — maior risco de atraso.

---

### 8. Empresário por Um Dia

**Conceito:** O jogador faz um pitch de negócio por texto para um "investidor" IA com personalidade cética, que faz perguntas difíceis e dá uma nota final.

**Como o jogador joga:** Jogador descreve ideia → IA (investidor) questiona pontos fracos → jogador responde → ao final, IA dá parecer e nota de investimento.

**Onde entra a IA generativa:**
- *Entrada:* pitch do jogador + histórico.
- *Processamento:* gera perguntas críticas e avalia a qualidade das respostas (clareza, viabilidade).
- *Resposta gerada:* perguntas + parecer final com nota.
- *Influência:* nota final é o objetivo do jogo.

**Por que a IA é necessária:** simula um avaliador crítico e imprevisível, difícil de fazer com regras fixas.

**Complexidade:** **3**

**Tecnologias:** Python, Streamlit, API de LLM.

**Tempo estimado MVP:** 1 a 2 semanas.

**Diferencial:** aplicável a contexto educacional/empreendedorismo, mas mecânica parecida com "Negociador".

---

### 9. Duelo de Rimas

**Conceito:** Batalha de poesia/rima por texto: jogador escreve uma estrofe sobre um tema, a IA responde com sua própria estrofe (oponente) e depois atua como "jurado" pontuando ambas.

**Como o jogador joga:** Jogador recebe tema → escreve estrofe → IA gera estrofe rival → IA (papel de jurado) pontua rima, criatividade e coerência de ambas → repete por N rounds → vence quem tiver mais pontos.

**Onde entra a IA generativa:**
- *Entrada:* tema + estrofe do jogador.
- *Processamento:* gera contra-estrofe; em seguida avalia as duas com critérios definidos no prompt.
- *Resposta gerada:* estrofe do oponente + pontuação com justificativa curta.
- *Influência:* pontuação decide o vencedor de cada round.

**Por que a IA é necessária:** gera versos originais em tempo real e faz uma avaliação criativa (não binária) que regras fixas não conseguem.

**Complexidade:** **2**

**Tecnologias:** Python, Streamlit, API de LLM (opcional: TTS para "declamar" os versos).

**Tempo estimado MVP:** 3 a 5 dias.

**Diferencial:** leve, divertido, fácil de demonstrar ao vivo em sala (interativo com a plateia).

---

### 10. Quem Sou Eu, IA?

**Conceito:** A IA "pensa" em um personagem/objeto secreto; o jogador faz perguntas de sim/não (ou abertas) para adivinhar.

**Como o jogador joga:** IA sorteia/gera um personagem oculto → jogador pergunta → IA responde mantendo o segredo → jogador tenta adivinhar em N tentativas.

**Onde entra a IA generativa:**
- *Entrada:* pergunta do jogador + personagem oculto (guardado no backend).
- *Processamento:* responde de forma consistente sem revelar o segredo.
- *Resposta gerada:* resposta curta (sim/não/talvez).
- *Influência:* guia o processo de eliminação do jogador.

**Por que a IA é necessária:** gera personagens infinitos e responde perguntas abertas com coerência, coisa que uma lista fixa de 20 personagens não faria.

**Complexidade:** **2**

**Tecnologias:** Python, Streamlit, API de LLM.

**Tempo estimado MVP:** 3 a 5 dias.

**Diferencial:** extremamente simples, mas o uso de IA é mais raso que nos outros (risco de parecer pouco sofisticado).

---

## ETAPA 2 — Triagem

**Descartadas:**

- **Repórter Investigativo** — exige orquestrar 2 APIs de IA (texto + imagem) e múltiplos suspeitos em paralelo. Complexidade 5, custo maior, risco alto de atraso.
- **Sobrevivente: Texto e Escolhas** — gênero já muito comum de "demo de LLM"; risco real de parecer "ChatGPT com tema de sobrevivência" sem mecânica de jogo própria.
- **Cartas do Destino** — a mecânica de cartas em si não interage com a IA de forma profunda (a IA só narra); pouco "jogo", mais "gerador de texto com estética de carta".
- **Empresário por Um Dia** — conceito bom, mas muito redundante com "Negociador Implacável" (mesma estrutura de diálogo + avaliação); mantém-se apenas um dos dois.
- **Quem Sou Eu, IA?** — uso da IA é o mais raso do grupo (é essencialmente um oráculo de sim/não); interessante como protótipo de fim de semana, mas fraco para "uso inteligente de IA".

**Mantidas (5 finalistas):**

1. O Interrogatório (Detetive de Mentiras)
2. O Impostor entre Nós
3. Negociador Implacável
4. Duelo de Rimas
5. Enigma Vivo

---

## ETAPA 3 — Ranking

| Ideia | Originalidade | Uso da IA | Facilidade | Diversão | Aprovação | **Nota final** |
|---|---:|---:|---:|---:|---:|---:|
| O Interrogatório | 7 | 9 | 7 | 8 | 9 | **8,2** |
| O Impostor entre Nós | 8 | 9 | 5 | 8 | 8 | 7,7 |
| Negociador Implacável | 6 | 8 | 8 | 6 | 7 | 7,2 |
| Duelo de Rimas | 7 | 7 | 9 | 7 | 6 | 7,3 |
| Enigma Vivo | 5 | 6 | 9 | 6 | 6 | 6,3 |

*(Nota final pondera mais Facilidade e Uso da IA, conforme prioridade do grupo.)*

---

## ETAPA 4 — Ideia Vencedora

### 🏆 O Interrogatório (Detetive de Mentiras)

É a melhor relação **criatividade × IA × simplicidade** porque:

- A IA não é enfeite: ela **gera** o caso (personagem, motivo, verdade oculta) e **sustenta uma persona coerente** durante toda a conversa — isso é PLN de verdade (geração condicionada, manutenção de contexto, e no final, comparação/extração de informação entre a acusação do jogador e a verdade oculta).
- O estado do jogo é mínimo: 1 caso, 1 suspeito, N perguntas, 1 acusação final. Nada de múltiplos NPCs, imagens ou física.
- É fácil de demonstrar ao vivo: o professor pode literalmente jogar uma rodada em 5 minutos.
- Cada partida é diferente (a IA gera um caso novo), o que evita a sensação de "sistema decorado".

---

## ETAPA 5 — Simplificação Agressiva

### Versão ideal (se tivéssemos tempo/recursos)
Múltiplos casos com dificuldades variadas, vários suspeitos por caso, retratos gerados por IA de imagem, sistema de pontuação com ranking, dicas adaptativas conforme o desempenho do jogador, histórico de partidas salvo em banco de dados, modo multiplayer (um jogador é o suspeito controlado por outro humano vs. IA).

### MVP acadêmico (o que vamos desenvolver)
- 1 caso gerado por partida (crime + suspeito + verdade oculta + versão oficial), criado uma única vez no início via chamada à IA.
- Interrogatório por texto livre, limitado a um número fixo de perguntas (ex: 8).
- Ao final, o jogador escreve sua acusação (culpado/inocente + motivo).
- Uma chamada final à IA compara a acusação com a verdade oculta e devolve um veredito com explicação.
- Interface única em Streamlit (chat + botão de acusação final).

### Protótipo mínimo (prova de conceito)
- Um único caso fixo ou gerado uma vez no início da sessão.
- Loop de chat simples (mesmo em terminal, sem Streamlit) entre jogador e suspeito via chamada de API com system prompt contendo a verdade oculta.
- Sem limite de perguntas, sem pontuação — só provar que a IA consegue **manter a persona** e **plantar inconsistências reconhecíveis**.
- Isso já prova o conceito central do jogo.

---

## ETAPA 6 — Arquitetura Simples

```
Jogador (navegador)
   │
   ▼
Interface Streamlit (chat + botão "Acusar")
   │
   ▼
Python (estado do jogo: histórico da conversa,
        verdade oculta gerada, nº de perguntas restantes)
   │
   ▼
API de LLM (Gemini / Groq)
   │  ├─ Chamada 1 (início): gera o caso e a verdade oculta
   │  ├─ Chamadas seguintes: responde como o suspeito
   │  └─ Chamada final: compara acusação x verdade oculta
   ▼
Resposta em texto
   │
   ▼
Interface Streamlit (mostra fala do suspeito ou veredito final)
```

**O que precisamos desenvolver:**
1. Prompt de geração do caso (formato estruturado: crime, suspeito, motivo real, versão oficial).
2. Prompt de persona do suspeito (mantém personagem, evasivo, plantável de inconsistência).
3. Prompt de julgamento final (compara acusação do jogador com a verdade oculta).
4. Interface simples em Streamlit com chat + contador de perguntas + botão de acusação.

Nenhum banco de dados, nenhuma autenticação, nenhuma infraestrutura além de rodar o app localmente/Streamlit Cloud.

---

## ETAPA 7 — Exemplo de Partida

1. **Jogador inicia o jogo.** IA gera (nos bastidores, oculto): *"Suspeito: Marcos, dono de uma loja. Verdade: ele roubou o cofre do sócio para pagar uma dívida de jogo. Versão oficial: diz que estava em casa dormindo."*

2. **Jogo mostra:** "Marcos, dono da loja, está sendo interrogado sobre o roubo do cofre. Você tem 8 perguntas."

3. **Jogador digita:** *"Onde você estava na noite do roubo?"*

4. **Pergunta é enviada à IA** junto com o system prompt contendo a verdade oculta e a instrução de responder como Marcos, sem revelar a verdade diretamente.

5. **IA responde (em personagem):** *"Eu estava em casa, dormindo. Nem saí de lá a noite toda."*

6. **Jogador insiste:** *"Um vizinho disse que viu sua caminhonete saindo às 23h. Como explica isso?"*
   → IA responde ficando visivelmente na defensiva, talvez se contradizendo levemente: *"Ah... isso, eu... fui só dar uma volta rápida, não tem nada a ver com o roubo."*

7. **Após as 8 perguntas**, jogador escreve a acusação: *"Acuso Marcos. Ele mentiu sobre estar em casa e ficou nervoso quando perguntei sobre a caminhonete — acho que ele tinha uma dívida e precisava de dinheiro."*

8. **IA compara** a acusação com a verdade oculta gerada no passo 1 e responde: *"Correto! Marcos realmente roubou o cofre para pagar uma dívida de jogo. Você identificou a contradição certa. Pontuação: 9/10."*

9. **Jogador pode iniciar uma nova partida** — a IA gera um caso completamente novo.

---

## ETAPA 8 — Estrutura de Apresentação (5 slides)

### Slide 1 — Problema/Conceito
- **Colocar:** frase de impacto ("E se você pudesse interrogar um suspeito que nunca conta a mesma história duas vezes?"), nome do jogo, 1 imagem/ícone temático (lupa, sala de interrogatório).
- **Não colocar:** texto longo, detalhes técnicos.
- **Visual:** fundo escuro estilo "sala de interrogatório", tipografia de destaque.
- **Falar oralmente:** motivação do projeto — jogos tradicionais de dedução são estáticos; queremos um jogo onde a IA cria histórias e personagens novos a cada partida.

### Slide 2 — Como o Jogo Funciona
- **Colocar:** diagrama simples do loop (Jogador → Pergunta → IA responde como suspeito → Acusação final → Veredito).
- **Não colocar:** código ou prompts completos.
- **Visual:** fluxograma de 4 caixas com setas.
- **Falar oralmente:** regras básicas (número de perguntas, objetivo do jogador).

### Slide 3 — Como a IA Generativa é Utilizada
- **Colocar:** os 3 momentos em que a IA é chamada (gerar caso → sustentar persona → julgar acusação), com 1 frase por momento.
- **Não colocar:** prompt bruto extenso (pode citar 1 trecho curto como exemplo).
- **Visual:** os 3 momentos como ícones/etapas numeradas.
- **Falar oralmente:** por que isso é PLN de verdade — geração condicionada, manutenção de contexto/persona e comparação semântica de texto (não é só "perguntar pro ChatGPT").

### Slide 4 — Exemplo de Gameplay
- **Colocar:** print (ou mock) de uma pergunta e resposta reais do protótipo, ou o exemplo de partida resumido em 3-4 falas.
- **Não colocar:** transcrição inteira do interrogatório.
- **Visual:** print de tela do chat ou "mockup" simulando a interface.
- **Falar oralmente:** narrar a cena, mostrando como a contradição aparece naturalmente na conversa.

### Slide 5 — MVP e Viabilidade
- **Colocar:** lista curta do escopo do MVP (1 caso por partida, chat com limite de perguntas, veredito automático), tecnologias usadas (Python, Streamlit, API de LLM), tempo estimado (1-2 semanas).
- **Não colocar:** arquitetura técnica detalhada ou stack completo.
- **Visual:** checklist ou linha do tempo curta.
- **Falar oralmente:** por que é viável para 3 pessoas em pouco tempo — poucas telas, poucas chamadas de API, sem infraestrutura extra.
