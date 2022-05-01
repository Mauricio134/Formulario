from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/formulario", methods=["POST"])
def formu():
    error = False
    errorMessage = ""
    return render_template("formu.html", error = error, errorMessage = errorMessage)

@app.route("/user", methods=["POST"])
def register():
    name = request.form.get("name")
    surname = request.form.get("surname")
    date = request.form.get("born")
    cell = request.form.get("cell")
    dni = request.form.get("dni")
    gmail = request.form.get("email")
    passw = request.form.get("password")
    pass_confirm = request.form.get("password_confirm")
    if name == "" and surname == "" and date == "" and dni == "" and cell == "" and gmail == "" and passw == "" and pass_confirm == "":
        error = True
        errorMessage = "Todos los campos están vacíos..."
        return render_template("formu.html", error = error, errorMessage = errorMessage)
    elif name == "":
        error = True
        errorMessage = "Confirma bien tus nombres..."
        return render_template("formu.html", error = error, errorMessage = errorMessage)
    elif surname == "":
        error = True
        errorMessage = "Confirma bien tus apellidos..."
        return render_template("formu.html", error = error, errorMessage = errorMessage)
    elif date == "":
        error = True
        errorMessage = "Confirma bien tu fecha de nacimiento..."
        return render_template("formu.html", error = error, errorMessage = errorMessage)
    elif dni == "":
        error = True
        errorMessage = "Confirma bien tu dni..."
        return render_template("formu.html", error = error, errorMessage = errorMessage)
    elif cell == "":
        error = True
        errorMessage = "Confirma bien tu celular..."
        return render_template("formu.html", error = error, errorMessage = errorMessage)
    elif gmail == "":
        error = True
        errorMessage = "Confirma bien tu email..."
        return render_template("formu.html", error = error, errorMessage = errorMessage)

        
    if passw == pass_confirm:
        return render_template("result.html", name = name, surname = surname, date = date, cell = cell, dni = dni, gmail = gmail, passw = passw)
    else:
        error = True
        errorMessage = "Confirma bien tu contraseña..."
        return render_template("formu.html", error = error, errorMessage = errorMessage)