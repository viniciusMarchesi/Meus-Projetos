import sqlite3
import PySimpleGUI as sg

# Conectar ao banco de dados (ou criar um novo se ele não existir)
conn = sqlite3.connect('lista_de_compras.db')
c = conn.cursor()

# Criar tabela para armazenar os itens da lista de compras
#c.execute('''
#    CREATE TABLE IF NOT EXISTS lista_de_compras (
#        id INTEGER PRIMARY KEY AUTOINCREMENT,
#        nome TEXT,
#        quantidade INTEGER,
#        preco_unitario REAL
#    )
#''')

# Salvar as alterações e fechar a conexão com o banco de dados
#conn.commit()
#conn.close()

# Salvar as alterações e fechar a conexão com o banco de dados
conn.commit()
conn.close()

# Layout da janela do menu principal
menu_layout = [
    [sg.Text("Nome do item:"), sg.Input(key="nome_item")],
    [sg.Text("Quantidade:"), sg.Input(key="quantidade_item")],
    [sg.Text("Preço unitário:"), sg.Input(key="preco_unitario_item")],
    [sg.Button("Adicionar item"), sg.Button("Remover item"), sg.Button("Atualizar item"), sg.Button("Ler lista")]
]

# Janela do menu principal
menu_janela = sg.Window("Menu Principal", menu_layout)

# Função para adicionar um item à lista de compras
def adicionar_item(nome, quantidade, preco_unitario):
     # Conectar ao banco de dados   
    conn = sqlite3.connect('lista_de_compras.db')
    c = conn.cursor()
    
     # Inserir o item na tabela lista_de_compras   
    c.execute('INSERT INTO lista_de_compras (nome, quantidade, preco_unitario) VALUES (?, ?, ?)', (nome, quantidade, preco_unitario))
    
     # Salvar as alterações e fechar a conexão com o banco de dados   
    conn.commit()
    conn.close()

# Função para remover um item da lista de compras
def remover_item(nome):
     # Conectar ao banco de dados   
    conn = sqlite3.connect('lista_de_compras.db')
    c = conn.cursor()
    
     # Deletar o item da tabela lista_de_compras   
    c.execute('DELETE FROM lista_de_compras WHERE nome = ?', (nome,))
    
     # Salvar as alterações e fechar a conexão com o banco de dados   
    conn.commit()
    conn.close()

# Função para atualizar um item da lista de compras
def atualizar_item(nome_antigo, nome_novo, quantidade_nova, preco_unitario_novo):
     # Conectar ao banco de dados   
    conn = sqlite3.connect('lista_de_compras.db')
    c = conn.cursor()
    
     # Atualizar o item na tabela lista_de_compras   
    c.execute('UPDATE lista_de_compras SET nome = ?, quantidade = ?, preco_unitario = ? WHERE nome = ?', (nome_novo, quantidade_nova, preco_unitario_novo, nome_antigo))
    
     # Salvar as alterações e fechar a conexão com o banco de dados   
    conn.commit()
    conn.close()

# Função para ler a lista de compras
def ler_lista():
     # Conectar ao banco de dados   
    conn = sqlite3.connect('lista_de_compras.db')
    c = conn.cursor()
    
     # Selecionar todos os itens da tabela lista_de_compras   
    c.execute('SELECT * FROM lista_de_compras')
    itens = c.fetchall()
    
     # Fechar a conexão com o banco de dados   
    conn.close()
    
     # Calcular o valor total e a quantidade total de itens   
    valor_total = sum([item[2] * item[3] for item in itens])
    quantidade_total = sum([item[2] for item in itens])
    
     # Mostrar os itens da lista de compras e as informações adicionais   
    sg.popup_scrolled("Sua lista de compras:", "\n".join([f"Nome: {item[1]}, Quantidade: {item[2]}, Preço Unitário: {item[3]}, Preço: {item[2] * item[3]}" for item in itens]), f"\nValor Total: {valor_total}", f"Quantidade Total: {quantidade_total}")

while True:
    # Ler eventos e valores das janelas
    evento, valores = menu_janela.read()
    
     # Fechar o programa   
    if evento == sg.WIN_CLOSED:
        break
    
     # Adicionar item à lista de compras   
    elif evento == "Adicionar item":
        nome = valores["nome_item"]
        quantidade = int(valores["quantidade_item"])
        preco_unitario = float(valores["preco_unitario_item"])
        adicionar_item(nome, quantidade, preco_unitario)
        sg.popup("Item adicionado à lista de compras")
    
     # Remover item da lista de compras   
    elif evento == "Remover item":
        nome = sg.popup_get_text("Digite o nome do item que deseja remover:")
        if nome:
            remover_item(nome)
            sg.popup("Item removido da lista de compras")
    
     # Atualizar item da lista de compras   
    elif evento == "Atualizar item":
        nome_antigo = sg.popup_get_text("Digite o nome do item que deseja atualizar:")
        if nome_antigo:
            nome_novo = sg.popup_get_text("Digite o novo nome do item:")
            quantidade_nova = int(sg.popup_get_text("Digite a nova quantidade do item:"))
            preco_unitario_novo = float(sg.popup_get_text("Digite o novo preço unitário do item:"))
            atualizar_item(nome_antigo, nome_novo, quantidade_nova, preco_unitario_novo)
            sg.popup("Item atualizado na lista de compras")
    
     # Ler a lista de compras   
    elif evento == "Ler lista":
        ler_lista()

menu_janela.close()






