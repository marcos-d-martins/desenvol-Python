#programa que recebe um ano digitado pelo usuário e o calcula
#, informando se é ou não um ano bissexto. 
ano_informado = int(input("informe um ano bissexto: "))
def calcula_Ano(anoInformado):
    #  % = resultado do número dividido por 400 resultará ou não em Zero
    #  % = resultado do número dividido por 4 resultará ou não em Zero
    if anoInformado == '':
        print("digite um valor! Não pode ser um campo vazio")
    """if anoInformado.isnumeric():
        print("O valor DEVE ser um número inteiro. Não pode conter letras")
        print("\nAno digitado: ",anoInformado)"""
    if anoInformado % 4 == 0:
        print("funciona")
        print("\n ", anoInformado)
    else:
        print("erro. Ano não bissexto. Tente Novamente..")
        while anoInformado % 4 != 0:
            ano_informado = int(input("\ninforme um ano bissexto: "))
            if ano_informado % 4 == 0:
                print("\nfunciona")
                anos_errados = []
                anos_errados.append(ano_informado)
                print(anos_errados)
                print("Parabéns! Ano bissexto encontrado.")
                print("\nAno digitado: ",ano_informado)
                print("\nfim programa.")
  
        #return false



#if __name__ == calcula_Ano(ano_informado):
calcula_Ano(ano_informado)