#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date
ano =int(input('Qual o ano deseja analisar ? Coloque 0 para o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and  ano % 100 != 0 or ano % 400 == 0:
    print ('Este ano {} é Bissexto'.format (ano))
else:
    print('Este ano {} nao é Bissexto'.format(ano))