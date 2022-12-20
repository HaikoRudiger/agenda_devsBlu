SQLALCHEMY_DATABASE_URI = \
    "{SGBD}://{usuario}:{senha}@{servidor}/{database}".format(
    SGBD = "postgresql",
    usuario = "david",
    senha = "123456",
    servidor = "192.168.1.102:5432",
    database = "postgres"
)