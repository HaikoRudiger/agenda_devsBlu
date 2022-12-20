import psycopg2

print("Teste de conexão")

try:
    conn = psycopg2.connect(
    host = "192.168.1.102",
    port ="5432",
    database = "postgres", 
    user="postgres", password = "123456")
    print("Conectado")

except Exception:
    print("Você está sem conexâo.")

if conn is not None:
    
    print("Sua Conexão está estabilizada.")

    cursor = conn.cursor()
    
    cursor.execute("""CREATE TABLE usuario (
                        id serial,
                        username VARCHAR(50) NOT NULL,
                        nome VARCHAR(50) NOT NULL,
                        admin BOOL NOT NULL,
                        senha VARCHAR(256) NOT NULL,
                      PRIMARY KEY (id));""")

    print("Sua tabela USUARIO foi criada.")
    
    cursor.execute("""CREATE TABLE evento (
                        id serial,
                        id_usuario INT NOT NULL,
                        data_evento DATE NOT NULL,
                        titulo VARCHAR(50) NOT NULL,
                        descricao VARCHAR(200) NOT NULL,
                        publico BOOL NOT NULL,
                        ativo BOOL NOT NULL,
                      PRIMARY KEY (id),
                      FOREIGN KEY (id_usuario)
                        REFERENCES usuario (id));""")
        
    print("Sua tabela EVENTO foi criada")

    conn.commit()
    cursor.close()
    conn.close()

"""
SELECT * FROM usuario;

INSERT INTO usuario (id, username, nome, admin, senha)
	VALUES (1, 'david', 'David Simas', true, '123456');


SELECT * FROM evento;

INSERT INTO evento (id, id_usuario, data_evento, titulo, descricao, publico, ativo)
	VALUES (1, 1, '20221220', 'Trabalho', 'Trabalho de aulas Python', true, true);


SELECT 
	evento.id "Código",
	evento.data_evento "Data",
	evento.titulo "Título",
	evento.descricao "Descrição",
	evento.publico "Público",
	evento.ativo "Ativo",
	usuario.id "Código Usuário",
	usuario.username "Nickname",
	usuario.nome "Nome Completo",
	usuario.admin "Administrador",
	usuario.senha "Password"
FROM evento
INNER JOIN usuario ON usuario.id = evento.id_usuario;
"""
