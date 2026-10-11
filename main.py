# Import
from flask import Flask, render_template,request, redirect  
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Creando la DB
db = SQLAlchemy(app)

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    comment = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f'<Feedback {self.email}>'

# Página de contenidos en ejecución
@app.route('/')
def index():
    return render_template('index.html')


# Habilidades dinámicas
@app.route('/python', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    return render_template('index.html', button_python=button_python)

@app.route('/discord', methods=['POST'])
def process():
    button_discord = request.form.get('button_discord')
    return render_template('index.html', button_discord=button_discord)

@app.route('/html', methods=['POST'])
def form():
    button_html = request.form.get('button_html')
    return render_template('index.html', button_html=button_html)

@app.route('/db', methods=['POST'])
def pf():
    button_db = request.form.get('button_db')
    return render_template('index.html', button_db=button_db)

@app.route('/feedback', methods=['POST'])
def process_feedback():
    email = request.form.get('email')
    comment = request.form.get('comment')

    if email and comment:
        feedback = Feedback(email=email, comment=comment)
        db.session.add(feedback)
        db.session.commit()
        return redirect('/')
    else:
        return "Por favor, completa todos los campos del formulario."


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)
