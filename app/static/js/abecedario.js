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
        mostrarMensajeSinResultado("tituloAbecedario", "No se generó ningún abecedario");
        return;
    }

    renderizarTabla("filaAbecedario", "tituloAbecedario", "ABECEDARIO GENERADO", abecedarioBase);
    
    document.getElementById("tablaAbecedario").style.display = "table";
    document.getElementById("divVariables").style.display = "flex";
}