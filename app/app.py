from flask import Flask, render_template, request, url_for, redirect, jsonify, make_response

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
    tblAbecedario = generar_tabla_explicativa(abecedario, trasposicion)
    
    res = make_response(jsonify({"abecedario_generado": list(tblTrasposicion), "abecedario_explicativo": list(tblAbecedario)}), 200)
    return res

@app.route("/generarTrama", methods=["POST"])
def generarTrama():
    req = request.get_json()
    
    trama = req.get("trama")
    abecedario = list(req.get("abecedario"))
    
    tblAbecedario = generar_tabla_trama(abecedario, trama)
    tblTrama = generar_tabla_trama_ordenada(tblAbecedario, trama)

    res = make_response(jsonify({"abecedario_generado": list(tblTrama), "abecedario_explicativo": list(tblAbecedario)}), 200)    
    return res

@app.route("/generarClaveNumerica", methods=["POST"])
def generarClaveNumerica():
    req = request.get_json()
    
    claveNumerica = req.get("claveNumerica")
    abecedario = list(req.get("abecedario"))
    
    columnas = list(claveNumerica)
    
    tblAbecedario = []
    
    for i in range(0, len(abecedario), len(columnas)):
        fila = []

        for j in range(len(columnas)):
            posicion = i + j

            if posicion < len(abecedario):
                fila.append(abecedario[posicion])
            else:
                fila.append("")

        tblAbecedario.append(fila)
    
    tblClaveNumerica = []

    for numero in sorted(columnas, key=int):

        indice_columna = columnas.index(numero)

        for fila in tblAbecedario:

            if fila[indice_columna] != "":
                tblClaveNumerica.append(fila[indice_columna])


    res = make_response(jsonify({"abecedario_generado": list(tblClaveNumerica), "abecedario_explicativo": list(tblAbecedario), "columnas": columnas}), 200)
    return res

def generar_abecedario(cantidad_letras, alfanumerico, inverso, letraInicial, palabraClave):
    abecedario_generado = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    if cantidad_letras == 27:
        abecedario_generado = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    
    if alfanumerico == True:
        abecedario_generado += "0123456789"
    
    if inverso == True:
        abecedario_generado = abecedario_generado[::-1]
    
    if letraInicial:
        abecedario_generado = mover_letra_inicial(abecedario_generado, letraInicial)
        
    if palabraClave:
        abecedario_generado = aplicar_palabra_clave(abecedario_generado, palabraClave)
    
    return abecedario_generado

def mover_letra_inicial(abecedario_generado, letraInicial):
    letraInicial = letraInicial.upper()
    
    if letraInicial in abecedario_generado:
        index = abecedario_generado.index(letraInicial)
        abecedario_generado = abecedario_generado[index:] + abecedario_generado[:index]
    
    return abecedario_generado

def aplicar_palabra_clave(abecedario_generado, palabraClave):
    palabraClave = palabraClave.upper() 
    
    palabraClave = "".join(sorted(set(palabraClave), key=palabraClave.index)) #Quitar letras repetidas
    abecedario_generado = "".join([letra for letra in abecedario_generado if letra not in palabraClave]) #Quitar letras de la palabra clave del abecedario
    
    return palabraClave + abecedario_generado

def generar_tabla_trasposicion(abecedario, trasposicion):
    
    tabla = []
    tamaño = len(trasposicion)
    
    for i in range(0, len(abecedario), tamaño):
        bloque = abecedario[i:i+tamaño]#separa el abecedario en bloques del tamaño de la trasposición
        
        fila = [
            letra for _, letra in sorted(zip(trasposicion, bloque), key=lambda x: int(x[0]))#ordenar el bloque según la trasposición
        ]
        
        tabla.extend(fila)
    
    return tabla

def generar_tabla_explicativa(abecedario, trasposicion):
    tabla = []
    
    for i, letra in enumerate(abecedario):
        tabla.append({
            "id": trasposicion[i%len(trasposicion)],
            "letra": letra
            })
    
    return tabla

def generar_tabla_trama(abecedario, trama):
    cadena = sorted(trama)
    tabla = []
    n = 0
    
    for i, letra in enumerate(abecedario, start=1):
        id_trama = 100 if n == len(cadena) else int(cadena[n])
                
        tabla.append({
            "id": id_trama,
            "trama": letra
        })
        
        if i % (len(abecedario) // len(trama)) == 0:
            n += 1
    
    return tabla

def generar_tabla_trama_ordenada(tabla, trama):
    orden = {
        int(valor): posicion
        for posicion, valor in enumerate(trama)
    }
    
    tabla_ordenada = sorted(
        tabla,
        key=lambda fila: orden.get(fila["id"], 100)
    )
    
    return tabla_ordenada

def pagina_no_encontrada(error):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True)