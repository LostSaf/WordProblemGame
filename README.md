# WordProblemGame

Project Overview
This project is a Flask web app that helps users solve word problems based on different categories (Travel, Geometry, and Shopping). The project consists of HTML files, a Python script (app.py), and a CSS file for styling. The HTML is used to create the webpage's structure, the CSS file is used to style the pages, and the Python script runs the server and handles the app's logic.

File Breakdown and Instructions
1. app.py - The Main Python Script
Language: Python
Purpose: Manages the server and handles user requests. It also holds the logic for generating random problems and validating answers.

Key Parts of app.py:
Flask Setup:

python
Copy code
from flask import Flask, render_template, request, redirect, url_for, flash
import random

app = Flask(__name__)
app.secret_key = "your_secret_key"
Flask is a lightweight web framework. It helps us create and run a web server.
The secret_key is needed for managing sessions and secure flash messages.
Problem Definitions:

python
Copy code
word_problems = {
    # Each category has its own set of problems
    "travel": [ ... ], 
    "geometry": [ ... ],
    "shopping": [ ... ]
}
This section contains word problems for each category. Each problem includes a formula for the answer and units for the answer.
Logic for Generating Problems:

python
Copy code
def generate_random_problem(category):
    # Chooses a random problem and calculates the correct answer
This function picks a random question from the chosen category and fills it with random numbers.
Routes for Pages:

python
Copy code
@app.route('/')
def welcome():
    return render_template("welcome.html")
Routes define what users see when they visit a specific page. Each @app.route() decorator maps a URL path (like /home) to a specific function that loads an HTML page.
Running the Server:

python
Copy code
if __name__ == "__main__":
    app.run(debug=True)
This part runs the server when you execute the file with python app.py.
How to Edit app.py:

Adding Problems: Add more problems to the word_problems dictionary. Follow the same structure as other problems.
Changing Categories: Add new keys to word_problems and update the HTML to display new categories.
Styling Flash Messages: You can change the flash messages by modifying their text or categories in functions like check().
2. templates/ Folder - HTML Files
Language: HTML
Purpose: Creates the structure of your web pages. HTML stands for Hypertext Markup Language and is the standard language for building web pages.

Key HTML Files:

welcome.html - Welcome Page
This file displays a welcome message with a button to start the quiz.

html
Copy code
<h1>Welcome to the Word Problem Quiz!</h1>
<a href="{{ url_for('home') }}">Start</a>
The button uses url_for to link to the homepage. If you want to change the welcome message, just update the text inside <h1> tags.
home.html - Category Selection Page
Displays the categories as clickable boxes with images.

html
Copy code
<div class="category-container">
    <a href="{{ url_for('category', category='travel') }}">
        <img src="{{ url_for('static', filename='images/travel.png') }}" alt="Travel">
        <p>Travel</p>
    </a>
    <!-- Other categories... -->
</div>
You can change the images or names for each category by replacing the src attribute or <p> text.
category.html - Question Display Page
Shows the question, allows users to input their answer, and displays the answer’s unit.

html
Copy code
<div class="input-group">
    <input type="text" id="answer" name="answer" class="form-control" pattern="\d*">
    <div class="input-group-append">
        <span>{{ units }}</span>
    </div>
</div>
You can modify the page layout or text by editing the HTML elements and attributes.
How to Edit HTML Files:

Changing Text: Just replace the text between HTML tags, like <h1>Welcome to the Quiz</h1>.
Adding New Categories: Add new <a> tags in home.html and update the route in app.py to handle them.
Changing Images: Replace the file path in src="{{ url_for('static', filename='images/travel.png') }}".
3. static/ Folder - CSS File and Images
Languages: CSS and Image Files (PNG)
Purpose: Adds styling and images for the web pages.

styles.css - Styling File
Contains custom styles for making the web pages look nice. CSS stands for Cascading Style Sheets and allows you to apply design rules to HTML elements.

css
Copy code
.category-card {
    width: 150px;
    height: 150px;
    border-radius: 15px;
    background-color: #f0f8ff;
}
You can change the size, colors, and other properties by modifying CSS properties like width, height, and background-color.
images/ Folder - Image Files
Contains images for each category. You can replace or add images here and update the corresponding HTML.

How to Edit CSS Files:

Changing Colors: Update the color values like #f0f8ff to your preferred color code.
Resizing Elements: Change the values for width and height to make elements larger or smaller.
How to Add or Change Images:

Adding a New Image: Place the image in the static/images folder and update the corresponding HTML <img src="..."> tag to point to the new image.
How It All Works Together
When You Visit the App: You start at the welcome route (/), which loads the welcome.html page.
Clicking Start: You’re redirected to the homepage (/home), which loads home.html to show the available categories.
Selecting a Category: When you click a category, it calls the category route (/category/<category_name>) and loads category.html with a randomly generated question.
Answer Submission: When you submit an answer, the app checks if it’s correct and gives feedback.
Editing Tips for Beginners
Experiment with HTML: Start by changing some text or images and see how it affects the page. HTML is forgiving and easy to learn.
Use a CSS Color Picker: If you want to change colors, search for an online color picker tool.
Adding Problems: You can expand the problem sets by copying the existing problems and modifying the values or text.
Read the Code Comments: I’ve added comments to help you understand what each part of the code does.
By following these steps and understanding each file's purpose, you should be able to confidently edit and expand this project! If you have more questions or need further explanations, feel free to ask.
