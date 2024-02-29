import random 
# importando o módulo random para resposta aletória dos dados do programa

# Desenvolvendo dentro de um bloco while para controlar quando o programa continua ou encerra
def main():
    print("BEM VINDO ao Gerador de testes")
    print('------------------------------')
    while True:
        

        #Criando as listas
        nomes = ["David","Arthur", "Aline", "Guilherme", "Danilo"]
        emails = ["david@gmail.com", "aline@gmail.com", "arthur@gmail.com", "guilherme@gmail.com", "danilo@gmail.com"]
        telefones = ["988787878", "943433434", "976754323", "912322343", "9445566773"]
        cidades = ["São Paulo", "Guarulhos", "Itaqua", "Mogi", "Suzano"]
        estados = ["SP","RJ", "SC", "RS", "BA"]

        # Criando o menu
        print("Por favor, escolha uma das opções abaixo: ")
        print("1 - Nome")
        print("2 - Email")
        print("3 - Telefone")
        print("4 - Cidade")
        print("5 - Estado")
        

        user_input = input("Por favor, escolha sua opção apenas com o número, caso mais de uma opção, separe por virgulas sem espaço: ")

        # Dividindo a entrada do usuário por vírgula para obter as opções selecionadas
        opcoes_selecionadas = user_input.split(',')

        # Processando as opções selecionadas
        for opcao in opcoes_selecionadas:
            
            if opcao.strip() == "1":
                nomes_aleatorios = random.choice(nomes)
                print(nomes_aleatorios)

            elif opcao.strip() == "2":
                emails_aleatorios = random.choice(emails)
                print(emails_aleatorios)    
                
            elif opcao.strip() == "3":
                telefones_aleatorios = random.choice(telefones)
                print(telefones_aleatorios)

            elif opcao.strip() == "4":
                cidades_aleatorias = random.choice(cidades)
                print(cidades_aleatorias)

            elif opcao.strip() == "5":
                estados_aleatorios = random.choice(estados)
                print(estados_aleatorios)

            else:
                print("Por favor, escolha uma das opções corretamente")    
                
        continuar = input("Deseja continuar (s/n)? ")
        
        
        if continuar.lower() == 'n':
            print("Até mais")
            break  
        else:
            print("                         ")
            print("Por favor, somente s ou n")  
            print("#########################")

if __name__ == "__main__":
    main()        