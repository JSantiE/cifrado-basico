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
        trasposicion: document.getElementById("txtTrasposicion").value,
        abecedario: abecedarioBase
    };        
}

function procesarTrasposicion(data) {

    if (data.abecedario_generado.length === 0) {
        mostrarMensajeSinResultado("tituloTablaTrasposicion", "No se generó ningún abecedario");
        return;
    }

    renderizarTabla("filaTablaTrasposicion", "tituloTablaTrasposicion", "ABECEDARIO TRASPOSICION GENERADO", data.abecedario_generado);
    actualizarTablaExplicativa(data.abecedario_explicativo);

    document.getElementById("tablaTrasposicion").style.display = "table";
}