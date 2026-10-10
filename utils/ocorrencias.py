# arquivo para funções das ocorrencias

from config import ARQ_JSON

import json





def carregar_ocorrencias():
    try:
        with open(ARQ_JSON, "r", encoding="utf-8") as arquivo:
            # json.load transforma o texto do arquivo em uma lista Python
            lista = json.load(arquivo)

    except FileNotFoundError:
        return [], True

    except json.JSONDecodeError:

        return [], False


    if not isinstance(lista, list):
        return [], False


    return lista, True



def salvar_ocorrencias(lista):

    with open(ARQ_JSON, "w", encoding="utf-8") as arquivo:
        json.dump(lista, arquivo, ensure_ascii=False, indent=4)




def registrar_ocorrencia():

    lista, ok = carregar_ocorrencias()

    if ok == False:
        print("ERRO: o arquivo ocorrencias.json está inválido.")
        print("Corrija o arquivo (ele não foi alterado).")
        print("Cadastro, consulta e resumo estão suspensos até lá.")
        return


    servico = input("Serviço afetado (ex.: login, pagamento): ").strip()
    descricao = input("Descrição do problema e efeito para o usuário: ").strip()

    prioridade = input("Prioridade (alta/media/baixa): ").strip().lower()
    while prioridade != "alta" and prioridade != "media" and prioridade != "baixa":
        print("Valor inválido! Digite alta, media ou baixa.")
        prioridade = input("Prioridade (alta/media/baixa): ").strip().lower()


    status = input("Status (aberto/resolvido): ").strip().lower()
    while status != "aberto" and status != "resolvido":
        print("Valor inválido! Digite aberto ou resolvido.")
        status = input("Status (aberto/resolvido): ").strip().lower()


    if status == "resolvido":

        proxima_acao = "nenhuma"
    else:
        proxima_acao = input("Próxima ação para a próxima equipe: ").strip()


    ocorrencia = {
        "servico": servico,
        "descricao": descricao,
        "prioridade": prioridade,
        "status": status,
        "proxima_acao": proxima_acao,
    }


    lista.append(ocorrencia)
    salvar_ocorrencias(lista)
    print("Ocorrência salva com sucesso!")




def consultar_ocorrencias():
    lista, ok = carregar_ocorrencias()


    if ok == False:
        print("ERRO: o arquivo ocorrencias.json está inválido. Corrija-o.")
        return

    if len(lista) == 0:
        print("Não há ocorrências registradas.")
        return

    for oc in lista:
        print("---------------------------------")
        print(f"Serviço:      {oc['servico']}")
        print(f"Descrição:    {oc['descricao']}")
        print(f"Prioridade:   {oc['prioridade']}")
        print(f"Status:       {oc['status']}")
        print(f"Próxima ação: {oc['proxima_acao']}")
        print("----------------------------------")
