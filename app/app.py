from flask import Flask, render_template, request, url_for, redirect, jsonify, make_response
from funciones_cifrado import(
    generar_abecedario,
    generar_tabla_trasposicion,
    generar_tabla_trasposicion_explicativa,
    generar_tabla_trama,
    generar_tabla_trama_ordenada,
    generar_tabla_clave_numerica,
    generar_tabla_clave_numerica_ordenada    
)

app = Flask(__name__)

@app.route("/")
def index():
    
    data = {
        "title": "Index",
        "abecedarioBase": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "message": "Cifrado de datos - Trasposición y Trama de columnas",
    }
    
    return render_template("index.html", data=data)

@app.route("/generar", methods=["POST"])
def generar():
    req = request.get_json()    
    
    cantidad_letras = int(req.get("cantidad_letras"))    
    alfanumerico = req.get("alfanumerico")
    inverso = req.get("inverso")
    letraInicial = req.get("letraInicial")
    palabraClave = req.get("palabraClave")
    
    abecedario_generado = generar_abecedario(cantidad_letras, alfanumerico, inverso, letraInicial, palabraClave)
    
    res = make_response(jsonify({"abecedario_generado": list(abecedario_generado)}), 200)
    return res

@app.route("/generarTrasposicion", methods=["POST"])
def generarTrasposicion():
    req = request.get_json()
    
    trasposicion = req.get("trasposicion")
    abecedario = list(req.get("abecedario"))
    
    tblTrasposicion = generar_tabla_trasposicion(abecedario, trasposicion)
    tblAbecedario = generar_tabla_trasposicion_explicativa(abecedario, trasposicion)
    
    res = make_response(jsonify({"abecedario_generado": list(tblTrasposicion), "abecedario_explicativo": list(tblAbecedario)}), 200)
    return res

@app.route("/generarTrama", methods=["POST"])
def generarTrama():
    req = request.get_json()
    
    trama = req.get("trama")
    abecedario = list(req.get("abecedario"))
    
    tblAbecedario = generar_tabla_trama(abecedario, trama)
    tblTrama = generar_tabla_trama_ordenada(tblAbecedario, trama)

    res = make_response(jsonify({"abecedario_generado": [fila["trama"] for fila in tblTrama], "abecedario_explicativo": list(tblAbecedario)}), 200)    
    return res

@app.route("/generarClaveNumerica", methods=["POST"])
def generarClaveNumerica():
    req = request.get_json()
    
    claveNumerica = req.get("claveNumerica")
    abecedario = list(req.get("abecedario"))
    
    columnas = list(claveNumerica)
    
    tblAbecedario = generar_tabla_clave_numerica(abecedario, columnas)
    tblClaveNumerica = generar_tabla_clave_numerica_ordenada(tblAbecedario, columnas)

    res = make_response(jsonify({"abecedario_generado": list(tblClaveNumerica), "abecedario_explicativo": list(tblAbecedario), "columnas": columnas}), 200)
    return res

@app.route("/generarEncriptacion", methods=["POST"])
def generarEncriptacion():
    req = request.get_json()
    
    cadena = req.get("cadena")
    abecedario = list(req.get("abecedario"))
    abecedarioGenerado = list(req.get("abecedarioGenerado"))
    estado = req.get("estado")
    n = 0
    res = ""
    cadena = cadena.upper()
 
    if estado :
        for i,letra in enumerate(cadena):
            if letra == " ":
                n += 1
                res += " "
                continue
            
            posicion = abecedario.index(letra)
            x = posicion + (i + 1 -n)
            x = (x - 1) % len(abecedarioGenerado)            
            res += abecedarioGenerado[x]
    else:
        for i,letra in enumerate(cadena):
            if letra == " ":
                n += 1
                res += " "
                continue
            
            posicion = abecedarioGenerado.index(letra)
            x = posicion - (i + 1 -n)            
            res += abecedario[x + 1]
                
    return make_response(jsonify({"cadena" : res}), 200);

def pagina_no_encontrada(error):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True)