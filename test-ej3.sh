#!/bin/bash

# Función de prueba
test_procesamiento_pedidos() {
    pedidos=$1
    stock=$2
    precios=$3
    expected=$4

    # Ejecutar el script de Python y capturar su salida
    result=$(printf "$pedidos\n$stock\n$precios\n" | python3 Ej3-ProcesamientoPedidos.py)

    if [[ "$result" == *"$expected"* ]]; then
        echo "PASSED: Expected: $expected - Result: $result"
    else
        echo "FAILED: Expected: $expected - Result: $result"
    fi
}

# Ejecutar pruebas
test_procesamiento_pedidos "[{\"id\":21,\"cliente\":\"Gabriela\", \"productos\":{\"Manzana\":2}}, {\"id\":1,\"cliente\":\"Juan\",\"productos\":{\"Manzana\":2,\"Pan\":4,\"Factura\":6}}]" "{\"Manzana\":10, \"Leche\":5, \"Pan\":3, \"Factura\":0}" "{\"Manzana\":3.5, \"Leche\":5.5, \"Pan\":3.5, \"Factura\":2.75}" "{'id': 21, 'cliente': 'Gabriela', 'productos': {'Manzana': 2}, 'precio_total': 7.0, 'estado': 'completo'}"
test_procesamiento_pedidos "[{\"id\":21,\"cliente\":\"Gabriela\", \"productos\":{\"Manzana\":2}}]" "{\"Manzana\":10, \"Leche\":5, \"Pan\":3, \"Factura\":0}" "{\"Manzana\":3.5, \"Leche\":5.5, \"Pan\":3.5, \"Factura\":2.75}" "{'id': 21, 'cliente': 'Gabriela', 'productos': {'Manzana': 2}, 'precio_total': 7.0, 'estado': 'completo'}"
test_procesamiento_pedidos "[{\"id\":21,\"cliente\":\"Gabriela\", \"productos\":{\"Manzana\":2, \"Pan\":4}}]" "{\"Manzana\":10, \"Leche\":5, \"Pan\":1, \"Factura\":0}" "{\"Manzana\":3.5, \"Leche\":5.5, \"Pan\":3.5, \"Factura\":2.75}" "{'id': 21, 'cliente': 'Gabriela', 'productos': {'Manzana': 2, 'Pan': 1}, 'precio_total': 10.5, 'estado': 'incompleto'}"
