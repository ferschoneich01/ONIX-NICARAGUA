from cs50 import SQL
from flask import Flask, render_template, flash, redirect, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash
from funciones import login_required

app = Flask(__name__)

app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///Data.db")

#ruta principal
@app.route("/")
def home():
    rows=db.execute("select * from vista")
    return render_template("Principal.html",vista=rows)

#ruta login
@app.route("/login", methods=["GET", "POST"])
def login():
    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            flash("must provide username")

        # Ensure password was submitted
        elif not request.form.get("password"):
            flash("must provide password")

        # Query database for username
        rows = db.execute("SELECT * FROM Users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["password"], request.form.get("password")):
            flash("invalid username and/or password")

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    else:
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
    if request.method == "POST":
        category = request.form.get("category")

        if category == "Parejas":
            db.execute("Insert into vista(id,nombre,foto,descripcion,precio) values(NULL,:nombre,:foto,:descripcion,:precio)"
            ,nombre=request.form["nombre"],foto=request.form["foto"],descripcion=request.form["descripcion"],precio=request.form["precio"])

        elif category == "Caballeros":
            db.execute("Insert into caballero(id,nombre,foto,descripcion,precio) values(NULL,:nombre,:foto,:descripcion,:precio)"
            ,nombre=request.form["nombre"],foto=request.form["foto"],descripcion=request.form["descripcion"],precio=request.form["precio"])

        elif category == "Damas":
            db.execute("Insert into damas(id,nombre,foto,descripcion,precio) values(NULL,:nombre,:foto,:descripcion,:precio)"
            ,nombre=request.form["nombre"],foto=request.form["foto"],descripcion=request.form["descripcion"],precio=request.form["precio"])

        elif category == "Otros":
            db.execute("Insert into otros(id,nombre,foto,descripcion,precio) values(NULL,:nombre,:foto,:descripcion,:precio)"
            ,nombre=request.form["nombre"],foto=request.form["foto"],descripcion=request.form["descripcion"],precio=request.form["precio"])

    else:
        return render_template("Admin.html")

# Ruta para crear pulseras personalizadas
@app.route("/personalizada",methods=["GET", "POST"])
@login_required
def personalizada():
    return render_template("Create.html")

@app.route("/buy",methods=["GET", "POST"])
@login_required
def buy():
    rows=db.execute("select * from vista")
    filas=db.execute("select * from caballero")
    casillas=db.execute("select * from damas")
    celdas=db.execute("select * from otros")
    return render_template("buy.html",vista=rows,caballero=filas,damas=casillas,otros=celdas)

@app.route("/compras",methods=["GET", "POST"])
@login_required
def compras():
    return render_template("compras.html")

# Cerrar sesion
@app.route("/logout")
def logout():
    # Forget any user_id
    session.clear()
    # Redirect user to login form
    return redirect("/")

@app.route("/eliminar/<descripcion>",methods=["GET","POST"])
def eliminar(descripcion):

    db.execute("DELETE FROM vista WHERE descripcion = :desc",
                    desc = descripcion)
    return redirect("/")


#funcion principal
if __name__ == '__main__':
    app.run(debug=True)