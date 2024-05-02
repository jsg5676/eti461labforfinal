from flask import Flask, render_template, request, redirect
import MySQLdb

app = Flask(__name__)
app.config["DEBUG"] = True

conn = MySQLdb.connect(
    host="jsg56762.mysql.pythonanywhere-services.com",
    user="jsg56762",
    passwd="examplepass",
    db="jsg56762$default"
)
cursor = conn.cursor()

@app.route('/')
def index():

    return render_template('homeex.html')

@app.route('/display', methods=['GET', 'POST'])
def display():
    if request.method == 'POST':
        # Get the new category from the form
        new_category = request.form['category']

        # Insert the new category into the database
        cursor.execute("INSERT INTO Category (category) VALUES (%s)", (new_category,))

        # Redirect back to the display page to prevent form resubmission on refresh
        return redirect('/display')

    else:
        # Execute the query to fetch existing categories
        cursor.execute("""
            SELECT category_id, category
            FROM Category;
        """)

        # Fetch the results
        data = cursor.fetchall()

        # Return the template with the table data
        return render_template('display.html', data=data)