num = int(input('digite por quantos dias o carro foi alugado:'))
km = float(input('digite por quantos kilometros vc andou:'))
print('você usou o carro por {} dias e andou com ele por {}km\n o preço a pagar é R${:.2f}'
.format(num, km, (60*num)+(0.15*km)))
