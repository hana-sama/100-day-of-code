from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from send_email import TelegramBot
app = Flask(__name__)
app.config["SECRET_KEY"] = "myapplication123"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
 
db = SQLAlchemy(app)
 
class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    date = db.Column(db.Date)
    occupation = db.Column(db.String(80))

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        first_name = request.form['first_name'].capitalize()
        last_name = request.form['last_name'].capitalize()
        email = request.form['email']
        date = request.form['date']
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        status = request.form['occupation'].capitalize()
        print(first_name, last_name, email, date, status)

        form = Form(first_name=first_name, last_name=last_name, email=email, date=date_obj, occupation=status)

        db.session.add(form)
        db.session.commit()
        bot = TelegramBot()
        bot.send(f'We hereby confirm that we have received an application from {first_name} {last_name} for jobs that will become available on {date}')
        return redirect(url_for("success" if form else "error"))
    
    return render_template("index.html")

@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/error")
def error():
    return render_template("error.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5001)