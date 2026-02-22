#O mesmo professor do desafio anterior quer sortear a orde de apresentação de trabalhos dos alunos. Faca um programa que leia o nome dos quatros alunos e mostre a ordem sorteada. 
#import random
#n1 =str (input('Primerio nome: '))
#n2 = str(input('Segundo numero: '))
#n3 = str(input('Terceiro numero: '))
#n4 = str(input('Quarto numero: '))

#lista = [n1, n2,n3,n4]
#random.shuffle(lista)
#print('A ordem da lista é {}'.format(lista))

from random import shuffle
n1 =str (input('Primerio nome: '))
n2 = str(input('Segundo numero: '))
n3 = str(input('Terceiro numero: '))
n4 = str(input('Quarto numero: '))
lista = [n1, n2,n3,n4]
shuffle(lista)
print('A ordem da lista é {}'.format(lista))