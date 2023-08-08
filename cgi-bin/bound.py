#!/usr/bin/env python

import cgi
import cgitb
import os
import openpyxl
import tempfile

cgitb.enable()

# grade boundaries for post 1610 students
values = [97, 93, 89, 84, 80, 76, 73, 70, 67, 64, 60]

# grade boundaries for pre 1610 students
values2 = [95, 90, 85, 80, 75, 70, 65, 60, 56, 53, 50]

# variable to store the rows read from the excel file
data = []

# ID cutoff for the 16/40 students
cutoff2200 = 220000000

# ID cutoff from the pass out of 60, but 12/40 students
cutoff1610 = 16100000

def read_excel_file(file_path, data):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    for row in sheet.iter_rows(values_only=True):
        data.append(row)

def check_number(array, number):
    for entry in array:
        if (number >= entry - 1 and number<entry): 
            return True
    return False

def process_rows(data):
    for row in data:
        if (row[5]>=cutoff2200):
            if (row[0]>=60 and row[1]<16 and row[1]>=14):
                theid = row[5]
                number = row[6]
                print(f"<p>Student number {number} with ID {theid} should pass, please change final to 16</p>")
            elif (row[1]>=16 and row[0]<60 and row[0]>=58):
                theid = row[5]
                number = row[6]
                print(f"<p>Student number {number} with ID {theid} should pass, please add two marks to the grades out of 60</p>")
        elif (row[5]>=cutoff1610 and row[5]<cutoff2200):
            if (row[0]>=60 and row[1]<12 and row[1]>=10):
                theid = row[5]
                number = row[6]
                print(f"<p>Student number {number} with ID {theid} should pass, please change final to 12</p>")
            elif (row[1]>=12 and row[0]<60 and row[0]>=58):
                theid = row[5]
                number = row[6]
                print(f"<p>Student number {number} with ID {theid} should pass, please add two marks to the grades out of 60</p>")
        else:
            if (row[0]>=50 and row[1]<12 and row[1]>=10):
                theid = row[5]
                number = row[6]
                print(f"<p>Student number {number} with ID {theid} should pass, please change final to 12</p>")
            elif (row[1]>=12 and row[0]<50 and row[0]>=48):
                theid = row[5]
                number = row[6]
                print(f"<p>Student number {number} with ID {theid} should pass, please add two marks to the grades out of 60</p>")

def grade_boundaries(data):
    for row in data:
        if (row[5]>=cutoff1610):
            if (check_number(values,row[0])):
                theid = row[5]
                number = row[6]
                print(f"<p>Student number {number} with ID {theid} needs one grade up +1</p>")
        else:
            if (check_number(values2,row[0])):
                theid = row[5]
                number = row[6]
                print(f"<p>Student number {number} with ID {theid} needs one grade up +1</p>")

print("Content-Type: text/html")    # HTML is following
print()                             # blank line, end of headers

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

form = cgi.FieldStorage()

# Check if file was uploaded
if 'uploadedfile' in form:
    fileitem = form['uploadedfile']

    if fileitem.file:
        # It's an uploaded file; process the data
        fd, tempname = tempfile.mkstemp(suffix=".xlsx")
        with os.fdopen(fd,'wb') as f:
            f.write(fileitem.file.read())
        #temp = tempfile.NamedTemporaryFile(delete=False)
        #tempname = temp.name
        #with open(tempname, 'wb') as f:
        #    f.write(fileitem.file.read()) 
        #    print(f"The file name is {fileitem}")
        
        # functions as before but using tempname instead of excel_file_path
        read_excel_file(tempname, data)
        process_rows(data)
        grade_boundaries(data)
        
        # remove the temporary file
        os.unlink(tempname)
else:
    print("<h1>No file was uploaded</h1>")
print('''
    </section>
  </div>
  <footer>
    &copy; Sherif Fadel Fahmy 2023. All rights reserved.
  </footer>
</body>
</html>
''')

