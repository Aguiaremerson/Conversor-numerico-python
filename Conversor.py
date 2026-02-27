numero = int (input('Digite um numero inteiro: '))
print ("""Escolha uma das opçôes
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL""")

m= int (input("Digite opção desejada: "))
if m == 1:
    print("{} Convertido para BINARIO é igual a {}".format(numero,bin(numero)[2:]))
elif m == 2:
    print ("{}convertido para OCTAL é igual a {}".format(numero,oct(numero)[2:]))
elif m == 3:
    print ("{}Convertidp ára HEXADECIMAL é igual a {} ".format9num. hex(numero)[2:])
else:
    Print("Opção invalida")

