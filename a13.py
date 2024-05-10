nome ='Renato Peixoto';
altura = 1.80;
peso = 140
imc = peso / (altura*altura)
linha_1 = f'{nome} tem {altura:.2f} de altura' 
# linha_1 = f'{nome} tem {altura:,.2f} de altura' 

linha_2 = f'pesa {peso} quilos e seu IMC é'

linha_3 = f'{imc:.2f}'
#as chamadas de 'f strings' permite vc usar vars dentro basta a var existir, colocar o 'f' antes e envolver em chaves a var

#em números float podemos escolher quantas casas decimais vai aparecer no caso da altura aparecerá 2 casas após o .

#também é possivel usando o :.xf fazermos ele colocar uma ',' ou um '.' a cada casa decimal

#o calculo do IMC pode ser feito também da seguinte forma: peso / altura**2 pela lei da precedencia

print(linha_1)
print(linha_2)
print(linha_3)

# os três pontinhos (...) é chamado de elipsis e é um placeholder e não dá erro na execução 