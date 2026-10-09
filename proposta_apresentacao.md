# O Interrogatório — Detetive de Mentiras
## Versão Final para Apresentação

---

## 1. O que é o jogo

Um jogo de dedução em que o jogador investiga um crime conversando por texto com um suspeito controlado por IA.

Cada partida apresenta um caso novo — com crime, contexto, suspeito e uma mentira diferente — gerado pela própria IA. O jogador pode conversar livremente com o suspeito e precisa descobrir o que realmente aconteceu.

---

## 2. Como o jogador joga

O jogador recebe apenas as informações essenciais do caso: crime, local, horário e suspeito.

Ele tem 6 perguntas para interrogar o personagem e precisa analisar as respostas em busca de pistas, hesitações e contradições.

No final, responde a três perguntas:
- Qual foi a mentira do suspeito?
- O que realmente aconteceu?
- Qual foi o motivo?

Depois, o jogo revela a verdade e apresenta a pontuação do jogador.

---

## 3. Onde a IA entra

A IA participa de três momentos principais:

**Antes do jogo:**
Gera o caso completo — incluindo a verdade, a versão do suspeito, a mentira e o motivo real. Essas informações ficam ocultas do jogador.

**Durante o interrogatório:**
A IA interpreta o suspeito e responde às perguntas em linguagem natural. A cada resposta, os fatos do caso são reenviados ao modelo para reduzir inconsistências e manter o personagem fiel à história definida anteriormente.

**No final:**
A IA compara as respostas do jogador com os fatos reais do caso, considerando também respostas escritas com palavras diferentes, mas com o mesmo significado. Ela retorna critérios estruturados de acerto, e o código do jogo calcula a pontuação.

---

## 4. Por que a IA é necessária?

O jogador pode fazer qualquer pergunta e formulá-la da maneira que quiser.

Um sistema tradicional precisaria prever e programar manualmente diferentes perguntas e respostas. Como cada partida também possui um caso diferente, isso tornaria o desenvolvimento muito mais complexo.

Com um modelo generativo, conseguimos combinar: casos diferentes + perguntas livres + respostas dinâmicas, sem precisar criar uma árvore de diálogos para cada possibilidade.

---

## 5. Onde está o PLN?

O PLN aparece diretamente na interação do jogo:

- **Geração de linguagem:** a IA cria os casos e as respostas do suspeito.
- **Compreensão de linguagem natural:** o sistema interpreta as perguntas feitas pelo jogador.
- **Geração condicionada:** as respostas do suspeito são geradas com base nos fatos definidos para aquele caso.
- **Processamento de diálogo:** mantém o contexto e a coerência das respostas durante o interrogatório.
- **Comparação semântica:** verifica se a resposta do jogador possui o mesmo significado dos fatos reais, mesmo utilizando palavras diferentes.

---

## 6. MVP

O primeiro protótipo será propositalmente simples:
- Uma única tela;
- Um suspeito;
- Um caso por partida;
- 6 perguntas;
- Perguntas em texto livre;
- Formulário final com 3 respostas;
- Pontuação de 0 a 3;
- Revelação da verdade;
- Botão para iniciar uma nova partida.

Não haverá no MVP:
- Login;
- Ranking;
- Banco de dados;
- Multiplayer;
- Geração de imagens;
- Geração de áudio;
- Geração de vídeo.

**Tecnologia:** Python + Streamlit + API de LLM, utilizando uma opção de API com uso gratuito adequado ao protótipo, respeitando os limites vigentes do serviço escolhido.

---

## 7. Viabilidade

O projeto é viável para 3 estudantes em aproximadamente 1 a 2 semanas.

A interface é simples, a integração com a API é direta e o estado necessário para uma partida é pequeno.

O principal trabalho de refinamento será realizar testes com diferentes casos e perguntas para ajustar os prompts e garantir que o suspeito mantenha coerência durante o interrogatório.

---

## 8. Expansões futuras

Depois do MVP, o jogo poderia evoluir para:
- Múltiplos suspeitos, incluindo inocentes;
- Diferentes níveis de dificuldade;
- Temas de investigação selecionáveis;
- Retratos de personagens gerados por IA;
- Histórico de partidas;
- Ranking de jogadores;
- Dicas durante o interrogatório.
