import streamlit as st

import ia
from config import NUM_PERGUNTAS

st.set_page_config(page_title="O Interrogatório", page_icon="🕵️")


def iniciar_nova_partida():
    with st.spinner("Montando o caso..."):
        try:
            caso = ia.gerar_caso()
        except ia.ErroIA as exc:
            st.session_state["erro"] = str(exc)
            return
    st.session_state["caso"] = caso
    st.session_state["historico"] = []
    st.session_state["perguntas_restantes"] = NUM_PERGUNTAS
    st.session_state["fase"] = "interrogatorio"
    st.session_state["resultado"] = None
    st.session_state.pop("erro", None)


def tela_publico(caso: dict):
    st.info(
        f"**{caso['crime']}**\n\n"
        f"📍 {caso['local']}  ·  🕐 {caso['horario']}  ·  🧑 Suspeito: **{caso['suspeito']}**"
    )


def tela_interrogatorio(caso: dict):
    tela_publico(caso)

    for turno in st.session_state["historico"]:
        with st.chat_message("user"):
            st.write(turno["pergunta"])
        with st.chat_message("assistant", avatar="🕵️"):
            st.write(turno["resposta"])

    restantes = st.session_state["perguntas_restantes"]
    st.caption(f"Perguntas restantes: {restantes}/{NUM_PERGUNTAS}")

    if restantes > 0:
        pergunta = st.chat_input("Faça sua pergunta ao suspeito...")
        if pergunta:
            with st.spinner(f"{caso['suspeito']} está pensando..."):
                try:
                    resposta = ia.perguntar_suspeito(pergunta, st.session_state["historico"], caso)
                except ia.ErroIA as exc:
                    st.error(f"Erro ao falar com o suspeito: {exc}")
                    return
            st.session_state["historico"].append({"pergunta": pergunta, "resposta": resposta})
            st.rerun()
    else:
        st.warning("Suas perguntas acabaram. Hora de apresentar sua acusação.")
        if st.button("Fazer acusação final", type="primary"):
            st.session_state["fase"] = "acusacao"
            st.rerun()


def tela_acusacao(caso: dict):
    tela_publico(caso)
    st.subheader("Acusação final")

    with st.form("form_acusacao"):
        mentira = st.text_area("Qual foi a mentira do suspeito?")
        verdade = st.text_area("O que realmente aconteceu?")
        motivo = st.text_area("Qual foi o motivo?")
        enviado = st.form_submit_button("Acusar", type="primary")

    if enviado:
        if not (mentira.strip() and verdade.strip() and motivo.strip()):
            st.error("Preencha as três respostas antes de acusar.")
            return
        with st.spinner("Avaliando sua acusação..."):
            try:
                resultado = ia.avaliar_acusacao(mentira, verdade, motivo, caso)
            except ia.ErroIA as exc:
                st.error(f"Erro ao avaliar a acusação: {exc}")
                return
        st.session_state["resultado"] = resultado
        st.session_state["fase"] = "resultado"
        st.rerun()


def tela_resultado(caso: dict):
    resultado = st.session_state["resultado"]
    pontuacao = ia.calcular_pontuacao(resultado)

    st.header(f"Resultado: {pontuacao}/3")

    criterios = [
        ("Identificou a mentira", resultado.get("identificou_mentira")),
        ("Explicou o que aconteceu", resultado.get("explicou_verdade")),
        ("Identificou o motivo", resultado.get("identificou_motivo")),
    ]
    for texto, acertou in criterios:
        st.write(("✅ " if acertou else "❌ ") + texto)

    st.write(resultado.get("justificativa", ""))

    with st.expander("Ver a verdade completa do caso"):
        st.write(f"**O que realmente aconteceu:** {caso['verdade']}")
        st.write(f"**A mentira do suspeito:** {caso['mentira_principal']}")
        st.write(f"**Motivo:** {caso['motivo']}")

    if st.button("Nova partida", type="primary"):
        iniciar_nova_partida()
        st.rerun()


st.title("🕵️ O Interrogatório")
st.caption("Detetive de Mentiras")

if st.session_state.get("erro"):
    st.error(st.session_state["erro"])

if "fase" not in st.session_state:
    st.write("Descubra a mentira. Encontre a verdade.")
    if st.button("Começar partida", type="primary"):
        iniciar_nova_partida()
        st.rerun()
else:
    caso = st.session_state["caso"]
    fase = st.session_state["fase"]

    if fase == "interrogatorio":
        tela_interrogatorio(caso)
    elif fase == "acusacao":
        tela_acusacao(caso)
    elif fase == "resultado":
        tela_resultado(caso)
