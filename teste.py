import random

def main():
    print("BEM VINDO ao Gerador de testes")
    print('------------------------------')
    while True:
        nomes = ["David","Arthur", "Aline", "Guilherme", "Danilo"]
        emails = ["david@gmail.com", "aline@gmail.com", "arthur@gmail.com", "guilherme@gmail.com", "danilo@gmail.com"]
        telefones = ["988787878", "943433434", "976754323", "912322343", "9445566773"]
        cidades = ["São Paulo", "Guarulhos", "Itaqua", "Mogi", "Suzano"]
        estados = ["SP","RJ", "SC", "RS", "BA"]

        print("Por favor, escolha uma das opções abaixo: ")
        print("1 - Nome")
        print("2 - Email")
        print("3 - Telefone")
        print("4 - Cidade")
        print("5 - Estado")
        
        user_input = input("Por favor, escolha sua opção apenas com o número, caso mais de uma opção, separe por virgulas sem espaço: ")
        opcoes_selecionadas = user_input.split(',')

        # Variável para armazenar as informações selecionadas
        informacoes_selecionadas = []

        for opcao in opcoes_selecionadas:
            if opcao.strip() == "1":
                informacoes_selecionadas.append(random.choice(nomes))
            elif opcao.strip() == "2":
                informacoes_selecionadas.append(random.choice(emails))    
            elif opcao.strip() == "3":
                informacoes_selecionadas.append(random.choice(telefones))
            elif opcao.strip() == "4":
                informacoes_selecionadas.append(random.choice(cidades))
            elif opcao.strip() == "5":
                informacoes_selecionadas.append(random.choice(estados))
            else:
                print("Por favor, escolha uma das opções corretamente")

        # Exibindo as informações selecionadas
        for info in informacoes_selecionadas:
            print(info)

        continuar = input("Deseja continuar (s/n)? ").lower()
        
        if continuar == 'n':
            salvar = input("Deseja salvar (s/n)?").lower()
            if salvar == 's':
                # Convertendo a lista de informações selecionadas em uma string
                informacoes_str = "\n".join(informacoes_selecionadas)
                with open('arquivo.txt', 'a') as arquivo:
                    arquivo.write(informacoes_str + "\n")
            else:
                print("Até mais")
                break  
        else:
            print("                         ")
            print("Por favor, somente s ou n")  
            print("#########################")

if __name__ == "__main__":
    main()
