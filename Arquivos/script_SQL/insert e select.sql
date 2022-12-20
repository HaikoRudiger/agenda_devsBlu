SELECT * FROM usuario;

INSERT INTO usuario (id, username, nome, admin, senha)
	VALUES (1, 'david', 'David Simas', true, '123456');

INSERT INTO usuario (id, username, nome, admin, senha)
	VALUES (2, 'felipe', 'Felipe Weiss', true, '123456');


SELECT * FROM evento;

INSERT INTO evento (id, id_usuario, data_evento, titulo, descricao, publico, ativo)
	VALUES (4, 2, '20221220', 'Trabalho', 'Trabalho de aulas Python', true, true);

INSERT INTO evento (id, id_usuario, data_evento, titulo, descricao, publico, ativo)
	VALUES (5, 2, '20221225', 'Natal', 'Festa de Natal', true, true);

INSERT INTO evento (id, id_usuario, data_evento, titulo, descricao, publico, ativo)
	VALUES (6, 2, '20221221', 'Trabalho', 'Apresentar Trabalho', true, true);


SELECT 
	evento.id "Código Evento",
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
INNER JOIN usuario ON usuario.id = evento.id_usuario
WHERE username = 'david';

where id_usuario = 1;

select * from evento where id_usuario = 1;
