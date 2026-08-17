/* =========================================================
    GENERAR CLAVE NUMERICA
========================================================= */

function generarClaveNumerica(){
    const datos = obtenerDatosClaveNumerica();

    enviarPost("/generarClaveNumerica", datos)
        .then(data => {
            procesarClaveNumerica(data);
        })
        .catch(error => {
            mostrarError("Error al generar la trama.", error);
        });
}

function obtenerDatosClaveNumerica(){
    return {
        claveNumerica: document.getElementById("txtClaveNumerica").value,
        abecedario: abecedarioBase
    };        
}

function procesarClaveNumerica(data) {

    if (data.abecedario_generado.length === 0) {
        mostrarMensajeSinResultado("tituloTablaClaveNumerica", "No se generó ningún abecedario");
        return;
    }

    renderizarTabla("filaTablaClaveNumerica", "tituloTablaClaveNumerica", "ABECEDARIO CLAVE NUMERICA GENERADO", data.abecedario_generado);
    mostrarTabla(data.columnas, data.abecedario_explicativo);

    document.getElementById("tablaClaveNumerica").style.display = "table";
    document.getElementById("tablaClaveNumericaExplicativa").style.display = "table";
}

function mostrarTabla(columnas, tabla){
    const tablaHTML = document.getElementById("tablaClaveNumericaExplicativa");
    const thead = tablaHTML.querySelector("thead");
    const tbody = tablaHTML.querySelector("tbody");

    thead.innerHTML = "";
    tbody.innerHTML = "";

    const filaEncabezado = document.createElement("tr");

    columnas.forEach(numero => {
        const th = document.createElement("th");

        th.textContent = numero;

        filaEncabezado.appendChild(th);
    });

    thead.appendChild(filaEncabezado);

    tabla.forEach(fila => {
        const tr = document.createElement("tr");

        fila.forEach(letra => {
            const td = document.createElement("td");

            td.textContent = letra;

            tr.appendChild(td);
        });

        tbody.appendChild(tr);
    });

}