SECRET_KEY = '123'
SESSION_PERMANENT = False

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
    SGBD = 'postgresql',
    usuario = "denega",
    senha = "123456",
    servidor = "localhost:5450",
    database = "postgres"
)