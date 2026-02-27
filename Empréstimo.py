
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

