
# 3 - Programa que pede dois numeros, soma e depois mostra o resultado
"""n1 = input("Digite um número: ")
n2 = input("Digite outro número: ")
result = int(n1) + int(n2)
print(result)"""

# 4 - Programa que pede as 4 notas do bimestre, soma e mostra a média
'''
nota1 = input("Digite a sua primeira nota no bimestre: ")
nota2 = input("Digite a sua segunda nota no bimestre: ")
nota3 = input("Digite a sua terceira nota do bimestre: ")
nota4 = input("Digite a sua quarta nota do bimestre: ")

resultado = (int(nota1) + int(nota2) + int(nota3) + int(nota4)) / 4
print(resultado)
'''

# 5 - Programa que converte metros para centímetros
'''
m1 = input("Quantos metros você quer converter para centímetros: ")
resultado = float(m1) * 100
print(resultado)
'''

# 6 - Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
'''
pi = 3.14
raio = float(input("Digite o raio do seu círculo: "))
area = pi * (raio*raio)
print("A área do seu circulo é de ", area)
'''

# 7 - Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
'''
lado1 = float(input("Digite o tamanho do primeiro lado do seu quadrado: "))
lado2 = float(input("Digite o tamanho do segundo lado do seu quadrado: "))

area = lado1 * lado2
dobro = area * 2
print("Seu quadrado tem",area, "metros quadrados, e o dobro da sua área é: ", dobro)
'''

# 8 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.
'''
ganhoPorHoras = float(input("Quando você ganha por hora? "))
horasTrabalhadas = float(input("Quantas horas você trabalhou esse mês?"))
salarioDoMes = ganhoPorHoras * horasTrabalhadas
print("O seu salário deste mês foi de: R$",salarioDoMes)
'''

# 9 - Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius
'''
tempF = float(input("Digite a temperatura em Fahrenheit: "))
tempC = float(tempF - 32) * 5/9
tempC_formatado = "{:.2f}".format(tempC)
print("O resultado de", tempF,"convertidos para Celsius é: ",tempC_formatado)
'''

# 10 - Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
'''
tempC = float(input("Digite a temperatura em Celsius: "))
tempF = float((tempC * (9/5)) + 32)
tempf_formatado = "{:.2f}".format(tempF)
print("O resultado de", tempC,"convertidos para Fahrenheit é: ",tempf_formatado)
'''

# 11 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.
'''
n1 = int(input("Digite um número inteiro (Ex.: 5): "))
n2 = int(input("Digite outro número inteiro (Ex.: 2): " ))
n3 = float(input("Digite um número decimal (Ex.: 2.5): "))
result1 = (n1 * 2) + (n2 / 2)
result2 = (n1 * 3) + n3
result3 = n3 ** 3
print("O produto do dobro do primeiro número com metade do segundo é: ", result1)
print("A soma do triplo do primeiro número com o terceiro é: ", result2)
print("O terceiro número digitado elevado ao cubo é: ", result3)
'''

# 12 - Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal.
# usando a seguinte fórmula: (72.7*altura) - 58
'''
altura = float(input("Digite sua altura: "))
pesoIdeal = (72.7 * altura) - 58
pesoIdeal_formatado = "{:.2f}".format(pesoIdeal)
print("Seu peso ideal é de: ", pesoIdeal_formatado)
'''

# 13 - Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal.
# utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7
'''
altura = float(input("Digite sua altura: "))
pesoH = (altura * 72.7) - 58
pesoH_Formatado = "{:.2f}".format(pesoH)
pesoM = (altura * 62.1) - 44.7
pesoM_Formatado = "{:.2f}".format(pesoM)
print("Se você for homem seu peso ideal é de: ", pesoH_Formatado)
print("Se você for mulher seu peso ideal é de: ", pesoM_Formatado)
'''

# 14 - João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
'''
pesoDePeixes = float(input("Digite o rendimento em Kg de hoje: "))

if pesoDePeixes > 50:
    pesoDePeixes -= 50
    excesso = pesoDePeixes
    multa = excesso * 4
    print("Você deve pagar ", multa,"de multa")

else:
    print("Você não precisa pagar multa")
'''

# 15 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.
'''
ganhoHora = float(input("Digite quanto você ganha por hora: "))
horasTrabalhadas = float(input("Digite quantas horas você trabalha por mês: "))
bruto = ganhoHora * horasTrabalhadas
ir = bruto * 0.11
inss = bruto * 0.08
sindicato = bruto * 0.05
salarioLiquido = bruto - sindicato - inss - ir
print("Seu salário bruto é de: R$", bruto)
print("Você paga, R$",inss,"para o INSS.")
print("Você paga, R$",sindicato,"para o sindicado.")
print("Seu salário liquido é de: R$", salarioLiquido)
'''



# 16 - Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''
coberturaTinta = 3
capacidadeLata = 18
precoLata = 80.0

areaPintada = float(input("Digite o tamanho da área a ser pintada: "))

litros = areaPintada / coberturaTinta
latasInteiras = int(litros/capacidadeLata)
if (litros%capacidadeLata != 0):
    latasInteiras += 1

valorTotal = precoLata * latasInteiras

print("Quantidade de litros necessários: {}" .format(litros))
print("Quantidade de latas necessárias: {}" .format(latasInteiras))
print("Valor total da compra {}" .format(valorTotal))
'''

# 17 - Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.



# 18 - Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

'''
tamanhoArquivo = float(input("Digite o tamanho do arquivo (em MB): "))
velocidade = float(input("Digite a velocidade da internet (em Mbps): "))
tempo = (tamanhoArquivo / (velocidade / 8)) / 60

print(f'Para efetuar o download de {tamanhoArquivo} MB com uma velocidade de {velocidade} Mbps, irá demorar aproximadamente {tempo:.0f} minutos.')
'''







