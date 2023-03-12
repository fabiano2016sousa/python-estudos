ultimo = 10
fila = list(range(1, ultimo + 1))
while True:
    print(f"\nExistem {len(fila)} clientes na fila")
    print(f"Fila atual: {fila}")
    print("Digite F para adicionar um cliente no fim da fila,")
    print("ou A para realizar oatendimento. S para sair.")
    operacao = input("Operação (F, A ou S):")
    if operacao == "A":
        if len(fila) > 0:
            atendimento = fila.pop(0)
            print(f"Cliente {atendimento} atendido")
        else:
            print("Fila vazia! Ninguém para atender.")
    elif operacao == "F":
        ultimo += 1 #incrementa o tickt do novo cliente
        fila.append(ultimo)
    elif operacao == "S":
        break
    else:
        print("Operação inválida! Digte apenas F, A ou S!")
