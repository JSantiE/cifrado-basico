/* =========================================================
    GENERAR TRASPOSICION
========================================================= */

function generarTrasposicion(){
    const datos = obtenerDatosTrasposicion();

    enviarPost("/generarTrasposicion", datos)
        .then(data => {
            procesarTrasposicion(data);
        })
        .catch(error => {
            mostrarError("Error al generar la trasposición.", error);
        });
}

function obtenerDatosTrasposicion(){
    return {
        trasposicion: document.getElementById("txtCifrado").value,
        abecedario: abecedarioBase
    };        
}

function procesarTrasposicion(data) {

    if (data.abecedario_generado.length === 0) {
        mostrarMensajeSinResultado("tituloTablaGenerada", "No se generó ningún abecedario");
        return;
    }

    renderizarTabla("filaTablaGenerada", "tituloTablaGenerada", "ABECEDARIO TRASPOSICION GENERADO", data.abecedario_generado);
    actualizarTablaExplicativa(data.abecedario_explicativo);

    document.getElementById("tablaGenerada").style.display = "table";
    document.getElementById("tablaClaveNumericaExplicativa").style.display = "none";
}