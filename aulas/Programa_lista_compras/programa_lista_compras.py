lista_de_compras = []

def adicionar_item(nome, quantidade, preco):
    item = {"nome": nome, "quantidade": quantidade, "preco": preco}
    lista_de_compras.append(item)

def remover_item(nome):
    for item in lista_de_compras:
        if item["nome"] == nome:
            lista_de_compras.remove(item)
            break

def atualizar_item(nome_antigo, nome_novo, quantidade_nova, preco_novo):
    for item in lista_de_compras:
        if item["nome"] == nome_antigo:
            item["nome"] = nome_novo
            item["quantidade"] = quantidade_nova
            item["preco"] = preco_novo
            break

def ler_lista():
    print("Sua lista de compras:")
    total_quantidade = 0
    total_preco = 0
    for item in lista_de_compras:
        print(f"Nome: {item['nome']}, Quantidade: {item['quantidade']}, Preço: {item['preco']}")
        total_quantidade += int(item['quantidade'])
        total_preco += float(item['preco'])
    print(f"Total da quantidade: {total_quantidade}")
    print(f"Total do preço: {total_preco}")

while True:
    opcao = input("Digite a opção desejada: (1) Adicionar item, (2) Remover item, (3) Atualizar item, (4) Ler lista, (5) Sair: ")
    if opcao == "1":
        nome = input("Digite o nome do item que deseja adicionar: ")
        quantidade = input("Digite a quantidade do item que deseja adicionar: ")
        preco = input("Digite o preço do item que deseja adicionar: ")
        adicionar_item(nome, quantidade, preco)
    elif opcao == "2":
        nome = input("Digite o nome do item que deseja remover: ")
        remover_item(nome)
    elif opcao == "3":
        nome_antigo = input("Digite o nome do item que deseja atualizar: ")
        nome_novo = input("Digite o novo nome do item: ")
        quantidade_nova = input("Digite a nova quantidade do item: ")
        preco_novo = input("Digite o novo preço do item: ")
        atualizar_item(nome_antigo, nome_novo, quantidade_nova, preco_novo)
    elif opcao == "4":
        ler_lista()
    elif opcao == "5":
        break

