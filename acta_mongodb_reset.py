import os
import sys
from pymongo import MongoClient


DB_NAME = "acta_db"


def resetar_banco(URL):
    client = MongoClient(URL)

    try:
        # -------------------------------------------------
        # 1. Derruba o banco existente
        # -------------------------------------------------
        print(f"Derrubando o banco '{DB_NAME}'...")

        client.drop_database(DB_NAME)

        print(f"Banco '{DB_NAME}' removido com sucesso.")

        # -------------------------------------------------
        # 2. Cria novamente o banco
        # -------------------------------------------------
        print(f"Criando o banco '{DB_NAME}'...")

        db = client[DB_NAME]

        # O MongoDB cria o banco efetivamente quando
        # uma coleção/documento é criado.
        db.create_collection("_init")

        print(f"Banco '{DB_NAME}' criado com sucesso.")

        # -------------------------------------------------
        # 3. Remove a coleção auxiliar
        # -------------------------------------------------
        db["_init"].drop()

        print("Coleção auxiliar removida.")
        print()
        print("Reset do banco concluído com sucesso!")

    finally:
        client.close()


def main():
    if len(sys.argv) >= 2:
        URL = sys.argv[1]

    else:
        URL = os.environ.get("MONGO_URL")

        if not URL:
            print(
                "Erro: nenhuma URL do MongoDB foi encontrada.\n\n"
                "Execute usando o Infisical:\n"
                "infisical run --env=prod -- python acta_mongodb_reset.py\n\n"
                "Ou informe a URL diretamente:\n"
                "python acta_mongodb_reset.py <mongo_URL>"
            )

            sys.exit(1)

    resetar_banco(URL)


if __name__ == "__main__":
    main()