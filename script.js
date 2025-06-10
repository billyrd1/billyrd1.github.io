
function mostrarTablaDesdeJSON(idTabla, archivoJson) {
    fetch(archivoJson)
        .then(response => response.json())
        .then(datos => {
            let html = `
                <h5>Tabla de Resultados</h5>
                <div class="table-responsive">
                    <table class="table table-bordered table-sm table-striped">
                        <thead class="table-dark">
                            <tr>
                                <th>Tiempo (t)</th>
                                <th>Heun</th>
                                <th>RK4</th>
                            </tr>
                        </thead>
                        <tbody>
            `;
            datos.forEach(fila => {
                html += `
                    <tr>
                        <td>${fila.Tiempo.toFixed(2)}</td>
                        <td>${fila.Heun.toFixed(4)}</td>
                        <td>${fila.RungeKutta4.toFixed(4)}</td>
                    </tr>
                `;
            });

            html += `</tbody></table></div>`;
            document.getElementById(idTabla).innerHTML = html;
        })
        .catch(error => console.error(`Error al cargar ${archivoJson}:`, error));
}

// Llamadas para cada sección
mostrarTablaDesdeJSON('tabla-37', 'datos/ejercicio_37.json');
mostrarTablaDesdeJSON('tabla-39', 'datos/ejercicio_39.json');
mostrarTablaDesdeJSON('tabla-40', 'datos/ejercicio_40.json');
