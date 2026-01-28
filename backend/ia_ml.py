import json
import os
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder


class IAML:
    def __init__(self):
        self.modelo = DecisionTreeClassifier(random_state=42)
        self.encoder_genero = LabelEncoder()
        self.encoder_conteudo = LabelEncoder()

        self.conteudos = self._carregar_conteudos()
        self._treinar_modelo()

    # --------------------------------------------------
    # Carregamento do catálogo de conteúdos
    # --------------------------------------------------
    def _carregar_conteudos(self):
        caminho = os.path.join(
            os.path.dirname(__file__),
            "..",
            "data",
            "conteudo.json"
        )

        with open(caminho, "r", encoding="utf-8") as f:
            return json.load(f)

    # --------------------------------------------------
    # Treinamento do modelo (simulado)
    # --------------------------------------------------
    def _treinar_modelo(self):
        dados = {
            "idade": [8, 10, 25, 30, 40, 60, 15, 18],
            "genero_preferido": [
                "desenhos", "desenhos",
                "esportes", "esportes",
                "noticias", "noticias",
                "jogos", "jogos"
            ],
            "conteudo_recomendado": [
                "canal_infantil",
                "canal_infantil",
                "futebol_ao_vivo",
                "futebol_ao_vivo",
                "jornal_nacional",
                "documentario",
                "games_show",
                "games_show"
            ]
        }

        df = pd.DataFrame(dados)

        df["genero_cod"] = self.encoder_genero.fit_transform(df["genero_preferido"])
        df["conteudo_cod"] = self.encoder_conteudo.fit_transform(df["conteudo_recomendado"])

        X = df[["idade", "genero_cod"]]
        y = df["conteudo_cod"]

        self.modelo.fit(X, y)

    # --------------------------------------------------
    # Recomendação final (IA + Curadoria)
    # --------------------------------------------------
    def recomendar(self, idade: int, genero: str):

        # 🔐 Segurança: garante que o gênero exista no encoder
        if genero not in self.encoder_genero.classes_:
            genero = "noticias"

        genero_cod = self.encoder_genero.transform([genero])[0]

        pred = self.modelo.predict([[idade, genero_cod]])
        previsao = self.encoder_conteudo.inverse_transform(pred)[0]

        # --------------------------------------------------
        # Curadoria de conteúdo (regra + classificação)
        # --------------------------------------------------
        conteudos_validos = [
            c for c in self.conteudos
            if c["genero"] == genero
            and c["classificacao"] in ["livre", "10+", "12+"]
        ]

        # Fallback seguro e explicável
        if not conteudos_validos:
            conteudos_validos = [
                c for c in self.conteudos
                if c["classificacao"] == "livre"
            ]

        conteudo_final = conteudos_validos[0]

        return {
            "conteudo": conteudo_final,
            "metodo": "Machine Learning (Decision Tree)",
            "confianca": "alta",
            "ia_decidiu_genero": genero,
            "ia_previsao_modelo": previsao
        }


# --------------------------------------------------
# Instância única da IA (singleton)
# --------------------------------------------------
ia_ml = IAML()
