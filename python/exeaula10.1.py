'''nome=str(input('Qual é seu nome?'))
if nome =='Soraia':
    print('Que nome lindo vc tem!')

print('Bom dia {}'. format(nome))

nome=str(input('Qual o seu nome?'))
if nome =='Laura':
    print('Que nome lindo vc tem!!')
else:
    print('Seu nome é tão normal!')    
print('Bom dia,{}'.format(nome))    '''

n1 = float(input('Digite a primeira nota: '))
n2= float(input('Digite a segunda nota :'))
m=(n1+n2)/2
print('A sua media foi {:.2f}'.format(m))
if m>= 6.0:
    print('Sua media foi boa! Aprovado!')
else:
    print('Sua media foi ruim! Esta reprovado!')