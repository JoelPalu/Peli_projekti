import os

#Peli prosessin ylä osa UI:sta
def head_UI(user,money):
    print(f"________________________________________________________")
    print(f"{user}            {money}")

#UI:n ala ja yläviiva
def bot_UI():
    print(f"________________________________________________________")

#Menu. Palauttaa valittu vaihtehto numerona.
def menu():
    bot_UI()
    print("1    New Game")
    print("2    Continue")
    print("3    Leaderboard")
    print("4    Quit")
    bot_UI()
    choice = int(input("Go to: "))
    os.system('cls')
    return choice

#Tekee uuden käyttäjän ja lisää sen tietokantaan.
def create_new_player(username, difficulty):
        sql_command = "INSERT INTO player_stat(screen_name, fuel_consumed, fuel, points, difficulty) values('" + username + "', 0, 10000,0,'" + difficulty + "')"
        cursor = connection.cursor()
        cursor.execute(sql_command)
        total = cursor.fetchall()
        if cursor.rowcount > 0:
            for row in total:
                print(row)

#Uuden pelin luominen. ja lisääminen tietokantaan.
def new_game():

    bot_UI()
    #Pelaajan nimi luonti
    print("Create new player")
    bot_UI()
    username = input("Give username: ")
    os.system('cls')
    #Vaikeustason valinta
    bot_UI()
    print("Choose difficulty or Go back: ")
    print("Difference between difficulties:")
    print("Easy: small plane uses less fuel and can land at any type of airfield.")
    print("Medium: Medium plane uses 50% more fuel and needs at least medium airport to land.")
    print("Hard: largest airplane uses 75% more fuel needs at least large airport to land.")
    bot_UI()
    difficulty = input("Go back, Easy, Medium or Hard: ")
    os.system('cls')
    if difficulty == "Go back" or difficulty == "go back":
        return

    bot_UI()
    print("Choose where to start")


    print("Europe = Helsinki Vantaa airport Finland")
    print("North-america = John F. Kennedy International Airport USA")
    print("South-america = Brasilia international Airport Brazil")
    print("Asia = Netaji Subas Chandra Bosen International Airport India")
    print("Africa = O. R. Tambo International Airport Shout Africa, Africa")
    print("Oceania = Sydney Airport, Australia, Oceania")
    print("Antarctica = Boulder Clay Runaway Airport, Antarctica")
    bot_UI()


    while difficulty != "Go back" and difficulty != "go back":
        if difficulty == "Easy" or difficulty == "easy":
            difficulty = "easy"

        elif difficulty == "Medium" or difficulty == "medium":
            difficulty = "medium"

        elif difficulty == "Hard" or difficulty == "hard":
            difficulty = "hard"

        else: print("Wrong input!")
"""
def new_continent(continent):
    while continent != "Go back" and continent != "go back":
        if continent == "Europe" or continent == "europe":

        elif continent == "North-America" or continent == "north-america":

        elif continent == "South-America" or continent == "south-america":

        elif continent == "Oceania" or continent == "oceania":

        elif continent == "Africa" or continent == "africa":

        elif continent == "Asia" or continent == "asia":

        elif continent == "Antartica" or continent == "antartica":
            
        else: print("Wrong input!")
"""