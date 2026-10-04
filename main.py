# Import
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

# Página de contenidos en ejecución
@app.route('/')
def index():
    return render_template('index.html')


# Habilidades dinámicas
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    return render_template('index.html', button_python=button_python)

@app.route('/feedback', methods=['POST'])
def process_feedback():
    email = request.form.get('email')
    comment = request.form.get('text')
    return render_template('index.html', email=email, comment=comment)

if __name__ == "__main__":
    app.run(debug=True)
