function abrirCarrito() {
    const items_carrito_w = JSON.parse(document.getElementById('items-carrito').textContent);
    let mensaje = "¡Hola! Quiero comprar los siguientes productos:\n";
    let total = 0;

    items_carrito_w.forEach(item => {
        mensaje += `${item.id_producto__nombre_producto}, $${item.id_producto__precio_producto} x ${item.cantidad_prod}\n`;
        total += item.id_producto__precio_producto * item.cantidad_prod;
    });

    mensaje += `Total: $${total.toFixed(2)}`;
    let mensajeWhatsapp = encodeURIComponent(mensaje);

    window.location.href = `https://wa.me/56997092033/?text=${mensajeWhatsapp}`;
}