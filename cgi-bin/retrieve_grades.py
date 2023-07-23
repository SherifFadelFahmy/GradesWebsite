#!/usr/bin/env python

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

print("Content-Type: text/html")  # Required CGI header
print()  # Blank line indicating the end of the header

print('''
<html lang="en">
<head>
<meta name="description" content="Here are your grades, best of luck!!">
<meta name="viewport" content="width=device-width, initial-scale=1">
          <!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-W6R5CJ2PHL"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-W6R5CJ2PHL');
</script>
  <title>Your Grades Are</title>
  <link rel="stylesheet" type="text/css" href="../style.css">
</head>
<body>
  <div class="container">
    <header>
      <img src="../logo.png" alt="Logo" height="150" width="220">
      <p class="tagline">Innovate. Engineer. Educate.</p>
    </header>
    <nav>
      <ul>
        <li><a href="../index.html">About</a></li>
        <li><a href="../books.html">Books</a></li>
        <li><a href="../publications.html">Publications</a></li>
        <li><a href="../links.html">Links</a></li>
        <li><a href="../mygrades.html">Get My Grades</a></li>
        <li><a href="../games.html">Games</a></li>
        <li><a href="../dogpa.html">GPA Calculator</a></li>
      </ul>
    </nav>
    <section class="owner-section">
      <h2>Student Grades</h2>
      ''')


# Your if statement
#grades_row = None  # Example value for demonstration
#student_id = "123"  # Example value for demonstration

if grades_row is None:
    print("<p>No grades found for the provided student ID.</p>")
else:
    print("<p>Grades for student ID:", student_id, "</p>")
    print("<ul>")
    for grade in grades_row[1:]:
        print("<li>", grade, "</li>")
    print("</ul>")


print('''
    </section>
  </div>
  <footer>
    &copy; Sherif Fadel Fahmy 2023. All rights reserved.
  </footer>
</body>
</html>
''')

