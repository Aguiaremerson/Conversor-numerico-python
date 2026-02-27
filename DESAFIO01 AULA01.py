print ('               Seja Bem vindo \nAqui vamos realizar o seu sonho de ter uma casa propria ')
salario=float(input('Digite seu salario: '))
Casa =float(    input('Digite o valor da casa que você quer possuir: '))
print ("Parabens,Pela sua iniciativa de compra !!\n Com o valor desejado de {:.2f} você podera parcela em quantas anod você quiser.".format(Casa))
ano = float(input('Digite em quantos anos você quer quitar sua nova casa: '))
resultado = salario * 0.3
res = ano * 12
res1 = res / Casa
if res <= resultado :
     print ("Parabens voce podera comprar a casa por apenas {:.2f} reais por mês".format(res1))
else:
     print ('Você não podera compra a casa pois excede 39 % do seu salario {}'.format(resultado))




                              # Codigo Certo abaixo:

casa = float(input('Digite o valor da casa:  R$ '))
salario = float (input('Sálario do comprador: R$ '))
anos = int (input ('Quantos anos de finaciament?'))
prestação = casa / (anos *  12)
minimo = salario  * 30 / 100
print ("Para pagar uma casa de R${:.2f} em {} anos".format (casa, anos), end ='')
print("A prestação será de R${:.2f}".format (prestação))
if prestação <= minimo:
    Print ("Emprestimo pode ser concedido parabens pela casa !!")
else:
    print("Emprestimo negado excedo 30% do seu salario")
