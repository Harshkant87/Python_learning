def mean(myList):
    if type(myList) == dict: # checking the type of data type given
        mean_value = sum(myList.values()) / len(myList.values())
    else:
        mean_value = sum(myList) / len(myList)
    return mean_value

student_grades = {
    "Harsh" : 90,
    "Ayush" : 85.4,
    "Abhinav" : 97
}

grades = [33, 46, 39]

print(mean(student_grades))
print(mean(grades))