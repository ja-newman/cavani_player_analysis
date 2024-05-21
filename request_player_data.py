import json
import requests

# Players to find:
# Edinson Cavani     ID: 274,   Team: 85 (PSG),               League: 61 (Ligue 1)
# Zlatan Ibrahimovic ID: 51070, Team: 33 (Manchester United), League: 39 (Premier League)
# Robert Lewandowski ID: 521,   Team: 157 (FC Bayern Munich), League: 78 (Bundesliga) ------> DOES NOT WORK!
# Luis Suarez        ID: 157,   Team: 529 (FC Barcelona),     League: 140 (La Liga)
# Sergio Aguero      ID: 642,   Team: 50 (Manchester City),   League: 39 (Premier League)

url = "https://api-football-v1.p.rapidapi.com/v3/players"

querystring = {
    "id"    : "__",
    "season": "____",
    "team"  : "__"
}

headers = {
	"X-RapidAPI-Key" : "4d8d14fda7msh01627ef5ab0f03fp14055bjsn2d65330d45b3",
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

# Send response to .json file.
with open("____stats.json", "w") as file:
    json.dump(response.json(), file, indent=4)