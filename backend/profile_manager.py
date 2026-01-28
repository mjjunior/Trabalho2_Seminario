# Perfis simulados
PERFIS = {
    "1": {
        "nome": "Usuário Adulto",
        "idade": 28,
        "preferencias": ["esportes", "noticias"],
        "restricoes": []
    },
    "2": {
        "nome": "Usuário Infantil",
        "idade": 9,
        "preferencias": ["desenhos"],
        "restricoes": ["conteudo_adulto"]
    }
}

def obter_perfil(user_id: str):
    return PERFIS.get(user_id)

def listar_perfis():
    return PERFIS
