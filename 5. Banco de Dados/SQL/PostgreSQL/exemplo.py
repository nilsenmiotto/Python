import psycopg2
from psycopg2.extras import RealDictCursor

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="meu_banco",
    user="postgres",
    password="mudar123",
)

with conn:
    with conn.cursor(cursor_factory=RealDictCursor) as cur:

        cur.execute("INSERT INTO usuarios (nome, email) VALUES(%s, %s) RETURNING id;",
                    ("Alice", "alice@example.com")
        )

        id_recuperada = cur.fetchone()["id"]
        print(id_recuperada)

        cur.execute("SELECT id, nome, email, criado_em FROM usuarios;")
        print(cur.fetchall())

        cur.execute("UPDATE usuarios SET email = %s WHERE id = %s;",
                ("outroemail@example.com", id_recuperada))

        cur.execute("SELECT nome, email, criado_em FROM Usuarios WHERE id = %s;",
                (id_recuperada,))
        linhas = cur.fetchall()

        for linha in linhas:
            print(f"Nome: {linha["nome"]}\nEmail: {linha["email"]}\nData de criação: {linha['criado_em']}")

            cur.execute("DELETE FROM usuarios WHERE nome= %s;",
                    (linha["nome"],))

conn.close()