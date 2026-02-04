import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='Alekai',
    password='MoiOpet:)',
    autocommit=True
)


def get_airport_data(icao):
    sql = f"SELECT name, iso_region FROM airport WHERE ident='{
        icao}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    val = cursor.fetchall()
    if cursor.rowcount > 0:
        for n in val:
            print(f"{icao} lentokentän nimi on {n[0]} ja se sijaitsee {
                  n[1]}")
    return val


def main():
    code = input("Syötä ICAO-koodi: ")
    get_airport_data(code)


main()
