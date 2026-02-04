from geopy import distance
import mysql.connector


connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='Alekai',
    password='MoiOpet:)',
    autocommit=True
)


def GetCoordinate(icao):
    sql = f"SELECT latitude_deg, longitude_deg, name FROM airport WHERE ident='{
        icao}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    val = cursor.fetchall()
    if val == []:
        print(f"Lentokenttää {icao} ei löydetty")
        exit(1)
    elif val[0][2] != "":
        print(val[0][2])
    return (val[0][0], val[0][1])


def GetDistance(a1: tuple, a2: tuple):
    return distance.distance(a1, a2).km


def main():
    airports = []
    while len(airports) < 2:
        airports.append(GetCoordinate(input("Syötä ICAO-koodi: ")))
    print(f"Lentokenttien välinen matka on {
          GetDistance(airports[0], airports[1]):.2f} km")


main()
