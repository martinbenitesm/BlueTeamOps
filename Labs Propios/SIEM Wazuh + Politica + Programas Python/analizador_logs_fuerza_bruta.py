"""
Analizador de logs de autenticación fallida
--------------------------------------------
Automatiza la detección de posibles ataques de fuerza bruta a partir
de un archivo de log de intentos de inicio de sesión.

Simula el mismo tipo de análisis que haría un SIEM como Wazuh al
correlacionar eventos de autenticación fallida (Event ID 4625).

Conceptos de Python usados: estructuras de control (for, if),
diccionarios, listas, funciones.
"""

from collections import defaultdict
from datetime import datetime

# Umbral de intentos fallidos para considerar un posible ataque
UMBRAL_INTENTOS = 5


def leer_log(ruta_archivo):
    """Lee el archivo de log y devuelve una lista de líneas."""
    with open(ruta_archivo, "r", encoding="utf-8") as f:
        return f.readlines()


def parsear_linea(linea):
    """
    Convierte una línea de log en un diccionario con sus datos.
    Formato esperado de línea:
    2026-08-10 09:15:02 | FAILED_LOGIN | user=admin | ip=190.10.20.5
    """
    partes = [p.strip() for p in linea.split("|")]
    if len(partes) != 4:
        return None

    fecha_hora_str, evento, usuario_raw, ip_raw = partes
    return {
        "fecha_hora": datetime.strptime(fecha_hora_str, "%Y-%m-%d %H:%M:%S"),
        "evento": evento,
        "usuario": usuario_raw.split("=")[1],
        "ip": ip_raw.split("=")[1],
    }


def detectar_fuerza_bruta(eventos):
    """
    Agrupa los intentos fallidos por IP de origen y detecta cuáles
    superan el umbral definido, tal como lo haría una regla de
    correlación en un SIEM.
    """
    intentos_por_ip = defaultdict(list)

    for evento in eventos:
        if evento is None:
            continue
        if evento["evento"] == "FAILED_LOGIN":
            intentos_por_ip[evento["ip"]].append(evento)

    alertas = []
    for ip, lista_intentos in intentos_por_ip.items():
        if len(lista_intentos) >= UMBRAL_INTENTOS:
            usuarios_afectados = {intento["usuario"] for intento in lista_intentos}
            alertas.append({
                "ip_origen": ip,
                "cantidad_intentos": len(lista_intentos),
                "usuarios_objetivo": list(usuarios_afectados),
                "primer_intento": min(i["fecha_hora"] for i in lista_intentos),
                "ultimo_intento": max(i["fecha_hora"] for i in lista_intentos),
            })

    return alertas


def imprimir_reporte(alertas):
    """Imprime un resumen tipo 'alerta de SIEM' por consola."""
    if not alertas:
        print("No se detectaron patrones de fuerza bruta.")
        return

    print(f"Se detectaron {len(alertas)} posibles ataques de fuerza bruta:\n")
    for alerta in alertas:
        print(f"IP origen: {alerta['ip_origen']}")
        print(f"  Intentos fallidos: {alerta['cantidad_intentos']}")
        print(f"  Usuarios objetivo: {', '.join(alerta['usuarios_objetivo'])}")
        print(f"  Ventana de tiempo: {alerta['primer_intento']} -> {alerta['ultimo_intento']}")
        print("-" * 50)


if __name__ == "__main__":
    lineas = leer_log("log_ejemplo.txt")
    eventos = [parsear_linea(linea) for linea in lineas]
    alertas = detectar_fuerza_bruta(eventos)
    imprimir_reporte(alertas)
