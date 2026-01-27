import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "mudar123",
    "host": "127.0.0.1",
    "port": 3306,
    "database": "meu_banco"
}

try:
    with mysql.connector.connect(**config) as conn:

        conn.ping(reconnect=True, attempts=3, delay=2)

        with conn.cursor(dictionary=True) as cur:

            cur.execute("INSERT INTO usuarios (nome, email) VALUES(%s, %s);",
                ("Alice", "alice@example.com")
            )
            conn.commit()

            id_recuperada = cur.lastrowid

            cur.execute("UPDATE usuarios SET email = %s WHERE id = %s;",
                ("outroemail@example.com", id_recuperada))
            conn.commit()

            cur.execute("SELECT nome, email, criado_em FROM Usuarios WHERE id = %s;",
                    (id_recuperada,))
            linhas = cur.fetchall()

            for linha in linhas:
                print(f"Nome: {linha["nome"]}\nEmail: {linha["email"]}\nData de criação: {linha['criado_em']}")

                cur.execute("DELETE FROM usuarios WHERE nome= %s;",
                        (linha["nome"],))
                conn.commit()


except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Usuário ou senha incorretos")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Banco de dados não existe")
    else:
        print(f"Erro: {err}")