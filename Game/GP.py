# GP = GamePlay
import textwrap
import mysql.connector
import os
connection = mysql.connector.connect(
    host ='26.83.105.196',
    port = 3307,
    database = 'peli_projekti',
    user = 'code',
    password = '1',
    autocommit = True
)



#def alotuspiste()


def idea():
    def get_idea():
        pelinidea = ''' Collect points from fly distance and from the different airports you land your plane, but remember to watch your fuel! If you run out of fuel in the middle of the game, it's game over.
        You can get more fuel from the airports where you land. Check the leaderboard after the game to see how you did!! Have fun!'''

        wrapper = textwrap.TextWrapper(width=80, break_long_words=False, replace_whitespace=False)

        word_list = wrapper.wrap(text=pelinidea)
        return word_list
    ideadialog = input("Do you want to know the game's idea or just jump blindly in the hornet's nest?? (IDEA/HORNET):")
    os.system('cls')
    if ideadialog == 'IDEA':
        for line in get_idea():
            print(line)

def ICAO():
    sql ="select ident, latitude_deg, longitude_deg from airport where type like %_airport order by rand() limit 1;"
    cursor = connection.cursor()
    cursor.execute(sql)
    outcome = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in outcome:
            ICAO1 = row[1]
    return ICAO1


def endpoint(ICAO1):
    sql = "SELECT name, latitude_deg, longitude_deg FROM airport Where airport.ident ='" + ICAO1 + "'"
    print(sql)
    kursori = connection.cursor()
    kursori.execute(sql)
    tulos1 = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos1:
            latitude = rivi[1]
            longitude = rivi[2]
            print(f"Kenttä: {rivi[0]} North-south{rivi[1]} east-west {rivi[2]}")
    return latitude, longitude