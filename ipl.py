import numpy as np
import pandas as pd

matches = pd.read_csv('datasets/ipl-matches.csv')
print(matches.head(5))

def teamsAPI():
    teams= list(set(list(matches['Team1']) + list(matches['Team2'])))
    team_dict = {
        'teams':teams
    }
    return team_dict

def teamVteamAPI(team1,team2):
    temp_df = matches[(matches['Team1'] == team1) & (matches['Team2'] == team2) | (
                (matches['Team2'] == team1) & (matches['Team1'] == team2))]
    total_matches = temp_df.shape[0]
    matches_won_team1 = temp_df['WinningTeam'].value_counts()[team1]
    matches_won_team2 = temp_df['WinningTeam'].value_counts()[team2]
    draws = total_matches - (matches_won_team1 + matches_won_team2)
    response = {
        'total_matches': str(total_matches),
        team1: str(matches_won_team1),
        team2: str(matches_won_team2),
        'draws': str(draws)
    }
    return response