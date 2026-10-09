"""Chamadas ao modelo de IA (Gemini). Ver proposta_final.md secao 12 (arquitetura)."""

import json

import google.generativeai as genai

import prompts
from config import GEMINI_API_KEY, MODEL_NAME

genai.configure(api_key=GEMINI_API_KEY)


class ErroIA(Exception):
    """Erro amigavel para exibir na interface quando a API falha ou responde algo inutilizavel."""


def _model(json_mode: bool = False):
    generation_config = {"response_mime_type": "application/json"} if json_mode else {}
    return genai.GenerativeModel(MODEL_NAME, generation_config=generation_config)


def _gerar_caso_uma_vez() -> dict:
    resposta = _model(json_mode=True).generate_content(prompts.PROMPT_GERADOR_CASO)
    return json.loads(resposta.text)


def gerar_caso() -> dict:
    """Gera o caso completo. Valida os campos e tenta novamente uma vez se algo faltar."""
    try:
        caso = _gerar_caso_uma_vez()
    except Exception as exc:
        raise ErroIA(f"Não foi possível gerar o caso: {exc}") from exc

    faltando = [c for c in prompts.CAMPOS_CASO if c not in caso]
    if faltando:
        try:
            caso = _gerar_caso_uma_vez()
        except Exception as exc:
            raise ErroIA(f"Não foi possível gerar o caso: {exc}") from exc
        faltando = [c for c in prompts.CAMPOS_CASO if c not in caso]
        if faltando:
            raise ErroIA(f"O caso gerado veio incompleto (faltou: {', '.join(faltando)}).")

    return caso


def perguntar_suspeito(pergunta: str, historico: list[dict], caso: dict) -> str:
    prompt = prompts.prompt_suspeito(caso, historico, pergunta)
    try:
        resposta = _model(json_mode=False).generate_content(prompt)
    except Exception as exc:
        raise ErroIA(f"O suspeito não respondeu: {exc}") from exc
    return resposta.text.strip()


def avaliar_acusacao(resposta_mentira: str, resposta_verdade: str, caso: dict) -> dict:
    prompt = prompts.prompt_avaliador(caso, resposta_mentira, resposta_verdade)
    try:
        resposta = _model(json_mode=True).generate_content(prompt)
        return json.loads(resposta.text)
    except Exception as exc:
        raise ErroIA(f"Não foi possível avaliar a acusação: {exc}") from exc


def calcular_pontuacao(resultado: dict) -> int:
    """Soma os 2 criterios booleanos retornados pela IA avaliadora. Nunca a IA decide a nota."""
    pontos = 0
    if resultado.get("identificou_mentira"):
        pontos += 1
    if resultado.get("explicou_verdade"):
        pontos += 1
    return pontos
