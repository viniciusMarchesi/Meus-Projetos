#import sqlite3

# Conectar ao banco de dados (ou criar um novo se ele não existir)
#banco = sqlite3.connect('banco_lista_compras.db')

#cursor = banco.cursor()

# criando a tabela de usuarios
#cursor.execute('CREATE TABLE usuarios (nome text, email text, senha integer)')

# inserindo os dados na tabela
#cursor.execute("INSERT INTO usuarios VALUES ('victor','victor_123@gmail.com','2793117')")

# Executando a atualização no banco
#banco.commit()

# Mostrando os dados no console
#cursor.execute('SELECT * FROM usuarios')
#print(cursor.fetchall())

# Deletando registros do banco 
'''try:
    cursor.execute('DELETE from usuarios WHERE senha = 12345')
    
    banco.commit()
    banco.close()
    print('os dados foram removidos com sucesso!')

except sqlite3.Error as erro:
    print('erro ao excluir os dados!!!')'''

#import sqlite3

# Conectar ao banco de dados (ou criar um novo se ele não existir)
#conn = sqlite3.connect('lista_de_compras.db')
#c = conn.cursor()

# Criar tabela para armazenar os usuários
#c.execute('''
#   CREATE TABLE IF NOT EXISTS usuarios (
#        id INTEGER PRIMARY KEY AUTOINCREMENT,
#        email TEXT,
#        senha TEXT,
#       nome TEXT
#    )
''')

# Criar tabela para armazenar os itens da lista de compras
c.execute('''
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

import sqlite3
import PySimpleGUI as sg

# Conectar ao banco de dados (ou criar um novo se ele não existir)
conn = sqlite3.connect('lista_de_compras.db')
c = conn.cursor()

# Criar tabela para armazenar os usuários
#c.execute('''
#    CREATE TABLE IF NOT EXISTS usuarios (
#        id INTEGER PRIMARY KEY AUTOINCREMENT,
#        email TEXT,
#        senha TEXT,
#        nome TEXT
#    )
''')

# Criar tabela para armazenar os itens da lista de compras
c.execute('''
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

# Layout da janela de acesso
acessar_layout = [
    [sg.Text("E-mail:"), sg.Input(key="email")],
    [sg.Text("Senha:"), sg.Input(key="senha")],
    [sg.Button("Acessar"), sg.Button("Criar novo usuário")]
]

# Janela de acesso
acessar_janela = sg.Window("Acessar", acessar_layout)

# Layout da janela de novo usuário
novo_usuario_layout = [
    [sg.Text("E-mail:"), sg.Input(key="email")],
    [sg.Text("Senha:"), sg.Input(key="senha")],
    [sg.Text("Nome:"), sg.Input(key="nome")],
    [sg.Button("Criar usuário")]
]

# Janela de novo usuário
novo_usuario_janela = None

# Layout da janela do menu principal
menu_layout = [
    [sg.Text("Nome do item:"), sg.Input(key="nome_item")],
    [sg.Text("Quantidade:"), sg.Input(key="quantidade_item")],
    [sg.Text("Preço unitário:"), sg.Input(key="preco_unitario_item")],
    [sg.Button("Adicionar item"), sg.Button("Remover item"), sg.Button("Atualizar item"), sg.Button("Ler lista")]
]

# Janela do menu principal
menu_janela = None

# Função para verificar se o e-mail e a senha estão corretos
def verificar_usuario(email, senha):
     # Conectar ao banco de dados   
    conn = sqlite3.connect('lista_de_compras.db')
    c = conn.cursor()
    
     # Selecionar o usuário com o e-mail informado   
    c.execute('SELECT * FROM usuarios WHERE email = ?', (email,))
    usuario = c.fetchone()
    
     # Fechar a conexão com o banco de dados   
    conn.close()
    
     # Verificar se o usuário existe e se a senha está correta   
    if usuario and usuario[2] == senha:
        return True
    else:
        return False

# Função para criar um novo usuário
def criar_usuario(email, senha, nome):
     # Conectar ao banco de dados   
    conn = sqlite3.connect('lista_de_compras.db')
    c = conn.cursor()
    
     # Verificar se o e-mail já existe   
    c.execute('SELECT * FROM usuarios WHERE email = ?', (email,))
    usuario = c.fetchone()
    
     # Se o e-mail não existir, criar um novo usuário   
    if not usuario:
        c.execute('INSERT INTO usuarios (email, senha, nome) VALUES (?, ?, ?)', (email, senha, nome))
        sg.popup("Usuário criado com sucesso")
    else:
        sg.popup_error("E-mail já existe")
    
     # Salvar as alterações e fechar a conexão com o banco de dados   
    conn.commit()
    conn.close()

# Função para obter o nome do usuário a partir do e-mail
def obter_nome_usuario(email):
     # Conectar ao banco de dados   
    conn = sqlite3.connect('lista_de_compras.db')
    c = conn.cursor()
    
     # Selecionar o usuário com o e-mail informado   
    c.execute('SELECT * FROM usuarios WHERE email = ?', (email,))
    usuario = c.fetchone()
    
     # Fechar a conexão com o banco de dados   
    conn.close()
    
     # Retornar o nome do usuário (ou None se ele não existir)   
    if usuario:
        return usuario[3]
    else:
        return None

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
    
     # Mostrar os itens da lista de compras   
    sg.popup_scrolled("Sua lista de compras:", "\n".join([f"Nome: {item[1]}, Quantidade: {item[2]}, Preço Unitário: {item[3]}, Preço: {item[2] * item[3]}" for item in itens]))

while True:
    # Ler eventos e valores das janelas
    janela, evento, valores = sg.read_all_windows()
    
     # Fechar o programa   
    if evento == sg.WIN_CLOSED:
        break
    
     # Acessar o programa   
    if evento == "Acessar":
        email = valores["email"]
        senha = valores["senha"]
        if verificar_usuario(email, senha):
            acessar_janela.hide()
            menu_janela = sg.Window("Menu Principal", menu_layout)
        else:
            sg.popup_error("Acesso negado")
    
     # Criar novo usuário   
    elif evento == "Criar novo usuário":
        novo_usuario_janela = sg.Window("Criar Novo Usuário", novo_usuario_layout)
    
     # Criar usuário   
    elif evento == "Criar usuário":
        email = valores["email"]
        senha = valores["senha"]
        nome = valores["nome"]
        criar_usuario(email, senha, nome)
        novo_usuario_janela.hide()
    
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




