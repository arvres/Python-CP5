# CP5 Computational Thinking With Python ----- Pedro Henrique Alves - RM 569192

#imports
from config import NOME_SISTEMA

from utils.ocorrencias import registrar_ocorrencia, consultar_ocorrencias
from utils.diario import registrar_diario, consultar_diario
from utils.passagem import gerar_passagem



def main():

    while True:
        print(f"\n===== Passagem de plantão - {NOME_SISTEMA} =====")
        print("1 - Registrar ocorrência")
        print("2 - Consultar ocorrências")
        print("3 - Registrar anotação no diário")
        print("4 - Consultar diário")
        print("5 - Gerar passagem de plantão")
        print("6 - Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            registrar_ocorrencia()

        elif opcao == "2":
            consultar_ocorrencias()

        elif opcao == "3":
            registrar_diario()

        elif opcao == "4":
            consultar_diario()

        elif opcao == "5":
            gerar_passagem()

        elif opcao == "6":
            print("Até a próxima!")
            break          # sai do while e o programa termina
        else:
            print("Opção inválida! Digite um número de 1 a 6.")




if __name__ == "__main__": main()