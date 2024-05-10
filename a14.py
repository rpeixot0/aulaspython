a = 'AAAAAA'
b = 'BBBBB'
c = 1.1

string =' b={nome2} a={nome1} b={nome2} a={nome1} c={nome3:.2f}'

#formato = 'a={} b={} c={}'.format(a, b, c) é uma outra forma de se fazer

#se for nomear algum paramêtro (nesse caso a, b, c) é obrigatorio nomear os parametros que vem após o 1° nomeado
#sempre que nomear um paramêtro é importante mudar o nome na string, caso contrario um erro ocorrerá
formato = string.format(
    nome1=a, nome2=b, nome3=c
    )

print(formato)