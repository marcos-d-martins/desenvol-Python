#usuário adiciona a nota
#usuário remove a nota
#exibe a nota
#
def exibir_menu():
    print("\nGerenciador de notas")
    print("1.adicionar notas")
    print("2.remover notas")
    print("3.ver todas as notas")
    print("4.calcular média das notas")
    print("5.exibir maior e menor nota")
    print("6.sair")

    escolha = input("Escolha uma opção:  ")
    return escolha

def adicionar_nota(notas):
    try:
        nota = float(input("digite a nota a ser adicionada: "))
        notas.append(nota)
        print("nota adicionada com sucesso")
    except ValueError:
        print("erro: por favor, insira um valor numérico.")

def remover_nota(notas):
    try:
        nota = float(input("digite a nota a ser removida: "))
        if nota in notas:
            notas.remove(nota)
        else:
            print("Erro: nota não encontrada.")
    except ValueError:
        print("erro: insira um valor numérico.")

def ver_notas(notas):
    if notas:
        print("notas: ",notas)
    else:
        print("Não há notas a exibir.")
    
def calcular_media(notas):
    if notas:
        media = sum(notas)  / len(notas)
        print(f"média das notas: {media:.2f}")
    else:
        print(f"Não há notas para exibir na média.")

def exibir_maior_menor(notas):
    if notas:
        maior_nota = max(notas)
        menor_nota = min(notas)
        print(f"maior nota: {maior_nota}")
        print(f"menor nota: {menor_nota}")
    else:
        print("não há notas a serem exibidas.")

def main():
    nota = []
    while True:
        escolha = exibir_menu()
        if escolha == '1':
            adicionar_nota(nota)
        elif escolha == '2':
            remover_nota(nota)
        elif escolha == '3':
            ver_notas(nota)
        elif escolha == '4':
            calcular_media(nota)
        elif escolha == '5':
            exibir_maior_menor(nota)
        elif escolha == '6' or escolha > '6':
            print("saindo do programa...")
            break
        else:
            print("escolha inválida. Escolha entre 1 e 5!")
        
if __name__ == "__main__":
    main()    
