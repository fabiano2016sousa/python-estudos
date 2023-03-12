#lendo e imprimindo uma lista de compras
compras = []
while True:
    produto = input('Produtos: ')
    if produto =='fim':
        break
    compras.append(produto)
for p in compras:
    print(p)
