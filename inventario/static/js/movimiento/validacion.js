console.log("entro")
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('miFormularioMovimiento');

    form.addEventListener('submit', function(event) {
        const cantidad = document.getElementById('id_cantidad').value;
        const tipo = document.getElementById('id_tipo').value;
        const origen = document.getElementById('id_origen').value
        const destino = document.getElementById('id_destino').value


        // Validación básica del lado del cliente
        if (cantidad <= 0) {
            alert('La cantidad debe ser mayor que cero.');
            event.preventDefault(); // Evitar que el formulario se envíe
        }

        if (tipo !== 'Entrada' && tipo !== 'Salida') {
            alert('El tipo de movimiento debe ser "Entrada" o "Salida".');
            event.preventDefault(); // Evitar que el formulario se envíe
        }

        if (origen == destino){
            alert('El origen no puede ser igual al destino');
            event.preventDefault(); // Evitar que el formulario se envíe
        }
    });
});