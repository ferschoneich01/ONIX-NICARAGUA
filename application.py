from cs50 import SQL
from flask import Flask, render_template, flash, redirect, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///Data.db")

#ruta principal
@app.route("/")
def home():
    return render_template('Principal.html')

#ruta login
@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")

# ruta register
@app.route("/register", methods=["POST", "GET"])
def register():
    # si el usuario alcanzó la ruta a través de POST
    if request.method == "POST":
        if not request.form.get("username"):
            flash("ingrese un usuario")
            return render_template("register.html")

        elif not request.form.get("password"):
            flash("ingrese la contraseña")
            return render_template("register.html")

        elif not request.form.get("vpass"):
            flash("las contraseñas no coinciden :(")
            return render_template("register.html")

        elif request.form.get("password") != request.form.get("vpass"):
            flash("las contraseñas no coinciden :(")
            return render_template("register.html")

        response = db.execute("INSERT INTO Users (username, password) \
                            VALUES(:username, :password)",
                            username = request.form.get("username"),
                            password = generate_password_hash(request.form.get("password")))

        if not response:
            flash("el usuario ya existe :(")
            return render_template("register.html")

        rows = db.execute("SELECT * FROM users WHERE username = :username", username = request.form.get("username"))

        session["user_id"] = rows[0]["id"]

        return redirect("/")

    else:
        return render_template("register.html")

# Ruta para el admin de la pagina
@app.route("/Admin", methods=["POST", "GET"])
def Admin():
    return render_template("Admin.html")

if __name__ == '__main__':
    app.run(debug=True)