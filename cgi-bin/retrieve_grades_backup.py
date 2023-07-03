#!/usr/bin/env python3

import cgi
import openpyxl

# Assuming the Excel file is named "grades.xlsx"
excel_file = '/var/data/grades.xlsx'

# Read the student ID from the form data
form = cgi.FieldStorage()
student_id = form.getvalue('studentId')
student_id=int(student_id)

# Load the Excel file and retrieve the grades for the student ID
workbook = openpyxl.load_workbook(excel_file)
worksheet = workbook.active
grades_row = None

for row in worksheet.iter_rows(values_only=True):
    if row[0] == student_id:
        grades_row = row
        break

# Generate the HTML response
print("Content-type: text/html")
print()
print("<html>")
print("<head>")
print("  <title>Student Grades</title>")
print("</head>")
print("<body>")
print("<h1>Student Grades</h1>")

if grades_row is None:
    print("<p>No grades found for the provided student ID.</p>")
else:
    print("<p>Grades for student ID:", student_id, "</p>")
    print("<ul>")
    for grade in grades_row[1:]:
        print("<li>", grade, "</li>")
    print("</ul>")

print("</body>")
print("</html>")

