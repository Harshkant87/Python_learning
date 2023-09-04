import pandas

data = pandas.read_csv("course_reviews.csv")
# print(data)

#1. for first five rows
print(data.head())

#2. for number of rows and cols
print(data.shape)

#3. to get name of cols
print(data.columns)

#4. for histograms
print(data.hist('Rating'))

#5. Select multiple columns
print(data[['Rating', 'Progress']])

#6. selcting row(s)
print(data.iloc[3])
print(data.iloc[[3, 7]])
print(data.iloc[1:7])

#7. selecting a section
print(data[['Rating', 'Progress']].iloc[3:8])

#8. Selecting a cell
print(data['Rating'].iloc[3])
print(data.at[3, 'Rating'])

#9. filtering data
print(data[data["Rating"] > 4.5])
print(data[data["Rating"] > 4.5].count())

#10. filtering on the basis of multiple conditions
print(data[(data['Rating'] > 4.0) & (data['Progress'] > 1.0)])