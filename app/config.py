SECRET_KEY = "agenda"

SQLALCHEMY_DATABASE_URI = \
    "{SGBD}://{usuario}:{senha}@{servidor}/{database}".format(
    SGBD = "postgresql",
    usuario = "david",
    senha = "123456",
    servidor = "localhost:5433",
    database = "postgres"
)