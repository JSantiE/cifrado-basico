from flask import Flask, render_template, request, url_for, redirect, jsonify, make_response

app = Flask(__name__)

abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "0123456789"

@app.route("/")
def index():
    
    data = {
        "title": "Index",
        "abecedarioBase": abecedario,
        "message": "Cifrado de datos - Trasposición de columnas",
    }
    
    return render_template("index.html", data=data)

@app.route("/generar", methods=["POST"])
def generar():
    req = request.get_json()    
    abecedario_generado = abecedario
    
    #Obtener los datos del formulario
    cantidad_letras = int(req.get("cantidad_letras"))    
    alfanumerico = req.get("alfanumerico")
    inverso = req.get("inverso")
    letraInicial = req.get("letraInicial")
    palabraClave = req.get("palabraClave")
    
    #Generar abecedario con 27 letras si se selecciona la opción correspondiente
    if cantidad_letras == 27:
        abecedario_generado = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    
    #Agregar números al abecedario si se selecciona la opción correspondiente
    if alfanumerico == True:
        abecedario_generado += numeros
    
    #Invertir el abecedario si se selecciona la opción correspondiente
    if inverso == True:
        abecedario_generado = abecedario_generado[::-1]
    
    #Mover la letra inicial al inicio del abecedario si se proporciona una letra inicial
    if letraInicial != "":
        letraInicial = letraInicial.upper()
        if letraInicial in abecedario_generado:
            index = abecedario_generado.index(letraInicial)
            abecedario_generado = abecedario_generado[index:] + abecedario_generado[:index]
    
    #Agregar la palabra clave al inicio del abecedario si se proporciona una palabra clave
    if palabraClave != "":
        palabraClave = palabraClave.upper()
        palabraClave = "".join(sorted(set(palabraClave), key=palabraClave.index))
        abecedario_generado = "".join([letra for letra in abecedario_generado if letra not in palabraClave])
        abecedario_generado = palabraClave + abecedario_generado
    
    print("Datos recibidos:", abecedario_generado)
    
    res = make_response(jsonify({"abecedario_generado": list(abecedario_generado)}), 200)
    
    return res

def pagina_no_encontrada(error):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True)