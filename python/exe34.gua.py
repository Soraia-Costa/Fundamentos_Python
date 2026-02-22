# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.


salario = float(input('Digite seu salario atual:'))
if salario <= 1250:
    salarioAtual = salario + (salario *15/100)
    
else:
    salarioAtual = salario + (1250 *10/100)
print ('Seu salario será de {:.2f}'.format(salarioAtual))