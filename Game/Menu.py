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

#Tekee uuden käyttäjän ja lisää sen tietokantaan. Käytetään lopulisen uuden pelin luoti funktiossa
def create_new_player(username, difficulty):
        sql_command = "INSERT INTO player_stat(screen_name, fuel_consumed, fuel, points, difficulty) values('" + username + "', 0, 10000,0,'" + difficulty + "')"
        cursor = connection.cursor()
        cursor.execute(sql_command)
        total = cursor.fetchall()
        if cursor.rowcount > 0:
            for row in total:
                print(row)

#Tarkistaa onko vaikeus taso oikein kirjoitettu. Käytetään lopulisen uuden pelin luoti funktiossa
def diffcheck():
    while True:
        user = input("Go back, Easy, Medium or Hard: ")
        os.system('cls')
        if user == "Go back" or user == "go back":
            return "go back"

        elif user == "Easy" or user == "easy":
            return "easy"


        elif user == "Medium" or user == "medium":
            return "medium"

        elif user == "Hard" or user == "hard":
            return "hard"

        else:
            print("Wrong input!")

#Tarkistaa onko aloitus piste oikein kirjoitettu. Käytetään lopulisen uuden pelin luoti funktiossa
def new_continent(continent):
    while True :
        if continent == "Europe" or continent == "europe":
            return "EU"
        elif continent == "North-America" or continent == "north-america":
            return "NA"
        elif continent == "South-America" or continent == "south-america":
            return "SA"
        elif continent == "Oceania" or continent == "oceania":
            return "OC"
        elif continent == "Africa" or continent == "africa":
            return "AF"
        elif continent == "Asia" or continent == "asia":
            return "AS"
        elif continent == "Antartica" or continent == "antartica":
            return "AN"
        if continent == "Go back" or continent == "go back":
            return "go back"
        else: print("Wrong input!")

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
    difficulty = diffcheck()
    os.system('cls')
    if difficulty == "go back":
        return


    #Aloitus pisteen valinta
    bot_UI()
    print("Choose continent where to start or go back")
    print("")
    print("Europe = Helsinki Vantaa airport Finland")
    print("North-america = John F. Kennedy International Airport USA")
    print("South-america = Brasilia international Airport Brazil")
    print("Asia = Netaji Subas Chandra Bosen International Airport India")
    print("Africa = O. R. Tambo International Airport Shout Africa, Africa")
    print("Oceania = Sydney Airport, Australia, Oceania")
    print("Antarctica = Boulder Clay Runaway Airport, Antarctica")
    bot_UI()
    continent = new_continent()
    if continent == "go back":
        return
