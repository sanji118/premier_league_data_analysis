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
