# Import
from flask import Flask, render_template,request, redirect  



app = Flask(__name__)

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
    comment = request.form.get('text')
    return render_template('index.html', email=email, comment=comment)

if __name__ == "__main__":
    app.run(debug=True)
