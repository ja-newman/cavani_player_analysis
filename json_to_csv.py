import csv
import json

with open("cavani_2016_stats.json", "r") as stats:
    data = json.load(stats)

# Extract player info
player = data['response'][0]['player']

# Extract statistics
statistics = data['response'][0]['statistics']

# Prepare CSV data
csv_data = []

# Header
header = [
    "player_id", "name", "firstname", "lastname", "age", "birth_date", "birth_place", "birth_country",
    "nationality", "height", "weight", "injured", "photo", "team_id", "team_name", "team_logo",
    "league_id", "league_name", "league_country", "league_logo", "league_flag", "season",
    "appearances", "lineups", "minutes", "position", "rating", "captain", "sub_in", "sub_out", "bench",
    "shots_total", "shots_on", "goals_total", "goals_assists", "passes_total", "passes_key", "passes_accuracy",
    "tackles_total", "interceptions", "duels_total", "duels_won", "dribbles_attempts", "dribbles_success",
    "fouls_drawn", "fouls_committed", "cards_yellow", "cards_yellowred", "cards_red", "penalty_won",
    "penalty_committed", "penalty_scored", "penalty_missed"
]
csv_data.append(header)

# Add player statistics
for stat in statistics:
    row = [
        player['id'], player['name'], player['firstname'], player['lastname'], player['age'],
        player['birth']['date'], player['birth']['place'], player['birth']['country'],
        player['nationality'], player['height'], player['weight'], player['injured'], player['photo'],
        stat['team']['id'], stat['team']['name'], stat['team']['logo'],
        stat['league']['id'], stat['league']['name'], stat['league']['country'], stat['league']['logo'], stat['league'].get('flag', ''),
        stat['league']['season'], stat['games']['appearences'], stat['games']['lineups'], stat['games']['minutes'],
        stat['games']['position'], stat['games']['rating'], stat['games']['captain'], stat['substitutes']['in'],
        stat['substitutes']['out'], stat['substitutes']['bench'], stat['shots']['total'], stat['shots']['on'],
        stat['goals']['total'], stat['goals']['assists'], stat['passes']['total'], stat['passes']['key'],
        stat['passes']['accuracy'], stat['tackles'].get('total', ''), stat['tackles'].get('interceptions', ''),
        stat['duels']['total'], stat['duels']['won'], stat['dribbles']['attempts'], stat['dribbles']['success'],
        stat['fouls']['drawn'], stat['fouls']['committed'], stat['cards']['yellow'], stat['cards']['yellowred'],
        stat['cards']['red'], stat['penalty'].get('won', ''), stat['penalty'].get('commited', ''),
        stat['penalty']['scored'], stat['penalty'].get('missed', '')
    ]
    csv_data.append(row)

# Write to CSV file
with open('cavani_2016_stats.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)