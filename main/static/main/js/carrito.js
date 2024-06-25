let carrito = [];
function agregarAlCarrito(producto){
    carrito.push(producto);
    alert(`"${producto}" se agregó al carrito.`);
}
function abrirCarrito(){
    let mensaje = encodeURIComponent(`¡Hola! Quiero comprar los siguientes productos: ${carrito.join(', ')}`);

    window.location.href = `https://wa.me/56997092033/?text=${mensaje}`;
}