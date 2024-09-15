import psycopg

# Mostra qual versão do módulo está sendo importada
print(psycopg)

class Usuario:
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha

# Método que verifica se o usuário existe no banco de dados
def existe(usuario):
    # Abre a conexão com o banco
    with psycopg.connect(
        host="localhost",
        port=5432,
        dbname="PBDI",
        user="postgres",
        password="12345678"
    ) as conexao:
        with conexao.cursor() as cursor:
            # Executa a consulta SQL
            cursor.execute('SELECT * FROM tb_usuario WHERE login=%s AND senha=%s', (usuario.login, usuario.senha))
            # Verifica se o usuário foi encontrado
            result = cursor.fetchone()
            return result is not None

# Método que insere um novo usuário no banco de dados
def inserir(usuario):
    with psycopg.connect(
        host="localhost",
        port=5432,
        dbname="PBDI",
        user="postgres",
        password="12345678"
    ) as conexao:
        with conexao.cursor() as cursor:
            cursor.execute('INSERT INTO tb_usuario (login, senha) VALUES (%s, %s)', (usuario.login, usuario.senha))
            return cursor.rowcount >= 1

# Função do menu de opções
def menu():
    texto = "0-Fechar Sistema\n1-Login\n2-Logoff\n3-Criar Novo Usuário\n"
    usuario = None
    
    op = int(input(texto))  # Captura a opção do usuário

    # Enquanto o usuário não escolher sair (opção 0)
    while op != 0:
        if op == 1:  # Login
            login = input("Digite seu login\n")
            senha = input("Digite sua senha\n")
            usuario = Usuario(login, senha)
            print("Usuário OK!!!" if existe(usuario) else "Usuário NOK!!!")
        
        elif op == 2:  # Logoff
            usuario = None
            print("Logoff realizado com sucesso")
        
        elif op == 3:  # Criar novo usuário
            login = input("Digite login do novo usuário\n")
            senha = input("Digite senha do novo usuário\n")
            novoUsuario = Usuario(login, senha)
            print("Inserção OK!!!" if inserir(novoUsuario) else "Inserção NOK")
        
        else:
            print("Opção inválida")
        
        # Pede a próxima opção no final do loop
        op = int(input(texto))

    print("Até mais")  # Mensagem de saída

# Executa o menu
menu()
