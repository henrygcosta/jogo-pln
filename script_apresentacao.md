# Script de Apresentação (versão falada, informal)
## O Interrogatório — Detetive de Mentiras

> Script corrido, pra ler em voz alta e depois deixar mais "seu". Segue a ordem dos 6 slides do pptx. Tem sugestão de divisão entre os 3 integrantes no final, mas dá pra uma pessoa só apresentar tudo também.

---

### Abertura / Slide 1 — Conceito

Oi, gente. A gente vai apresentar um projeto de jogo com IA que a gente chamou de O Interrogatório.

A ideia surgiu de uma pergunta meio boba, mas que a gente achou bem legal: e se você pudesse interrogar um suspeito que **não segue um roteiro**? Tipo, você pergunta o que quiser, do jeito que quiser, e ele responde na hora, como se fosse uma pessoa de verdade sendo interrogada.

É basicamente isso: um jogo de dedução em que você bate um papo — de verdade, por texto — com um suspeito controlado por IA, tentando descobrir o que ele tá escondendo."

*(mostra o slide com o exemplo de conversa)*

"Óó, é mais ou menos assim: você pergunta 'onde você estava na noite do crime?' e o suspeito responde 'eu estava em casa'. Só que, spoiler, ele tá mentindo — e a graça do jogo é descobrir isso."

---

### Slide 2 — Como funciona

"Beleza, e como que isso funciona na prática?

Toda partida começa com a IA criando um caso do zero: um crime, um suspeito, uma mentira — tudo novo, ninguém escreveu isso à mão. Você recebe só o básico: o que aconteceu, onde, quando e quem é o suspeito.

Daí você tem **6 perguntas**. Só isso, 6 — a gente escolheu esse número porque dá tempo suficiente pra investigar direito, mas não fica arrastado. Você vai perguntando, prestando atenção nas hesitações, nas contradições...

E no final, você precisa responder três coisas: qual foi a mentira dele, o que realmente aconteceu, e qual foi o motivo. Aí o jogo te fala se você acertou ou não."

---

### Slide 3 — Onde a IA entra

"Agora a parte que eu acho mais bacana, que é onde a IA realmente entra — porque isso aqui não é só um chat bonitinho, sabe?

A IA trabalha em **três momentos** diferentes.

Primeiro, **antes do jogo começar**: ela monta o caso inteiro escondido — a verdade, a versão que o suspeito vai contar, a mentira, o motivo. Isso tudo fica guardado, o jogador não vê nada.

Depois, **durante o interrogatório**, ela 'vira' o suspeito e responde suas perguntas. E aqui tem um detalhe importante: a cada resposta, a gente reenvia pra ela os fatos do caso de novo. Por quê? Porque se a gente deixasse ela solta, ela ia começar a inventar coisa aleatória, ia se contradizer sem sentido nenhum. Então a gente meio que 'prende' ela nos fatos que já foram definidos, pra ela ficar coerente a partida toda.

E no final, uma IA compara o que você respondeu com a verdade real do caso — mesmo que você tenha escrito com outras palavras — e é o código, não a IA, que calcula sua pontuação.

Então assim: a IA não tá ali de enfeite. Ela cria, ela interpreta e ela avalia. Ela é o motor do jogo mesmo."

---

### Slide 4 — Onde está o PLN

"E cadê o PLN nisso tudo, já que é esse o foco da disciplina, né?

Olha só: quando você digita uma pergunta do seu jeito, com suas palavras, a IA precisa **entender** o que você quis dizer — isso é compreensão de linguagem natural. A resposta que ela gera pro suspeito **não é livre**, ela é condicionada aos fatos que já definimos — isso é geração condicionada. Ela precisa **manter a conversa coerente** do início ao fim — isso é processamento de diálogo. E na hora de avaliar, ela reconhece quando você disse a mesma coisa com palavras diferentes — isso é comparação semântica.

Ou seja, não é só 'a gente chamou uma API de IA e pronto'. Tem PLN de verdade acontecendo em cada uma dessas etapas."

---

### Slide 5 — Exemplo de partida

"Deixa eu mostrar rapidinho como isso fica na prática, com um exemplo.

*(lê a transcrição do slide, com um pouco de teatro na voz do suspeito)*

'Onde você estava às 22h?' — 'Eu estava em casa.' Aí você já sacou que a chave dele foi usada pra entrar no local, então você pergunta de novo, mais na cara: 'mas sua chave foi usada pra entrar no local'. E ele: 'eu... posso ter passado lá rapidinho'.

Viu? Achou a contradição. Aí você acusa: ele mentiu que ficou em casa, na verdade ele entrou lá com a própria chave, e o motivo era precisar de dinheiro. Resultado: 3 de 3."

---

### Slide 6 — MVP e viabilidade

"E pra fechar: a gente sabe que é fácil empolgar com a ideia e ela crescer descontroladamente, então a gente foi bem rígido no que vai entrar na primeira versão.

O MVP é literalmente isso: **uma tela**, **um suspeito**, **6 perguntas**, **3 respostas no final** e um resultado de 0 a 3. Só isso. Sem login, sem ranking, sem banco de dados, sem multiplayer — nada disso é necessário pra provar que a ideia funciona, então a gente cortou tudo isso fora de propósito.

A stack também é simples: Python, Streamlit pra interface, e uma API de LLM.

E olhando de forma realista: a gente é em três, e dá pra ter esse MVP rodando em **1 a 2 semanas**. Não é papo, o escopo foi desenhado exatamente pra caber nesse tempo."

---

### Fechamento

"Resumindo: é uma ideia simples de explicar, simples de desenvolver, mas que usa IA generativa de um jeito que faz sentido de verdade — não é só decoração. A gente acha que dá pra entregar isso com qualidade tranquilamente.

*(pausa)*

Descubra a mentira. Encontre a verdade. Bora pra perguntas!"

---

## Sugestão de divisão entre os 3 (opcional)

- **Pessoa 1:** Abertura + Slide 1 (Conceito) + Slide 2 (Como funciona)
- **Pessoa 2:** Slide 3 (Onde a IA entra) + Slide 4 (PLN)
- **Pessoa 3:** Slide 5 (Exemplo de partida) + Slide 6 (MVP/viabilidade) + Fechamento

Cada bloco dá mais ou menos 40-50 segundos falado no ritmo normal — a apresentação toda fica em torno de 4 a 5 minutos, com espaço de sobra pra perguntas.
