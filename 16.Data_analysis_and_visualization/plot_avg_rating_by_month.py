import pandas
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


data = pandas.read_csv("course_reviews.csv", parse_dates=['Timestamp'])
# print(data.head())

data['Month'] = data['Timestamp'].dt.strftime('%Y-%m')
month_avg = data.groupby(['Month', 'Progress']).mean(numeric_only = True)
dates = []
progress = []

for i in range(0, len(month_avg.index)):
    time = float(month_avg.index[i][0].replace("-",""))
    dates.append(time)
    progress.append(month_avg.index[i][1])

fig = plt.figure()
 
# syntax for 3-D projection
ax = plt.axes(projection ='3d')
 
# plotting
ax.plot3D(dates, progress, month_avg['Rating'], 'green')
ax.set_title('3D line plot for rating, progress and date')
plt.show()
# print(len(month_avg.index))
# month_avg.plot(figsize=(15, 8))

