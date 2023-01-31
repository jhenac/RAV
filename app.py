from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = "rav secret"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/rav'
app.config['SQLALCHEMY TRACK MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Data(db.Model):
    discipline = db.Column(db.String(100), primary_key = True)
    pay = db.Column(db.Integer)
    category = db.Column(db.String(100))
    gg_score = db.Column(db.Integer)
    group = db.Column(db.String(100))
    cmi = db.Column(db.Integer)


    def __init__(self, discipline, pay, category, gg_score, group, cmi):
        self.discipline = discipline
        self.pay = pay
        self.category = category
        self.gg_score = gg_score
        self.group = group
        self.cmi = cmi


@app.route('/')
def home():
    return render_template("index.html")

# @app.route('/insert', methods=['POST'])
# def insert():
#
#     if request.method == 'POST':
#
#         discipline = request.form['/html/body/div/div/div/div/div[3]/div[2]/table/tbody/tr[1]/th']


if __name__ == "__main__":
    app.run(debug=True)