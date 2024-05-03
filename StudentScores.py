import pandas as pd


def calculate_grade(x):
    # calculates the grade
    grade = x['Midterm Exam- 100 Pts.'] * 0.2 + x['Final Exam- 100 Pts.'] * 0.2 + x['Project 1- 100 Pts.'] * 0.3 + x[
        'Project 2 - 100 Pts.'] * 0.3
    x['Grade'] = grade  # sets the grade column
    # sets the letter grade column
    if grade >= 90:
        x['Letter grade'] = 'A'
    elif grade >= 80:
        x['Letter grade'] = 'B'
    elif grade >= 70:
        x['Letter grade'] = 'C'
    else:
        x['Letter grade'] = 'D'
    return x


df = pd.read_csv('Ten_Students_Scores.csv')
df = df.apply(calculate_grade, axis=1)  # applies the function to all rows
df.to_csv('Ten_Students_Grades.csv')
