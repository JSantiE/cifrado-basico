/* =========================================================
    FUNCIONES GENERALES
========================================================= */
let abecedarioBase;
let abecedarioGenerado;

function enviarPost(url, datos){

    return fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(datos)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("Error del servidor");
        }

        return response.json();
    });
}

function mostrarError(mensaje, error) {
    console.error("Error:", error);
    document.getElementById("resultado").innerText = mensaje;
}

function mostrarMensajeSinResultado(idTitulo, mensaje) {
    document.getElementById(idTitulo).innerText = mensaje;
}

function agregarCeldas(fila, datos) {
    for (const dato of datos) {
        const celda = fila.insertCell();
        celda.innerText = dato;
    }
}

function renderizarTabla(idFila, idTitulo, titulo, datos) {

    const fila = document.getElementById(idFila);
    const tituloTabla = document.getElementById(idTitulo);

    fila.innerHTML = "";
    tituloTabla.colSpan = datos.length;
    tituloTabla.innerText = titulo;

    for (const dato of datos) {
        const celda = document.createElement("td");
        celda.innerText = dato;
        fila.appendChild(celda);
    }
}

function actualizarTablaExplicativa(datos) {

    const tabla = document.getElementById("tablaAbecedario");
    let fila = document.getElementById("filaTrasposicion");

    // Crear la fila solamente si todavía no existe
    if (!fila) {
        fila = tabla.insertRow();
        fila.id = "filaTrasposicion";
    }
    else {
        fila.innerHTML = "";
    }

    agregarCeldas(fila, datos.map(elemento => elemento.id));
}
