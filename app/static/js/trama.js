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
        trama: document.getElementById("txtTrama").value,
        abecedario: abecedarioBase
    };        
}

function procesarTrama(data) {

    if (data.abecedario_generado.length === 0) {
        mostrarMensajeSinResultado("tituloTablaTrama", "No se generó ningún abecedario");
        return;
    }

    renderizarTabla("filaTablaTrama", "tituloTablaTrama", "ABECEDARIO TRAMA GENERADO", data.abecedario_generado);
    actualizarTablaExplicativa(data.abecedario_explicativo);

    document.getElementById("tablaTrama").style.display = "table";
}