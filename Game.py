import mysql.connector
from time import sleep
import os

import geopy.distance

connection = mysql.connector.connect(
    host ='26.83.105.196',
    port = 3307,
    database = 'peli_projekti',
    user = 'code',
    password = '1',
    autocommit = True
)

def search_ICAO(input1, input2):
    sql_command = "SELECT airport.latitude_deg, airport.longitude_deg FROM airport WHERE ident ='" + input1 + "' OR ident = '" + input2 + "'"
    airport = ()
    cursor = connection.cursor()
    cursor.execute(sql_command)
    total = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in total:
            airport += row[0], row[1]
    return airport


def create_new_player(username):
    sql_command = "INSERT INTO player_stat(screen_name, fuel_consumed, fuel, points) values('" + username + "', 0, 10000,0)"
    cursor = connection.cursor()
    cursor.execute(sql_command)
    total = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in total:
            print(row)




player_name = input("Name the player: ")
create_new_player(player_name)
"""ICAO1,ICAO2= input("Anna ekan kentän ISCO: "), input("Anna tokan kentän ISCO: ")
cordinates = search_ICAO(ICAO1,ICAO2)
place1 = cordinates[0],cordinates[1]
place2 = cordinates[2], cordinates[3]
print(f"Lentokenttien etäisyys on: {geopy.distance.distance(place1,place2).km:1.2f}km")
"""

sleep(4) #Peli jäätyy näkymään ja ei ota inputteja vastaan
os.system('cls') # puhdistaa taulun, niin voi piirtää uuden taulun.