import psycopg2

instance_name = "sat-kapita-selekta-basia-southeast2training-kapita-selekta"
host = "localhost"
port = 5432
db = "postgres"
user = "postgres"
password = "FwF6qfEA5AzlztzG"

# pakai /cloudsql/{instance_name} jika sudah ingin di deploy
# param = f"host='/cloudsql/{instance_name}' port={port} dbname='{db}' user='{user}' password='{password}'"
param = f"host='{host}' port={port} dbname='{db}' user='{user}' password='{password}'"
conn = psycopg2.connect(param)

query = "select current_date"
curs = conn.cursor()
curs.execute(query)
data = curs.fetchall()
print(data)

# function ini tinggal di panggil ke app.py lalu kirim param querynya tapi janggan lupa masukan dalam try/except


def select(query=""):
    try:
        conn = psycopg2.connect(param)
        curs = conn.cursor()
        curs.execute(query)

        data = curs.fetchall()
        curs.close()
        del (conn)

        return True, data
    except:
        return False, list()
