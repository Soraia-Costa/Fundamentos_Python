frase ='Curso em video Python'
print(frase )
print(frase [3]) #fatiamento
print(frase [3:13]) #de um ponto à outro
print(frase [:14])#do inicio ate o final 
print(frase [0:]) 
print(frase [::2])
print(frase [::13])
print(frase.count('o'))
print(len(frase))
print (frase.replace('Python','Android'))
print('Curso' in frase)
print(frase.find('Python'))
print(frase.split())

dividido=frase.split()
print(dividido[2][2])

#desafio
#Crie um programa que leia o nome completo de uma pessoa e mostre: 
#- O nome com todas as letras maiuscula
#O nome com todas minuscula
#Quantas letras ao todo (sem considerar espacos)
#quantas letras tem o primeiro nome


#Faca um programa que leia um numero de 0 à 9999 e mostre na tela cada um dos digitos separados 