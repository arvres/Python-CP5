from utils.ocorrencias import carregar_ocorrencias

from config import NOME_SISTEMA, ARQ_PASSAGEM

def gerar_passagem():
    lista, ok = carregar_ocorrencias()


    if ok == False:
        print("ERRO: ocorrencias.json inválido. O resumo anterior foi mantido.")
        return


    abertas = []
    qtd_altas = 0

    for oc in lista:
        if oc["status"] == "aberto":
            abertas.append(oc)
            if oc["prioridade"] == "alta":
                qtd_altas += 1

    with open(ARQ_PASSAGEM, "w", encoding="utf-8") as arquivo:
        arquivo.write(f"PASSAGEM DE PLANTÃO - {NOME_SISTEMA} \n")
        arquivo.write(f"Ocorrências abertas: {str(len(abertas))} \n")
        arquivo.write(f"Abertas com prioridade alta: {str(qtd_altas)} \n")
        arquivo.write("\n")

        if len(abertas) == 0:
            arquivo.write("Nenhuma pendência para o próximo plantão\n")
        else:
            for oc in abertas:
                arquivo.write("Serviço: " + oc["servico"] + "\n")
                arquivo.write("Descrição: " + oc["descricao"] + "\n")
                arquivo.write("Prioridade: " + oc["prioridade"] + "\n")
                arquivo.write("Próxima ação: " + oc["proxima_acao"] + "\n")
                arquivo.write("\n")


    with open(ARQ_PASSAGEM, "r", encoding="utf-8") as arquivo:
        print(arquivo.read())
