import psycopg2

print("Teste de conexão")

try:
    conn = psycopg2.connect(
    host = "localhost",
    port ="5450",
    database = "postgres", 
    user="denega", password = "123456")
    print('CONECTADO')

except Exception:
    print('VOCE ESTA SEM CONEXAO!')


if conn is not None:
    
    print('Sua Conexao está estabilizada!')

    cursor = conn.cursor()
    
    cursor.execute('CREATE TABLE IF NOT EXISTS usuario (id serial, username VARCHAR(50) NOT NULL, nome VARCHAR(50)  NOT NULL, admin bool NOT NULL, senha VARCHAR(256) NOT NULL);')
        
    cursor.execute('ALTER TABLE usuario ADD PRIMARY KEY(id);')
    
    print('Sua tabela USUARIO foi criada!')
    

    cursor.execute('CREATE TABLE evento  (id serial, id_usuario int NOT NULL, data_evento date NOT NULL, titulo VARCHAR(50) NOT NULL, descricao VARCHAR(200)NOT NULL, publico bool NOT NULL, ativo bool NOT NULL);')
    
    cursor.execute('ALTER TABLE evento ADD PRIMARY KEY(id);')
        
    cursor.execute('ALTER TABLE evento ADD CONSTRAINT eventos_id_usuario_foreign FOREIGN KEY(id_usuario) REFERENCES usuario(id);')
    
    
    print('Sua tabela EVENTO foi criada!')

    conn.commit()
    cursor.close()
    conn.close()
    
'''
/
/login
/autenticar
/cadastrar evento
/cadastro usuario
/calendario (tabela)
/editar
/deletar
/logout

'''