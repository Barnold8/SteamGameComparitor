import requests
from bs4 import BeautifulSoup
import re

def getGames(ID):

    x = requests.get(f'{API}{INTERFACE}?key={API_KEY}&steamid={ID}&format={dataFormat}')
    gameNames = []
    user_games = x.json()["response"]["games"]
    for game in user_games:
        f = next((item for item in games if item["appid"] == game["appid"]), None)
        if f != None:
            gameNames.append(f["name"])
    return gameNames

API = "http://api.steampowered.com/"
INTERFACE = "IPlayerService/GetOwnedGames/v0001/"
API_KEY = input("Please enter a steamAPI key: ")
dataFormat = "json"

games = requests.get("http://api.steampowered.com/ISteamApps/GetAppList/v0002/?key=STEAMKEY&format=json")
games = games.json()["applist"]["apps"]

common = []
userIDS = []

getID = True

print("Please enter a steam UserID, or type n to finish")

while(getID):

    ID = input("SteamID: ")
    if(ID.lower() == 'n'):
        getID = False
    else:
        userIDS.append(int(ID))

print("Finding common games...")

for user in userIDS:
    common.append(getGames(user))

commonGames = list(set.intersection(*map(set,common)))
commonGames.sort()

print("The common games are: ")

for game in commonGames:
    print(game)

