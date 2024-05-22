import requests
import json


def fetch_player_data(player_id, league_id, team_id, season):
    url = "https://api-football-v1.p.rapidapi.com/v3/players"

    querystring = {
        "id"    : player_id,
        "league": league_id,
        "team"  : team_id,
        "season": season
    }

    headers = {
        "X-RapidAPI-Key" : "4d8d14fda7msh01627ef5ab0f03fp14055bjsn2d65330d45b3",
	    "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    response.raise_for_status()
    return response.json()



def combine_player_data(player_ids, league_ids, team_ids, season, output_file):
    all_players_data = {
        "players": []
    }

    for player_id, league_id, team_id in zip(player_ids, team_ids, league_ids):
        player_data = fetch_player_data(player_id, league_id, team_id, season)
        all_players_data["players"].append(player_data)

    with open(output_file, "w") as file:
        json.dump(all_players_data, file, indent=4)



player_ids = ["274", "51070", "157", "642"]
league_ids = ["61", "39", "140", "39"]
team_ids = ["85", "33", "529", "50"]  
season = "2016"
file_name = "player_stats.json"

combine_player_data(player_ids, league_ids, team_ids, season, file_name)