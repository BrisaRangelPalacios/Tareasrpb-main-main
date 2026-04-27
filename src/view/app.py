from flask import Flask, render_template_string, request

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
    <style>
        body {
            font-family: Arial;
            background: #f8bbd0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .box {
            background: white;
            padding: 30px;
            border-radius: 10px;
            width: 300px;
            text-align: center;
        }
        input {
            width: 90%;
            padding: 10px;
            margin: 10px;
        }
        button {
            padding: 10px;
            background: pink;
            border: none;
            color: white;
            width: 100%;
        }
    </style>
</head>
<body>
    <div class="box">
        <h2>Iniciar Sesión</h2>
        <form method="post">
            <input name="correo" placeholder="Correo"><br>
            <input name="password" type="password" placeholder="Contraseña"><br>
            <button>Ingresar</button>
        </form>
        <p>{{mensaje}}</p>
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET","POST"])
def login():
    mensaje = ""
    if request.method == "POST":
        if request.form["correo"] == "admin" and request.form["password"] == "1234":
            mensaje = "Login correcto"
        else:
            mensaje = "Datos incorrectos"
    return render_template_string(html, mensaje=mensaje)

app.run(port=5000)