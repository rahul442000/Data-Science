import pandas as pd 
  
# reading csv file  
season_data=pd.read_csv("Season.csv")
ball_data=pd.read_csv("Ball_by_Ball.csv")
player_data=pd.read_csv("Player.csv")
team_data=pd.read_csv("Team.csv")
match_data=pd.read_csv("Match.csv")
pl_match_data=pd.read_csv("Player_Match.csv")

print("Season Data:\n",season_data.head(5))
print(season_data.dtypes)
print("\n\n")
print("Ball by ball:\n",ball_data.head(5))
print(ball_data.dtypes)
print("\n\n")
print("Player data:\n",player_data.head(5))
print(player_data.dtypes)
print("\n\n")
print("Team data:\n",team_data.head(5))
print(team_data.dtypes)
print("\n\n")
print("Match data:\n",match_data.head(5))
print(match_data.dtypes)
print("\n\n")
print("Player match data:\n",pl_match_data.head(5))
print(pl_match_data.describe(include='all'))
print(pl_match_data.dtypes)
