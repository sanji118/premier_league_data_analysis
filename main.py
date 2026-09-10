import pandas as pd
import matplotlib.pyplot as plt

#Read data
data = pd.read_csv('C:/programming_course_1/python-course/premier_league_data_analysis/premier_league_data.csv')
print(data.head())

data["TotalGoals"] = data["FTHG"]+data["FTAG"]

print('\nTotal goals:', data["TotalGoals"].sum())