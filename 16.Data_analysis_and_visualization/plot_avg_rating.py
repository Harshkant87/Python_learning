import pandas
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt

data = pandas.read_csv("course_reviews.csv", parse_dates=['Timestamp'])
# print(data.head())
data['Day'] = data['Timestamp'].dt.date
day_avg = data.groupby(['Day']).mean(numeric_only = True) #grouping according to day
# print(day_avg.index)
plt.figure(figsize = (25, 3))
plt.plot(day_avg.index, day_avg['Rating']) #placing X and Y here
plt.show()


