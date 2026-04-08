import mysql.connector
from flask import Flask

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='bird_game',
    user='alekai',
    password='moiopet',
    autocommit=True
)

app = Flask(__name__)


@app.route('/kenttä/<icao>')
def get_airport_data(icao):
    sql = f"SELECT name, municipality FROM airport WHERE ident='{
        icao}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    val = cursor.fetchall()
    if cursor.rowcount > 0:
        for n in val:
            output = {
                "ICAO": icao,
                "Name": n[0],
                "Municipality": n[1]
            }
            return output


if __name__ == "__main__":
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
