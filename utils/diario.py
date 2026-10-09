from sistema import ARQ_DIARIO




def registrar_diario():
    servico = input("Serviço: ").strip()
    anotacao = input("Anotação: ").strip()


    with open(ARQ_DIARIO, "a", encoding="utf-8") as arquivo:

        arquivo.write(servico + " — " + anotacao + "\n")
    print("Anotação registrada no diário.")



def consultar_diario():
    try:
        with open(ARQ_DIARIO, "r", encoding="utf-8") as arquivo:

            texto = arquivo.read()
    except FileNotFoundError:

        print("Nenhuma anotação registrada")
        return

    if texto.strip() == "":
        print("Nenhuma anotação registrada")
    else:
        print(texto)