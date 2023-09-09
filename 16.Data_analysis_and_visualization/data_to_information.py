import pandas
from datetime import datetime
from pytz import utc

data = pandas.read_csv("course_reviews.csv", parse_dates=['Timestamp'])
#1. Average rating for progress
print(data[data['Progress'] > 5.0]['Rating'].mean())

#2. Average rating for Question asked
print(data[data['Questions Asked'] > 2.0]['Rating'].mean())

#3. Average rating for Question Answered
print(data[data['Questions Answered'] > 2.0]['Rating'].mean())

#4. Number of courses with certain rating
print(data[data['Rating'] > 1.0 ].count())
