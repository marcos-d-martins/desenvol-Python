#programa que recebe um ano digitado pelo usuário e o calcula
#, informando se é ou não um ano bissexto. 
ano_informado = int(input("informe um ano bissexto: "))
def calcula_Ano(anoInformado):
    #  % = resultado do número dividido por 400 resultará ou não em Zero
    #  % = resultado do número dividido por 4 resultará ou não em Zero
    if anoInformado == '':
        print("digite um valor! Não pode ser um campo vazio")
    if anoInformado % 4 == 0:
        print("funciona")
        print("\n ", anoInformado)
    else:
        print("erro. Ano não bissexto. Tente Novamente..")
        while anoInformado % 4 != 0:
            anoInformado = int(input("\ninforme um ano bissexto: "))
            if anoInformado % 4 == 0:
                print("\nfunciona")
                print("Parabéns! Ano bissexto encontrado.")
                print("\nAno digitado: ",anoInformado)
                print("\nfim programa.")
                break
            else:
                anos_errados = []
                anos_errados.append(anoInformado)
                print(anos_errados)
                print("erro")
        print("\n Anos não bissextos digitados: ",anos_errados)
#if __name__ == calcula_Ano(ano_informado):
calcula_Ano(ano_informado)