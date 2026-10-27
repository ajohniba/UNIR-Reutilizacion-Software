"""Punto de entrada de la V1 del sistema de informes.

Ejecutar: python codigo_python/V1_Sistema_Inicial/main.py
"""
from fabricas import FabricaEntrada, FabricaSalida
from procesador import ProcesadorInformes


def crear_procesador() -> ProcesadorInformes:
    """La composicion es el unico lugar que conoce factorias concretas."""
    fabricas = {
        "ENT": FabricaEntrada(),
        "SAL": FabricaSalida(),
    }
    creadores = {
        "FAC": lambda fabrica: fabrica.crear_factura(),
        "COM": lambda fabrica: fabrica.crear_compra(),
    }
    return ProcesadorInformes(fabricas, creadores)


def main() -> None:
    informes = [
        "ENT_FAC_001.txt",
        "ENT_COM_001.txt",
        "SAL_FAC_001.txt",
        "SAL_COM_001.txt",
    ]
    procesador = crear_procesador()
    for archivo in informes:
        print(procesador.procesar(archivo))


if __name__ == "__main__":
    main()
