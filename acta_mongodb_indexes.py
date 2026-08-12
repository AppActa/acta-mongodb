import os
import sys
from pymongo import MongoClient, ASCENDING, DESCENDING


def criar_indices(db):
    # ---------- Ciclos e tarefas ----------

    # 1. ishikawa
    db.ishikawa.create_index(
        [("id_empresa", ASCENDING), ("id_ciclo", ASCENDING)],
        unique=True,
    )

    # ---------- Formulários ----------

    # 2. formularios
    db.formularios.create_index(
        [("id_empresa", ASCENDING), ("id_formulario", ASCENDING)],
        unique=True,
    )

    db.formularios.create_index(
        [("id_empresa", ASCENDING), ("id_ciclo", ASCENDING), ("status", ASCENDING)]
    )

    # 3. respostas_formulario
    db.respostas_formulario.create_index(
        [
            ("id_empresa", ASCENDING),
            ("id_ciclo", ASCENDING),
            ("id_formulario", ASCENDING),
            ("respondido_em", DESCENDING),
        ]
    )

    # ---------- Documentos ----------

    # 6. anexos
    db.anexos.create_index(
        [("id_empresa", ASCENDING), ("id_ciclo", ASCENDING), ("tipo_documento", ASCENDING)]
    )

    # ---------- Memória do chatbot ----------

    # 7. memoria_sessoes
    db.memoria_sessoes.create_index(
        [("expira_em", ASCENDING)], expireAfterSeconds=0
    )

    # 8. memoria_mensagens
    db.memoria_mensagens.create_index(
        [("expira_em", ASCENDING)], expireAfterSeconds=0
    )

    print("Índices documentados criados com sucesso.")


def main():
    if len(sys.argv) >= 2:
        URL = sys.argv[1]
        nome_banco = sys.argv[2] if len(sys.argv) > 2 else None
    else:
        URL = os.environ.get("MONGO_URL")
        nome_banco = os.environ.get("MONGO_DB_NAME")
        if not URL:
            print(
                "Erro: nenhuma URL informada.\n"
                "Use: infisical run --env=prod -- python acta_mongodb_indexes.py\n"
                "Ou:  python acta_mongodb_indexes.py <mongo_URL> [nome_do_banco]"
            )
            sys.exit(1)

    client = MongoClient(URL)
    db = client.get_default_database() if nome_banco is None else client[nome_banco]

    criar_indices(db)


if __name__ == "__main__":
    main()