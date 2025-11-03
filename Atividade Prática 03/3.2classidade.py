#Crie um programa que solicite a idade do usuário e classifique-o em uma das seguintes categorias:
#Criança (0-12 anos),
#Adolescente (13-17 anos),
#Adulto (18-59 anos)
#Idoso (60 anos ou mais).


idade = int(input("Digite sua idade: "))

if idade >= 60:
    print("Idoso (60 anos ou mais)")
elif idade >= 18 and idade <= 59:
    print("Adulto (18-59 anos)")
elif idade >= 13 and idade <= 17:
    print("Adolescente (13-17 anos)")
else:
    print("Criança (0-12 anos)")
    
