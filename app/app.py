from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    
    abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    numeros = "0123456789"
    
    data = {
        "title": "Index",
        "abecedarioBase": abecedario,
        "abecedarioGenerado": numeros,
        "message": "Cifrado de datos - Trasposición de columnas",
    }
    
    return render_template("index.html", data=data)

@app.route("/generar", methods=["POST"])
def generar():
    print("Generando cifrado...")
    return {"mensaje": "Cifrado generado"}

if __name__ == "__main__":
    app.run(debug=True)