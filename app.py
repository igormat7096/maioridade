# entrada de dados 
nome = input("Informe seu nome: ")
idade = int(input("Informe sua idade: "))

# verifica a idade do usuário
print(f"{nome} é maior de idade. " if idade >= 19 else f"{nome} é menor de idade")