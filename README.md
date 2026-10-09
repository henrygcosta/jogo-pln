# O Interrogatório — Detetive de Mentiras (MVP CP5)

Jogo de dedução por texto: uma IA gera um caso e o jogador interroga um suspeito (também controlado por IA) em até 6 perguntas livres. Depois faz uma acusação com 2 respostas (qual foi a mentira e o que realmente aconteceu) e recebe uma nota de 0 a 2.

## Requisitos

- Python 3.10 ou superior (testado com 3.14)
- Chave gratuita da API do Gemini: https://aistudio.google.com/apikey

## Como executar (Windows, PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
# abra o .env e preencha GEMINI_API_KEY com a sua chave
streamlit run app.py
```

Se o PowerShell bloquear o `Activate.ps1`, execute direto: `.\.venv\Scripts\python.exe -m streamlit run app.py`.
O navegador abre em http://localhost:8501.

## Variáveis de ambiente (`.env`)

| Variável | Obrigatória | Descrição |
|---|---|---|
| `GEMINI_API_KEY` | sim | Chave da API do Gemini. Nunca versionar o `.env`. |
| `GEMINI_MODEL` | não | Modelo usado. Padrão: `gemini-2.5-flash`. |

## Como jogar

1. Clique em **Começar partida**: a IA gera o caso (crime, local, horário, suspeito).
2. Faça até **6 perguntas** livres ao suspeito, que responde em personagem. Procure contradições nas respostas.
3. Com as perguntas esgotadas, clique em **Fazer acusação final** e responda: qual foi a mentira e o que realmente aconteceu.
4. A IA compara com a verdade e o código Python soma a pontuação (0 a 2). Você vê a verdade completa e pode iniciar nova partida.

## Estrutura

| Arquivo | Função |
|---|---|
| `app.py` | Interface Streamlit e fluxo (menu, interrogatório, acusação, resultado) |
| `ia.py` | Chamadas ao Gemini (gerar caso, responder como suspeito, avaliar) e `calcular_pontuacao` |
| `prompts.py` | Templates dos 3 prompts |
| `config.py` | Leitura do `.env` e número de perguntas |
| `assets/` | Imagens geradas por IA (Bing Image Creator / DALL·E 3) exibidas no jogo |
| `evidencia_*.json` | Exemplos reais das saídas da IA da CP4 |

## IA generativa usada

- **Texto (tempo real):** Google Gemini, via `google-generativeai`. Até 8 chamadas por partida.
- **Imagem (assets pré-gerados):** Bing Image Creator (DALL·E 3): retrato do suspeito, cena do crime (menu) e ícone, exibidos no jogo em execução.

## Segurança

Não há chaves no código. O `.env` e o `.venv` estão no `.gitignore` e não devem entrar em ZIP ou commit.
