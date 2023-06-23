'''
Listas em python
tipo list - mutável
suporta vários valores de qualquer tipo
conhecimento reutilizaveis - indices e fatiamento
metodos uteis: 
        append, insert , pop, del, clear, extend, +
Create Read Update Delete
Criar, ler, alterar, apagar = lista[i]  (CRUD)     
'''
#string = 'ABCDE' # 5 caracteres (len)
#lista = [123, True, 'Vinicius', 1.2, []]
#print(lista, type(lista))
#print(lista[2])
#        0    1   2   3   4   5
lista = [10, 20, 30, 40, 50, 60]
lista[2] = 300
del lista[2]
print(lista)
print(lista[2])


#programa lista de compras


'''# Dicionário com e-mails e senhas
usuarios = {"usuario1@email.com": "senha1", "usuario2@email.com": "senha2"}

# Dicionário com e-mails e nomes de usuários
nomes = {"usuario1@email.com": "Usuario1", "usuario2@email.com": "Usuario2"}

# Função para verificar se o e-mail e a senha estão corretos
def verificar_usuario(email, senha):
    if email in usuarios and usuarios[email] == senha:
        return True
    else:
        return False

# Função para criar um novo usuário
def criar_usuario(email, senha, nome):
    if email not in usuarios:
        usuarios[email] = senha
        nomes[email] = nome
        print("Usuário criado com sucesso")
    else:
        print("E-mail já existe")

# Menu principal
while True:
    opcao = input("Digite a opção desejada: (1) Acessar, (2) Criar novo usuário, (3) Sair: ")
    
    # Acessar o programa
    if opcao == "1":
        email = input("Digite o e-mail: ")
        senha = input("Digite a senha: ")
        if verificar_usuario(email, senha):
            print(f"Seja bem-vindo {nomes[email]}, selecione a opção desejada")
            break
        else:
            print("Acesso negado")
    
    # Criar novo usuário
    elif opcao == "2":
        email = input("Digite o e-mail: ")
        senha = input("Digite a senha: ")
        nome = input("Digite o nome do usuário: ")
        criar_usuario(email, senha, nome)
    
    # Sair do programa
    elif opcao == "3":
        break
    

# Lista de compras
lista_de_compras = []

def adicionar_item(nome, quantidade, preco_unitario):
    """
    Adiciona um item à lista de compras.
    
    :param nome: Nome do item
    :type nome: str
    :param quantidade: Quantidade do item
    :type quantidade: int
    :param preco_unitario: Preço unitário do item
    :type preco_unitario: float
    """
    item = {"nome": nome, "quantidade": quantidade, "preco_unitario": preco_unitario}
    lista_de_compras.append(item)

def remover_item(nome):
    """
    Remove um item da lista de compras.
    
    :param nome: Nome do item a ser removido
    :type nome: str
    """
    for item in lista_de_compras:
        if item["nome"] == nome:
            lista_de_compras.remove(item)
            break

def atualizar_item(nome_antigo, nome_novo, quantidade_nova, preco_unitario_novo):
    """
    Atualiza um item da lista de compras.
    
    :param nome_antigo: Nome do item a ser atualizado
    :type nome_antigo: str
    :param nome_novo: Novo nome do item
    :type nome_novo: str
    :param quantidade_nova: Nova quantidade do item
    :type quantidade_nova: int
    :param preco_unitario_novo: Novo preço unitário do item
    :type preco_unitario_novo: float
    """
    for item in lista_de_compras:
        if item["nome"] == nome_antigo:
            item["nome"] = nome_novo
            item["quantidade"] = quantidade_nova
            item["preco_unitario"] = preco_unitario_novo
            break

def ler_lista():
    """
    Lê a lista de compras e mostra o total da quantidade e do preço dos itens.
    """
    print("Sua lista de compras:")
    total_quantidade = 0
    total_preco = 0
    for item in lista_de_compras:
        preco = int(item['quantidade']) * float(item['preco_unitario'])
        print(f"Nome: {item['nome']}, Quantidade: {item['quantidade']}, Preço Unitário: {item['preco_unitario']}, Preço: {preco}")
        total_quantidade += int(item['quantidade'])
        total_preco += preco
    print(f"Total da quantidade: {total_quantidade}")
    print(f"Total do preço: {total_preco}")

while True:
    opcao = input("Digite a opção desejada: (1) Adicionar item, (2) Remover item, (3) Atualizar item, (4) Ler lista, (5) Sair: ")
    
    # Adicionar item à lista de compras
    if opcao == "1":
        nome = input("Digite o nome do item que deseja adicionar: ")
        quantidade = input("Digite a quantidade do item que deseja adicionar: ")
        preco_unitario = input("Digite o preço unitário do item que deseja adicionar: ")
        adicionar_item(nome, quantidade, preco_unitario)
    
     # Remover item da lista de compras   
    elif opcao == "2":
        nome = input("Digite o nome do item que deseja remover: ")
        remover_item(nome)
    
     # Atualizar item da lista de compras   
    elif opcao == "3":
        nome_antigo = input("Digite o nome do item que deseja atualizar: ")
        nome_novo = input("Digite o novo nome do item: ")
        quantidade_nova = input("Digite a nova quantidade do item: ")
        preco_unitario_novo = input("Digite o novo preço unitário do item: ")
        atualizar_item(nome_antigo, nome_novo, quantidade_nova, preco_unitario_novo)
    
     # Ler a lista de compras   
    elif opcao == "4":
        ler_lista()
    
     # Sair do programa   
    elif opcao == "5":
        break'''

#versao 2.0 com banco de dados implementado

'''import sqlite3

# Conectar ao banco de dados (ou criar um novo se ele não existir)
conn = sqlite3.connect('lista_de_compras.db')
c = conn.cursor()

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

# Função para verificar se o e-mail e a senha estão corretos
'''def verificar_usuario(email, senha):
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
        print("Usuário criado com sucesso")
    else:
        print("E-mail já existe")
    
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
    print("Sua lista de compras:")
    total_quantidade = 0
    total_preco = 0
    for item in itens:
        preco = item[2] * item[3]
        print(f"Nome: {item[1]}, Quantidade: {item[2]}, Preço Unitário: {item[3]}, Preço: {preco}")
        total_quantidade += item[2]
        total_preco += preco
    print(f"Total da quantidade: {total_quantidade}")
    print(f"Total do preço: {total_preco}")

# Menu principal
while True:
    opcao = input("Digite a opção desejada: (1) Acessar, (2) Criar novo usuário, (3) Sair: ")
    
     # Acessar o programa   
    if opcao == "1":
        email = input("Digite o e-mail: ")
        senha = input("Digite a senha: ")
        if verificar_usuario(email, senha):
            nome_usuario = obter_nome_usuario(email)
            print(f"Seja bem-vindo {nome_usuario}, selecione a opção desejada")
            
             # Menu da lista de compras   
            while True:
                opcao_lista = input("Digite a opção desejada: (1) Adicionar item, (2) Remover item, (3) Atualizar item, (4) Ler lista, (5) Sair: ")
                
                 # Adicionar item à lista de compras   
                if opcao_lista == "1":
                    nome = input("Digite o nome do item que deseja adicionar: ")
                    quantidade = int(input("Digite a quantidade do item que deseja adicionar: "))
                    preco_unitario = float(input("Digite o preço unitário do item que deseja adicionar: "))
                    adicionar_item(nome, quantidade, preco_unitario)
                
                 # Remover item da lista de compras   
                elif opcao_lista == "2":
                    nome = input("Digite o nome do item que deseja remover: ")
                    remover_item(nome)
                
                 # Atualizar item da lista de compras   
                elif opcao_lista == "3":
                    nome_antigo = input("Digite o nome do item que deseja atualizar: ")
                    nome_novo = input("Digite o novo nome do item: ")
                    quantidade_nova = int(input("Digite a nova quantidade do item: "))
                    preco_unitario_novo = float(input("Digite o novo preço unitário do item: "))
                    atualizar_item(nome_antigo, nome_novo, quantidade_nova, preco_unitario_novo)
                
                 # Ler a lista de compras   
                elif opcao_lista == "4":
                    ler_lista()
                
                 # Sair do menu da lista de compras   
                elif opcao_lista == "5":
                    break
        else:
            print("Acesso negado")
    
     # Criar novo usuário   
    elif opcao == "2":
        email = input("Digite o e-mail: ")
        senha = input("Digite a senha: ")
        nome = input("Digite o nome do usuário: ")
        criar_usuario(email, senha, nome)
    
     # Sair do programa   
    elif opcao == "3":
        break'''








