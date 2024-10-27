from flask import Flask, render_template, request, redirect, url_for, flash
import random

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Step 1: Define a database of word problems with categories, random number ranges, and units
word_problems = {
    "travel": [
        {
            "problem": "If a car travels at {speed} km/h for {time} hours, how far does it travel?",
            "variables": {"speed": (20, 100), "time": (1, 10)},
            "formula": lambda speed, time: speed * time,
            "units": "km"
        },
        {
            "problem": "A train moves at {speed} km/h for {hours} hours. How far does it travel?",
            "variables": {"speed": (30, 150), "hours": (1, 8)},
            "formula": lambda speed, hours: speed * hours,
            "units": "km"
        }
    ],
    "geometry": [
        {
            "problem": "A rectangle has a width of {width} units and a length of {length} units. What is its area?",
            "variables": {"width": (1, 20), "length": (5, 50)},
            "formula": lambda width, length: width * length,
            "units": "square units"
        },
        {
            "problem": "A circle has a radius of {radius} units. What is its circumference?",
            "variables": {"radius": (1, 15)},
            "formula": lambda radius: 2 * 3.14 * radius,
            "units": "units"
        }
    ],
    "shopping": [
        {
            "problem": "If you buy {apples} apples for ${price_per_apple} each, how much will you pay in total?",
            "variables": {"apples": (1, 20), "price_per_apple": (0.5, 3.0)},
            "formula": lambda apples, price_per_apple: apples * price_per_apple,
            "units": "dollars"
        },
        {
            "problem": "You buy {items} items at ${price_per_item} each. What is the total cost?",
            "variables": {"items": (2, 10), "price_per_item": (1.0, 5.0)},
            "formula": lambda items, price_per_item: items * price_per_item,
            "units": "dollars"
        }
    ]
}

def generate_random_problem(category):
    """Generates a random problem with randomized values based on the selected category."""
    if category not in word_problems:
        return None, None, None

    # Choose a random problem from the category
    problem = random.choice(word_problems[category])
    
    # Generate random values for variables in the problem
    random_values = {
        var: round(random.uniform(*range_vals), 2) if isinstance(range_vals[0], float) 
        else random.randint(*range_vals)
        for var, range_vals in problem["variables"].items()
    }

    # Create the problem statement with randomized values
    problem_text = problem["problem"].format(**random_values)
    
    # Calculate the correct answer using the formula with the generated values
    correct_answer = problem["formula"](**random_values)
    
    # Get the units for the answer
    units = problem["units"]
    
    return problem_text, correct_answer, units

@app.route('/')
def welcome():
    return render_template("welcome.html")

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/category/<string:category>')
def category(category):
    problem_text, correct_answer, units = generate_random_problem(category)
    if problem_text is None:
        flash("Invalid category selected.", "danger")
        return redirect(url_for('home'))
    return render_template("category.html", problem=problem_text, correct_answer=correct_answer, category=category, units=units)

@app.route('/check/<string:category>', methods=['POST'])
def check(category):
    user_answer = request.form['answer']
    correct_answer = float(request.form['correct_answer'])
    try:
        user_answer = float(user_answer)
        if abs(user_answer - correct_answer) < 0.01:
            flash("Correct!", "success")
        else:
            flash(f"Incorrect. The correct answer was {correct_answer:.2f}", "danger")
    except ValueError:
        flash("Invalid input. Please enter a valid number.", "danger")
    return redirect(url_for('category', category=category))

if __name__ == "__main__":
    app.run(debug=True)
