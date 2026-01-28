from backend.ia_ml import IAML

# ==================================================
# Instância única da IA (singleton simples)
# ==================================================
ia = IAML()


def decidir_conteudo(perfil: dict):
    """
    Decide o conteúdo com base no perfil do usuário,
    aplicando regras determinísticas antes do Machine Learning.
    """

    idade = perfil.get("idade", 30)
    preferencias = perfil.get("preferencias", [])
    restricoes = perfil.get("restricoes", [])

    # --------------------------------------------------
    # REGRA 1 – Prioridade absoluta para público infantil
    # --------------------------------------------------
    if idade < 12:
        genero_base = "desenhos"
        classificacao = "Livre"

    # --------------------------------------------------
    # REGRA 2 – Usuário adulto/adolescente com preferências
    # --------------------------------------------------
    elif preferencias:
        genero_base = preferencias[0]
        classificacao = "12+"

    # --------------------------------------------------
    # REGRA 3 – Fallback real (último recurso)
    # --------------------------------------------------
    else:
        genero_base = "noticias"
        classificacao = "Livre"

    # --------------------------------------------------
    # REGRA 4 – Restrições explícitas do perfil
    # --------------------------------------------------
    if "conteudo_adulto" in restricoes:
        classificacao = "Livre"

    # --------------------------------------------------
    # DECISÃO FINAL via Machine Learning (simulada)
    # --------------------------------------------------
    ia_decisao = ia.recomendar(idade, genero_base)

    return {
        "ia_decidiu_genero": genero_base,
        "conteudo": {
            "titulo": f"Programa recomendado ({genero_base})",
            "classificacao": classificacao,
            "url_video": "/static/video.mp4"
        },
        "modelo": "IA simbólica + ML simulado"
    }
