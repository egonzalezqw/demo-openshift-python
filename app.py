from flask import Flask, request, jsonify, render_template_string
from datetime import datetime

app = Flask(__name__)

counter = 0

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>OpenShift Demo App</title>
</head>
<body>
    <h1>🚀 Demo OpenShift Interactivo</h1>

    <form action="/greet" method="get">
        <input type="text" name="name" placeholder="Escribe tu nombre">
        <button type="submit">Saludar</button>
    </form>

    <br>

    <form action="/increment" method="post">
        <button type="submit">Incrementar contador</button>
    </form>

    <p>Contador actual: {{counter}}</p>

    <p><a href="/health">Health Check</a></p>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_PAGE, counter=counter)

@app.route("/greet")
def greet():
    name = request.args.get("name", "amigo")
    return f"👋 Hola {name}, bienvenido a OpenShift!"

@app.route("/increment", methods=["POST"])
def increment():
    global counter
    counter += 1
    return f"🔢 Contador actualizado: {counter}"

@app.route("/api/info")
def api_info():
    return jsonify({
        "app": "OpenShift Interactive Demo",
        "time": datetime.now().isoformat(),
        "counter": counter
    })

@app.route("/health")
def health():
    return jsonify({"status": "UP"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
