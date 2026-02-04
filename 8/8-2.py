import mysql.connector


connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='Alekai',
    password='MoiOpet:)',
    autocommit=True
)


def GetAirportCount(country):
    sql = f"SELECT * FROM airport WHERE iso_country='{country}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    val = cursor.fetchall()
    i = 0
    if cursor.rowcount > 0:
        for n in val:
            i += 1
    return i


def main():
    code = input("country Code: ")
    print(GetAirportCount(code))


main()
