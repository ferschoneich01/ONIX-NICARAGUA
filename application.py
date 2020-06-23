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

def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code

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
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Query database for username
        rows = db.execute("SELECT * FROM Users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["password"], request.form.get("password")):
            return apology("invalid username and/or password", 400)



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
            return apology("Ingrese un usuario", 400)

        elif not request.form.get("correo") and not request.form.get("cel"):
            return apology("Ingrese correo y/o cel", 400)

        elif not request.form.get("direccion"):
            return apology("Ingrese direccion", 400)

        elif not request.form.get("password"):
            return apology("ingrese la contraseña", 400)

        elif not request.form.get("vpass"):
            return apology("Ingrese la confirmación de contraseña")

        elif request.form.get("password") != request.form.get("vpass"):
            return apology("Las contraseña y la confimarción no coinciden :(", 400)

        response = db.execute("INSERT INTO Users (username, correo, cel, direccion, password) \
                            VALUES(:username, :correo, :cel, :direccion, :password)",
                            username = request.form.get("username"),
                            correo = request.form.get("correo"),
                            cel = request.form.get("cel"),
                            direccion = request.form.get("direccion"),
                            password = generate_password_hash(request.form.get("password")))

        if not response:
            return apology("el usuario ya existe :(", 400)

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
            return redirect("/")

        elif category == "Caballeros":
            db.execute("Insert into caballero(id,nombre,foto,descripcion,precio) values(NULL,:nombre,:foto,:descripcion,:precio)"
            ,nombre=request.form["nombre"],foto=request.form["foto"],descripcion=request.form["descripcion"],precio=request.form["precio"])
            return redirect("/")

        elif category == "Damas":
            db.execute("Insert into damas(id,nombre,foto,descripcion,precio) values(NULL,:nombre,:foto,:descripcion,:precio)"
            ,nombre=request.form["nombre"],foto=request.form["foto"],descripcion=request.form["descripcion"],precio=request.form["precio"])
            return redirect("/")

        elif category == "Otros":
            db.execute("Insert into otros(id,nombre,foto,descripcion,precio) values(NULL,:nombre,:foto,:descripcion,:precio)"
            ,nombre=request.form["nombre"],foto=request.form["foto"],descripcion=request.form["descripcion"],precio=request.form["precio"])
            return redirect("/")
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
    if request.method == "POST":
        nom = request.form.get("nombre")
        dir = "Managua"
        desc = request.form.get("descripcion")
        prec = request.form.get("precio")
        cant = request.form.get("cantidad")

        db.execute("Insert into Pulseras(nombre,descripcion,direccion,precio,cantidad) values(:nombre,:descripcion, :direccion,:precio, :cantidad)",
        nombre=nom, descripcion = desc,direccion=dir,precio=prec,cantidad=cant)

        return redirect("/compras")
    else:
        rows=db.execute("select * from vista")
        filas=db.execute("select * from caballero")
        casillas=db.execute("select * from damas")
        celdas=db.execute("select * from otros")

        return render_template("buy.html",vista=rows,caballero=filas,damas=casillas,otros=celdas)

@app.route("/compras",methods=["GET", "POST"])
@login_required
def compras():
    rows=db.execute("select * from Pulseras")
    return render_template("compras.html",Pulseras=rows)

@app.route("/perfil", methods=["GET", "POST"])
@login_required
def perfil():

    return render_template("perfil.html")

@app.route("/contraseña", methods=["GET", "POST"])
@login_required
def contraseña():
    if request.method == "POST":

        rows = db.execute("SELECT password FROM Users WHERE id = :user_id", user_id=session["user_id"])

        if not request.form.get("newPass"):
            return apology("must provide new password", 400)

        elif not request.form.get("confimPass"):
            return apology("must provide new password confirmation", 400)

        elif request.form.get("newPass") != request.form.get("confimPass"):
            return apology("new password and confirmation must match", 400)

        password = request.form.get("newPass")
        rows = db.execute("UPDATE Users SET password = :password WHERE id = :user_id", user_id=session["user_id"], password=password)


    return render_template("contraseña.html")




@app.route("/telefono", methods=["GET", "POST"])
@login_required
def telefono():

    if request.method == "POST":

        rows = db.execute("SELECT cel FROM Users WHERE id = :user_id", user_id=session["user_id"])

        if not request.form.get("newCel"):
            return apology("must provide new Cellphone", 400)

        elif not request.form.get("confimCel"):
            return apology("must provide new Cellphone confirmation", 400)

        elif request.form.get("newCel") != request.form.get("confimCel"):
            return apology("new cellphone and confirmation must match", 400)

        cel = request.form.get("newCel")
        rows = db.execute("UPDATE Users SET cel = :cel WHERE id = :user_id", user_id=session["user_id"], cel=cel)

    return render_template("telefono.html")

@app.route("/correo", methods=["GET", "POST"])
@login_required
def correo():

    if request.method == "POST":

        rows = db.execute("SELECT correo FROM Users WHERE id = :user_id", user_id=session["user_id"])

        if not request.form.get("newCorreo"):
            return apology("must provide new Email", 400)

        elif not request.form.get("confimCorreo"):
            return apology("must provide new Email confirmation", 400)

        elif request.form.get("newCorreo") != request.form.get("confimCorreo"):
            return apology("new email and confirmation must match", 400)

        correo = request.form.get("newCorreo")
        rows = db.execute("UPDATE Users SET  correo = :correo WHERE id = :user_id", user_id=session["user_id"], correo=correo)

    return render_template("correo.html")

@app.route("/direccion", methods=["GET", "POST"])
@login_required
def direccion():

    if request.method == "POST":

        rows = db.execute("SELECT direccion FROM Users WHERE id = :user_id", user_id=session["user_id"])

        if not request.form.get("newDir"):
            return apology("must provide new Address", 400)

        elif not request.form.get("confimDir"):
            return apology("must provide new Address confirmation", 400)

        elif request.form.get("newDir") != request.form.get("confimDir"):
            return apology("new Address and confirmation must match", 400)

        direccion = request.form.get("newDir")
        rows = db.execute("UPDATE Users SET  direccion = :direccion WHERE id = :user_id", user_id=session["user_id"], direccion=direccion)

    return render_template("direccion.html")

# Cerrar sesion
@app.route("/logout")
def logout():
    # Forget any user_id
    session.clear()
    # Redirect user to login form
    return redirect("/")

@app.route("/eliminar/<nombre>")
def eliminar(nombre):

    db.execute("DELETE FROM vista WHERE nombre = :name",
    name = nombre)

    db.execute("DELETE FROM caballero WHERE nombre = :name",
    name = nombre)

    db.execute("DELETE FROM damas WHERE nombre = :name",
    name = nombre)

    db.execute("DELETE FROM otros WHERE nombre = :name",
    name = nombre)

    return redirect("/")

#funcion principal
if __name__ == '__main__':
    app.run(debug=True)
