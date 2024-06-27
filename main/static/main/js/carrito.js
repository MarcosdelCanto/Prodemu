let carrito = [];
    function agregarAlCarrito(nombre_producto, precio_producto){
        carrito.push(nombre_producto,precio_producto);
        alert('"${nombre_producto}" se agregó al carrito.');
    }
    function abrirCarrito(){
        let mensaje = "¡Hola! Quiero comprar los siguientes productos:\n";
        let total = 0;

        carrito.forEach(item =>{
            mensaje += '${item.nombre_producto}, $${item.precio_producto}\n';
            total += item.precio_producto;
        });

        mensaje += 'Total: $${total}';
        let mensajeWhatsapp = encodeURIComponent(mensaje);
        
        window.location.href = 'https://wa.me/56997092033/?text=${mensajeWhatsapp}';
    }