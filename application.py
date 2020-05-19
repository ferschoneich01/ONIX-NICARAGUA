from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('Principal.html')

@app.route('/sing_up')
def sing_up():
    return render_template('sing_up.html')

@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)