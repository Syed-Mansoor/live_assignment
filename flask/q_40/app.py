# 40.Explain how to set up a Flask application to handle form submissions using POST requests.
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle form submission
        name = request.form['name']
        email = request.form['email']
        # Process the data (e.g., save to database, perform calculations, etc.)
        return redirect(url_for('thank_you'))

    return render_template('form.html')

@app.route('/thank_you')
def thank_you():
    return "Thank you for submitting the form!"

if __name__ == '__main__':
    app.run(debug=True)
