from datetime import datetime

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles

from backend.profile_manager import obter_perfil
from backend.ia import decidir_conteudo


# ==================================================
# Inicialização da API
# ==================================================

app = FastAPI(
    title="TV 3.0 - Prova de Conceito",
    description=(
        "API para simulação de serviços da TV 3.0, incluindo "
        "detecção de dispositivo móvel, proximidade, perfil do usuário "
        "e recomendação inteligente de conteúdo com apoio de IA."
    ),
    version="1.1.0"
)

app.mount("/static", StaticFiles(directory="static"), name="static")


# ==================================================
# ROTA RAIZ
# ==================================================

@app.get("/")
def root():
    return {
        "projeto": "TV 3.0",
        "tipo": "POC",
        "status": "API ativa",
        "timestamp": datetime.now().isoformat()
    }


# ==================================================
# DISPOSITIVO (Simulação)
# ==================================================

@app.get("/device/current")
def get_current_device():
    return {
        "device_id": "mobile-001",
        "type": "smartphone",
        "connection": "Wi-Fi",
        "associated_with_tv": True
    }


@app.get("/device/proximity")
def get_device_proximity():
    return {
        "status": "proximo",
        "distancia_estimada": "2 metros",
        "metodo": "simulação por latência"
    }


# ==================================================
# PERFIL DO USUÁRIO
# ==================================================

@app.get("/profile/{user_id}")
def get_profile(user_id: str):
    perfil = obter_perfil(user_id)

    if not perfil:
        raise HTTPException(
            status_code=404,
            detail="Perfil não encontrado"
        )

    return perfil


# ==================================================
# CONTEXTO DA TV + IA
# ==================================================

@app.get("/tv/context/{user_id}")
def get_tv_context(user_id: str):
    perfil = obter_perfil(user_id)

    if not perfil:
        raise HTTPException(
            status_code=404,
            detail="Perfil não encontrado"
        )

    recomendacao = decidir_conteudo(perfil)

    return {
        "tv_state": "ligada",
        "usuario": perfil["nome"],
        "ia_ativa": True,
        "recomendacao": recomendacao,
        "explicacao": (
            "O sistema combina regras determinísticas e Machine Learning "
            "para realizar recomendações personalizadas, respeitando "
            "classificação indicativa e contexto do usuário."
        )
    }
