/* =========================================================
    GENERAR TRAMA
========================================================= */

function generarTrama(){
    const datos = obtenerDatosTrama();

    enviarPost("/generarTrama", datos)
        .then(data => {
            procesarTrama(data);
        })
        .catch(error => {
            mostrarError("Error al generar la trama.", error);
        });
}

function obtenerDatosTrama(){
    return {
        trama: document.getElementById("txtCifrado").value,
        abecedario: abecedarioBase
    };        
}

function procesarTrama(data) {
    abecedarioGenerado = data.abecedario_generado;

    if (data.abecedario_generado.length === 0) {
        mostrarMensajeSinResultado("tituloTablaGenerada", "No se generó ningún abecedario");
        return;
    }

    renderizarTabla("filaTablaGenerada", "tituloTablaGenerada", "ABECEDARIO TRAMA GENERADO", data.abecedario_generado);
    actualizarTablaExplicativa(data.abecedario_explicativo);

    document.getElementById("tablaGenerada").style.display = "table";
    document.getElementById("tablaClaveNumericaExplicativa").style.display = "none";
}