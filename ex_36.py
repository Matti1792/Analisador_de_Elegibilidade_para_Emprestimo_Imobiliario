import time

c = {'limpar': '\033[m',
     'vermelho': '\033[31m',
     'verde': '\033[32m'}



print('-=' * 20)
print('         {}Analisador de dados{}    '.format(c['vermelho'], c['limpar']))
print('-=' * 20)


v = float(input("Valor da Casa: R$ "))

Salario = float(input("Salario do comprador: R$ "))

q = int(input("Quantos anos de financiamento? "))

p = v / (q * 12)

print("Para pagar uma casa de {}R${:.2f}{} em {}{}{} anos a prestação será de {}R${:.2f}{}.".format(c['verde'], v, c['limpar'], c['verde'], q, c['limpar'], c['verde'], p, c['limpar'], c['verde']))

time.sleep(1.5)

print('-=' * 20)\


if Salario <= p:
    print("Emprestimo {}NEGADO!{}".format(c['vermelho'], c['limpar']))

else:
    print("Emprestimo {}CONCEDIDO!{}".format(c['verde'], c['limpar']))