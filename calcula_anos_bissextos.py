#programa que recebe um ano digitado pelo usuário e o calcula
#, informando se é ou não um ano bissexto. 
ano_informado = int(input("informe um ano bissexto: "))
def calcula_Ano(anoInformado):
    
    if anoInformado % 400 == 0 or anoInformado % 4 == 0 and anoInformado % 100 != 0:
        print("funciona")
    else:
        print("erro. Ano não bissexto. Tente Novamente..")
        while anoInformado % 400 != 0 or anoInformado % 4 != 0 and anoInformado % 100 != 0:
            ano_informado = int(input("\ninforme um ano bissexto: "))
        else:
                print("Parabéns! Ano bissexto encontrado.")
                print("\nAno digitado: ",anoInformado)
                print("\nfim programa.")
        """if anoInformado == '':
            print("digite um valor! Não pode ser um campo vazio")
            if not anoInformado.is_integer():
                print("O valor DEVE ser um número inteiro. Não pode conter letras")
                print("Parabéns! Ano bissexto encontrado.")
                print("\nAno digitado: ",anoInformado)
        
    
        #return false
    else:
        print(anoInformado," não é um ano bissexto. Tente de novo")
        anos_digitados_nao_bissextos = []
        anos_digitados_nao_bissextos.append(anoInformado)
        anoInformado = int(input("informe um ano bissexto: "))
        calcula_Ano(anoInformado)"""


#if __name__ == calcula_Ano(ano_informado):
calcula_Ano(ano_informado)