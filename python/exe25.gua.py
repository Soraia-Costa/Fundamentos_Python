# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”. 
city =str(input('Em que cidade vc nasceu? ')).strip()
print(city[:5].upper()=='SANTO')


# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome=str(input('Digite um nome : ')) .strip()         
print('Seu nome tem Silva {}'.format ('silva' in nome.lower()))