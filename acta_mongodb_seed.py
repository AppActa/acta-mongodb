import os
import sys
from datetime import datetime, timezone
from pymongo import MongoClient


def dt(iso_str: str) -> datetime:
    return datetime.fromisoformat(iso_str).replace(tzinfo=timezone.utc)


def popular(db):
    # ---------- 1. ishikawa ----------
    db.ishikawa.insert_one({
        "id_empresa": 1,
        "id_ciclo": 1,
        "problema": "Retrabalho alto",
        "causas": {
            "metodo": ["Ausência de padrão operacional"],
            "mao_de_obra": ["Treinamento incompleto"],
            "maquina": [],
            "material": [],
            "medicao": [],
            "meio_ambiente": []
        },
        "criado_por": 1,
        "criado_em": dt("2026-08-04T12:00:00"),
        "atualizado_em": dt("2026-08-04T12:00:00"),
    })

    # ---------- 2. formularios ----------
    db.formularios.insert_one({
        "id_formulario": "7f675087-b963-4148-a68c-e1cc1434ec70",
        "id_empresa": 1,
        "id_ciclo": 1,
        "titulo": "Análise de fenômeno",
        "tipo": "ANALISE_FENOMENO",
        "descricao": "Formulário para mapear ocorrências do processo.",
        "status": "ATIVO",
        "perguntas": [
            {
                "id_pergunta": "eece17a4-50f0-4564-97c6-f4e0a3bfdf4d",
                "texto": "Em qual turno ocorreu?",
                "tipo_resposta": "SELECAO_UNICA",
                "obrigatoria": True,
                "opcoes": ["Manhã", "Tarde", "Noite"]
            },
            {
                "id_pergunta": "0ca09ee8-2118-4fab-82bd-00dbef26d036",
                "texto": "Descreva o problema.",
                "tipo_resposta": "TEXTO",
                "obrigatoria": True
            }
        ],
        "criado_por": 1,
        "criado_em": dt("2026-08-04T12:00:00"),
        "publicado_em": dt("2026-08-04T12:30:00"),
        "atualizado_em": dt("2026-08-04T12:30:00"),
    })

    # ---------- 3. respostas_formulario ----------
    db.respostas_formulario.insert_one({
        "id_formulario": "7f675087-b963-4148-a68c-e1cc1434ec70",
        "id_usuario": 2,
        "respostas": [
            {
                "id_pergunta": "eece17a4-50f0-4564-97c6-f4e0a3bfdf4d",
                "resposta": ["Java", "Python"]
            },
            {
                "id_pergunta": "0ca09ee8-2118-4fab-82bd-00dbef26d036",
                "resposta": "Foi identificado retrabalho na linha A."
            }
        ],
        "respondido_em": dt("2026-08-04T14:00:00"),
    })

    # ---------- 4. relatorios ----------
    db.relatorios.insert_one({
        "id_relatorio": "478aac52-e2dc-490c-9281-472388cb3075",
        "id_empresa": 1,
        "id_ciclo": 1,
        "tipo": "RESUMO_EXECUTIVO",
        "formato": "MARKDOWN",
        "status": "CONCLUIDO",
        "titulo": "Resumo executivo do ciclo",
        "resumo": "O ciclo avançou, mas possui tarefas em risco.",
        "conteudo": "# Resumo executivo\n\nO ciclo apresenta...",
        "criado_por": 1,
        "criado_em": dt("2026-08-04T12:00:00"),
        "publicado_em": dt("2026-08-04T13:00:00"),
        "atualizado_em": dt("2026-08-04T13:00:00"),
    })

    # ---------- 5. licoes_aprendidas ----------
    db.licoes_aprendidas.insert_one({
        "id_licao": "e633fce9-7870-48a6-87ad-f32d79438cfd",
        "id_empresa": 1,
        "id_ciclo": 1,
        "titulo": "Validar o padrão antes do treinamento",
        "licao": "Treinamentos realizados antes da validação geram retrabalho.",
        "categoria": "PROCESSO",
        "tags": ["padronização", "treinamento"],
        "criado_por": 1,
        "criado_em": dt("2026-08-04T12:00:00"),
    })

    # ---------- 6. anexos ----------
    db.anexos.insert_one({
        "id_empresa": 1,
        "id_ciclo": 1,
        "nome_documento": "evidencia-retrabalho-linha-a.pdf",
        "tipo_documento": "PDF",
        "contexto": "EVIDENCIA",
        "dados": [],
    })

    # ---------- 7. memoria_sessoes ----------
    db.memoria_sessoes.insert_one({
        "session_id": "sessao-123",
        "empresa_id": 1,
        "usuario_id": 2,
        "status": "aberta",
        "resumo": "O usuário acompanha o ciclo 1.",
        "resumido_ate": dt("2026-08-04T12:30:00"),
        "total_mensagens": 8,
        "metadata": {},
        "iniciada_em": dt("2026-08-04T12:00:00"),
        "atualizada_em": dt("2026-08-04T12:30:00"),
        "expira_em": dt("2026-11-02T12:30:00"),
    })

    # ---------- 8. memoria_mensagens ----------
    db.memoria_mensagens.insert_one({
        "session_id": "sessao-123",
        "empresa_id": 1,
        "usuario_id": 2,
        "role": "usuario",
        "content": "Mostre as tarefas atrasadas do ciclo 1.",
        "agent": "guardrail_entrada",
        "metadata": {},
        "criada_em": dt("2026-08-04T12:05:00"),
        "expira_em": dt("2026-11-02T12:05:00"),
    })

    # ---------- 9. memoria_usuario ----------
    db.memoria_usuario.insert_one({
        "empresa_id": 1,
        "usuario_id": 2,
        "tipo": "preferencia",
        "conteudo": "Prefere relatórios executivos em tópicos curtos.",
        "origem": "explicita",
        "confianca": 1.0,
        "session_id_origem": "sessao-123",
        "metadata": {},
        "status": "ativa",
        "criada_em": dt("2026-08-04T12:00:00"),
        "atualizado_em": dt("2026-08-04T12:00:00"),
        "expira_em": None,
    })

    # ---------- 10. memoria_consentimentos ----------
    db.memoria_consentimentos.insert_one({
        "empresa_id": 1,
        "usuario_id": 2,
        "modo": "somente_explicitas",
        "retencao_dias": 365,
        "atualizado_em": dt("2026-08-04T12:00:00"),
    })

    # ---------- 11. skills_usuario ----------
    db.skills_usuario.insert_one({
        "empresa_id": 1,
        "usuario_id": 2,
        "nome": "Resumo executivo",
        "slug": "resumo-executivo",
        "objetivo": "Gerar um resumo executivo do ciclo.",
        "regras": "- Começar pelos riscos.\n- Usar tópicos curtos.",
        "markdown": (
            "# Resumo executivo\n\n"
            "# objetivo\n\nGerar um resumo executivo do ciclo.\n\n"
            "# regras\n\n- Começar pelos riscos."
        ),
        "status": "ativa",
        "criada_em": dt("2026-08-04T12:00:00"),
        "atualizado_em": dt("2026-08-04T12:00:00"),
    })


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
                "Use: infisical run --env=prod -- python acta_mongodb_seed.py\n"
                "Ou:  python acta_mongodb_seed.py <mongo_URL> [nome_do_banco]"
            )
            sys.exit(1)

    client = MongoClient(URL)
    db = client.get_default_database() if nome_banco is None else client[nome_banco]

    popular(db)


if __name__ == "__main__":
    main()