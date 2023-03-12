# Exemplo de dicionário com estoque e operação de venda

estoque = {"livro A": [1000, 12.50],
           "livro B": [500, 19.45],
           "livro C": [2015, 29.20],
           "livro D": [100, 102.50]}
venda = [["livro A", 5], ["livro D", 10], ["livro C", 5], ["livro B", 25]]
total = 0
print("Venda:\n")
for operacao in venda:
    produto, quantidade = operacao #desempacotamento (produto = operação), (quantidade = operação) em uma linha só.
    preco = estoque[produto][1] # produto está como chave no dicionário estoque.
    custo = preco * quantidade
    print(f"{produto:5s}: {quantidade:3d} x {preco:6.2f} = {custo:6.2f}")
    estoque[produto][0] -= quantidade #quantidade em estoque menos quantidade vendida.
    total += custo
print(f"Custo total: {total:21.2f}\n")
print("Estoque:\n")
for chave, dados in estoque.items(): #retornar uma trupla contendo a chave e o valor de cada item armazenado
    print("Descrição: ", chave)
    print("Quantidade: ", dados[0])
    print(f"Preço: {dados[1]:6.2f}\n")
