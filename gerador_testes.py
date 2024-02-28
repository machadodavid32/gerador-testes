import random
print("BEM VINDO ao Gerador de testes")
print('------------------------------')

#Criando as listas
nomes = ["David","Arthur", "Aline", "Guilherme", "Danilo"]
emails = ["david@gmail.com", "aline@gmail.com", "arthur@gmail.com", "guilherme@gmail.com", "danilo@gmail.com"]
telefones = ["988787878", "943433434", "976754323", "912322343", "9445566773"]
cidades = ["São Paulo", "Guarulhos", "Itaqua", "Mogi", "Suzano"]
estados = ["SP","RJ", "SC", "RS", "BA"]
# Criando random

# Criando o menu
print("Por favor, escolha uma das opções abaixo: ")
print("1 - Nome")
print("2 - Email")
print("3 - Telefone")
print("4 - Cidade")
print("5 - Estado")
print("6 - Sair")
user_input = input("Por favor, escolha sua opção apenas com o número: ")

if user_input == "1":
    nomes_aleatorios = random.choice(nomes)
    print(nomes_aleatorios)

elif user_input == "2":
    emails_aleatorios = random.choice(emails)
    print(emails_aleatorios)    
    
elif user_input == "3":
    telefones_aleatorios = random.choice(telefones)
    print(telefones_aleatorios)

elif user_input == "4":
    cidades_aleatorias = random.choice(cidades)
    print(cidades_aleatorias)

elif user_input == "5":
    estados_aleatorios = random.choice(estados)
    print(estados_aleatorios)
    
elif user_input == "sair":
    print("Até mais")

else:
    print("Por favor, escolha uma das opções corretamente")    
        
            
        