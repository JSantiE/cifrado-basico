/* =========================================================
    GENERAR ABECEDARIO
========================================================= */

function generar(){
    const datos = obtenerDatosFormulario();

    enviarPost("/generar", datos)
        .then(data => {
            procesarResultado(data);
        })
        .catch(error => {
            mostrarError("Error al generar el abecedario.", error);
        });
}

function obtenerDatosFormulario(){
    return {
        letraInicial: document.getElementById("txtLetraInicial").value,
        palabraClave: document.getElementById("txtPalabraClave").value,
        inverso: document.getElementById("chkInverso").checked,
        alfanumerico: document.getElementById("chkAlfanumerico").checked,
        cantidad_letras: document.getElementById("rdAbecedario27").checked
            ? 27
            : 26
    }
}

function procesarResultado(data){
    abecedarioBase = data.abecedario_generado;

    if (abecedarioBase.length === 0) {
        mostrarMensajeSinResultado("tituloTabla", "No se generó ningún abecedario");
        return;
    }

    renderizarTabla("filaAbecedario", "tituloTabla", "ABECEDARIO GENERADO", abecedarioBase);
    
    document.getElementById("tablaGenerada").style.display = "table";
    document.getElementById("divVariables").style.display = "inline";
}