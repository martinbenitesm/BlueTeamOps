"""
Validador de cumplimiento de la Política de Contraseñas
----------------------------------------------------------
Automatiza la verificación de si una contraseña cumple con los
requisitos definidos en la Política de Contraseñas y Autenticación
Segura (longitud mínima 10 caracteres, mayúsculas, minúsculas,
números y caracteres especiales).

Conceptos de Python usados: estructuras de control (for, if/elif),
listas, diccionarios, funciones.
"""

import re

LONGITUD_MINIMA = 10
CARACTERES_ESPECIALES = "!@#$%^&*()_+-=[]{}|;:,.<>?"


def validar_contrasena(contrasena):
    """
    Evalúa una contraseña contra cada requisito de la política y
    devuelve un diccionario con el detalle de qué cumple y qué no.
    """
    errores = []

    if len(contrasena) < LONGITUD_MINIMA:
        errores.append(f"Debe tener al menos {LONGITUD_MINIMA} caracteres")

    if not re.search(r"[A-Z]", contrasena):
        errores.append("Debe incluir al menos una letra mayúscula")

    if not re.search(r"[a-z]", contrasena):
        errores.append("Debe incluir al menos una letra minúscula")

    if not re.search(r"[0-9]", contrasena):
        errores.append("Debe incluir al menos un número")

    if not any(caracter in CARACTERES_ESPECIALES for caracter in contrasena):
        errores.append("Debe incluir al menos un carácter especial")

    cumple = len(errores) == 0
    return {
        "contrasena": contrasena,
        "cumple_politica": cumple,
        "errores": errores,
    }


def validar_lista(lista_contrasenas):
    """Valida una lista de contraseñas y devuelve el resultado de cada una."""
    resultados = []
    for contrasena in lista_contrasenas:
        resultados.append(validar_contrasena(contrasena))
    return resultados


def imprimir_reporte(resultados):
    """Imprime un resumen del cumplimiento, similar a un reporte de auditoría."""
    total = len(resultados)
    cumplen = sum(1 for r in resultados if r["cumple_politica"])

    print(f"Auditoría de contraseñas: {cumplen}/{total} cumplen la política\n")

    for resultado in resultados:
        estado = "CUMPLE" if resultado["cumple_politica"] else "NO CUMPLE"
        print(f"[{estado}] {resultado['contrasena']}")
        for error in resultado["errores"]:
            print(f"   - {error}")


if __name__ == "__main__":
    # Lista de ejemplo simulando una auditoría de contraseñas de usuarios
    contrasenas_a_evaluar = [
        "12345678",
        "Password1",
        "F0nd0#Segur1dad2026",
        "abcdefghij",
        "C1b3r$eg2026",
    ]

    resultados = validar_lista(contrasenas_a_evaluar)
    imprimir_reporte(resultados)
