velocidade = int(input("O carro passou com que velocidade? "))
if velocidade > 80:
    print("Você pagará multa! ")
    multa = velocidade - 80
    valor = multa * 7
    print("A multa é de R$ {},00!".format(valor))
else:
    print("Você está no limite da velocidade permitida. ")
