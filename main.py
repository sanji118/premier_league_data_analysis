import pandas as pd
import matplotlib.pyplot as plt

#Read data
data = pd.read_csv('C:/programming_course_1/python-course/premier_league_data_analysis/premier_league_data.csv')
print(data.head())

data["TotalGoals"] = data["FTHG"]+data["FTAG"]

print('\nTotal goals:', data["TotalGoals"].sum())
print('Average goals per match:', round(data["TotalGoals"].mean(), 2))


#highest scoring
print("\nTop 10 highest-scoring matches:")
top_matches = data.sort_values(by="TotalGoals", ascending=False)
print(top_matches[["HomeTeam", "AwayTeam", "FTHG", "FTAG", "TotalGoals"]].head(10))

#match results
print(data["FTR"].value_counts())
result = data["FTR"].value_counts()


#plot
plt.figure(figsize=(7,5))
result.plot(kind='bar')
plt.title("Premier League Match Results")
plt.xlabel("Results")
plt.ylabel("Number of Matches")
plt.show()

#goals scored by each team
home_goals = data.groupby("HomeTeam")["FTHG"].sum()
away_goals = data.groupby("AwayTeam")["FTAG"].sum()
total_goals = home_goals + away_goals
total_goals.sort_values(ascending=False)

print('\nTop 10 teams by goals scored:')
print(total_goals.head(10))

#plot
plt.figure(figsize=(9,5))
total_goals.head(10).sort_values().plot(kind='bar')
plt.title("Top 10 teams by goals scored")
plt.xlabel("Goals")
plt.ylabel("Team")
plt.show()

#create league
teams = set(data["HomeTeam"]) | set(data["AwayTeam"])

league = []

for team in teams:

    home = data[data["HomeTeam"] == team]
    away = data[data["AwayTeam"] == team]


    wins = (
        (home["FTR"] == "H").sum()
        +
        (away["FTR"] == "A").sum()
    )


    draws = (
        (home["FTR"] == "D").sum()
        +
        (away["FTR"] == "D").sum()
    )


    losses = (
        (home["FTR"] == "A").sum()
        +
        (away["FTR"] == "H").sum()
    )


    goals_for = (
        home["FTHG"].sum()
        +
        away["FTAG"].sum()
    )


    goals_against = (
        home["FTAG"].sum()
        +
        away["FTHG"].sum()
    )


    points = wins * 3 + draws

league.append([
    team,
    wins,
    draws,
    losses,
    goals_for,
    goals_against,
    points
])


table=pd.DataFrame(league, columns=["Team","Wins","Draws","Losses","GoalsFor","GoalsAgainst","Points"])

table["GoalDifference"]=table["GoalsFor"]-table["GoalsAgainst"]
table = table.sort_values(by=["Points","GoalDifference","GoalsFor"], ascending=False)
table["Position"]=range(1, len(table)+1)


print("\nFINAL LEAGUE TABLE")

print(table[["Position","Team","Wins","Draws","Losses","GoalsFor","GoalsAgainst","GoalDifference","Points"]].to_string(index=False))

