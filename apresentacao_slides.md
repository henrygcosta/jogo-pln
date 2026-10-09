# O Interrogatório — Detetive de Mentiras
## Especificação da Apresentação (6 slides)

> Versão navegável (dark, estilo dossiê/terminal) publicada como artifact — use como referência visual para reproduzir em PowerPoint/Canva.

Direção visual adotada: fundo quase-preto (#10131a), texto off-white, um único acento âmbar (#e8a33d) usado com moderação, tipografia grotesca para títulos e monoespaçada para rótulos/dados (efeito "ficha de caso"/terminal). Sem gradientes, sem ícones pictóricos, sem animação além de scroll simples. Cada slide abre com uma legenda no formato "0X / 06 — SEÇÃO", que também serve de índice.

---

### Slide 1 — O Conceito

**Título:** O Interrogatório
**Subtítulo:** Detetive de Mentiras
**Frase de impacto:** "Descubra a mentira. Encontre a verdade."

**Texto exato adicional:**
```
Investigador: "Você estava onde na noite do crime?"
Suspeito: "Eu estava em casa."
```

**Layout:** título grande centralizado à esquerda no topo, subtítulo em destaque logo abaixo (cor de acento), frase de impacto em tom secundário, e um pequeno bloco de transcrição (2 linhas: investigador/suspeito) na parte inferior, como uma citação de exemplo.

**Elementos visuais:** nenhum ícone; o próprio bloco de diálogo já comunica o conceito.

**Ícones/imagens:** dispensável — o slide funciona só com tipografia.

**Explicar oralmente:** que o jogo é uma conversa livre por texto com um suspeito de IA, e que cada partida gera um caso novo.

---

### Slide 2 — Como Funciona

**Título:** Como funciona

**Texto exato:**
```
Caso gerado → 6 perguntas → Análise das pistas → Acusação → Resultado

6 perguntas para descobrir
[A mentira]  [A verdade]  [O motivo]
```

**Layout:** fluxograma horizontal de 5 caixas conectadas por setas, ocupando a largura do slide; abaixo, um rótulo curto e três marcadores lado a lado.

**Elementos visuais:** caixas com borda fina (sem preenchimento chamativo), setas tipográficas simples (→), três marcadores/tags retangulares pequenos.

**Ícones/imagens:** nenhum — os marcadores textuais substituem ícones.

**Explicar oralmente:** o ciclo de uma partida do início ao fim, reforçando que são só 6 perguntas antes da decisão final.

---

### Slide 3 — Onde a IA Entra

**Título:** Onde a IA entra

**Texto exato:**
```
01 — Gera
Cria o caso completo — verdade, versão oficial, mentira e motivo — tudo oculto do jogador.

02 — Interpreta
Responde como o suspeito, revisando os fatos do caso a cada resposta para manter a versão coerente.

03 — Avalia
Compara a resposta do jogador com a verdade real, mesmo escrita com outras palavras.

IA generativa como motor do jogo
A IA não é apenas um chatbot: ela gera, mantém e avalia o contexto da partida.
```

**Layout:** três blocos lado a lado (numerados 01/02/03), largura igual, com título curto e 1 frase de descrição cada; abaixo, uma frase de destaque centralizada e uma legenda menor.

**Elementos visuais:** divisores finos entre os três blocos; número em cor de acento no canto superior de cada bloco.

**Ícones/imagens:** nenhum necessário — a numeração já organiza visualmente.

**Explicar oralmente:** este é o slide-chave — insistir que os três momentos são etapas técnicas reais (geração estruturada, diálogo restrito a fatos, avaliação semântica), não só "chamar um chatbot".

---

### Slide 4 — Onde Está o PLN

**Título:** Onde está o PLN

**Texto exato:**
```
Pergunta do jogador
↓
Compreensão da linguagem
↓
Resposta do suspeito
↓
Comparação semântica
↓
Avaliação

— Geração de linguagem
— Compreensão de linguagem natural
— Geração condicionada
— Processamento de diálogo
— Comparação semântica
```

**Layout:** duas colunas — à esquerda, o fluxo vertical em 5 passos conectados por setas para baixo; à direita, a lista curta dos 5 conceitos de PLN, cada um em uma linha.

**Elementos visuais:** setas verticais tipográficas (↓); lista com marcador simples (travessão), sem ícones.

**Ícones/imagens:** nenhum — o próprio fluxo já é o elemento visual central.

**Explicar oralmente:** relacionar cada termo da lista diretamente a um passo do fluxo (ex: "compreensão da linguagem" é o que acontece quando o modelo interpreta a pergunta livre do jogador). Não aprofundar teoria — só ancorar cada termo no jogo.

---

### Slide 5 — Exemplo de Gameplay

**Título:** Exemplo de partida

**Texto exato:**
```
Investigador: "Onde você estava às 22h?"
Suspeito: "Eu estava em casa."
Investigador: "Mas sua chave foi usada para entrar no local."
Suspeito: "Eu... posso ter passado lá rapidamente."

Acusação
Mentira: "Disse que ficou em casa, mas voltou ao local."
Verdade: "Entrou no local usando sua chave."
Motivo: "Precisava de dinheiro."

Resultado: 3/3
```

**Layout:** bloco de transcrição (4 linhas) ocupando a parte superior/esquerda; ao lado ou abaixo, uma "ficha" com os 3 campos da acusação em formato de tabela simples (rótulo + valor); o resultado "3/3" em destaque grande no canto inferior.

**Elementos visuais:** a transcrição e a ficha de acusação usam o mesmo estilo de caixa com borda fina, para parecerem parte do mesmo "dossiê"; o número do resultado em cor de acento, bem maior que o resto do texto.

**Ícones/imagens:** nenhum.

**Explicar oralmente:** narrar a cena — mostrar como a contradição (chave x versão de "ficou em casa") aparece naturalmente na conversa, e como isso vira uma resposta objetiva no formulário final.

---

### Slide 6 — MVP + Viabilidade

**Título:** MVP: simples de desenvolver, fácil de demonstrar

**Texto exato:**
```
Telas         1
Suspeitos     1
Perguntas     6
Respostas     3
Resultado     0–3

Tecnologias
Python + Streamlit + API de LLM

3 estudantes · 1–2 semanas

Sem banco de dados · Sem login · Sem multiplayer
```

**Layout:** à esquerda, uma "ficha técnica" do MVP em formato tabela (chave à esquerda, valor à direita); à direita, a stack de tecnologias em três marcadores conectados por "+", a frase de viabilidade em destaque, e a lista de exclusões em texto pequeno no rodapé.

**Elementos visuais:** mesmo estilo de "ficha"/tabela do slide 5, reforçando consistência visual no encerramento; nenhum ícone.

**Ícones/imagens:** nenhum necessário.

**Explicar oralmente:** fechar reforçando que o escopo é deliberadamente pequeno e que isso é uma vantagem, não uma limitação — o grupo consegue realmente entregar o que está sendo mostrado.

---

## Notas gerais de reprodução

- **Paleta:** fundo quase-preto, texto quase-branco, um único acento âmbar/dourado usado só em números, títulos de destaque e pontos-chave.
- **Tipografia:** uma fonte de título/corpo limpa (ex: Helvetica/Arial/Calibri) + uma fonte monoespaçada (ex: Consolas/Courier New) para rótulos, tags e a "ficha técnica" — esse contraste entre as duas fontes é o que dá o efeito "dossiê/terminal" sem precisar de imagens.
- **Consistência:** repetir a legenda "0X / 06 — Seção" no topo de cada slide (ou apenas o número do slide) para dar noção de progresso.
- **Sem excesso:** cada slide tem no máximo 1 ideia central; todo o resto é apoio visual mínimo (caixas, setas, uma tabela).
