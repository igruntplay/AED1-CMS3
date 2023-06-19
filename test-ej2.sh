#!/bin/bash

# Definir función de prueba
test_unir_diccionarios() {
    input=$1
    expected=$2

    result=$(python3 unir_diccionarios.py <<< "$input")
    
    if [ "$result" == "$expected" ]; then
        echo "PASSED: Input: $input - Expected: $expected - Result: $result"
    else
        echo "FAILED: Input: $input - Expected: $expected - Result: $result"
    fi
}

# Ejecutar pruebas
test_unir_diccionarios "[{\"a\": 1, \"b\": 2}, {\"b\": 3, \"c\": 4}, {\"a\": 5}]" "{\"a\": [1, 5], \"b\": [2, 3], \"c\": [4]}"
test_unir_diccionarios "[{\"x\": 1}, {\"y\": 2}, {\"z\": 3}]" "{\"x\": [1], \"y\": [2], \"z\": [3]}"
test_unir_diccionarios "[{\"a\": 1, \"b\": 2}, {\"b\": 3, \"a\": 1}, {\"a\": 5, \"b\": 2}]" "{\"a\": [1, 1, 5], \"b\": [2, 3, 2]}"
test_unir_diccionarios "[]" "{}"  # Lista vacía
test_unir_diccionarios "[{}]" "{}"  # Diccionario vacío
test_unir_diccionarios "[{\"a\": 1}, {\"a\": 1}]" "{\"a\": [1, 1]}"  # Valores duplicados
