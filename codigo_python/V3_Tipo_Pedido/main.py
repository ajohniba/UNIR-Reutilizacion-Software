"""Punto de entrada de la V3 del sistema de informes.

Ejecutar: python codigo_python/V3_Tipo_Pedido/main.py
"""
from fabricas import FabricaEntrada, FabricaSalida, FabricaMixta
from procesador import ProcesadorInformes, TipoNoSoportado
from fabricas import FabricaInformes, FabricaPedidos
from productos import InformePedido


def crear_procesador() -> ProcesadorInformes:
    """La composicion es el unico lugar que conoce factorias concretas."""
    fabricas = {
        "ENT": FabricaEntrada(),
        "SAL": FabricaSalida(),
        "MIX": FabricaMixta(),
    }
    creadores = {
        "FAC": lambda fabrica: fabrica.crear_factura(),
        "COM": lambda fabrica: fabrica.crear_compra(),
        "PED": crear_pedido,
    }
    return ProcesadorInformes(fabricas, creadores)


def crear_pedido(fabrica: FabricaInformes) -> InformePedido:
    """Comprueba la capacidad especial sin ampliar FabricaInformes."""
    if not isinstance(fabrica, FabricaPedidos):
        raise TipoNoSoportado("PEDIDO solo esta disponible en ENTRADA")
    return fabrica.crear_pedido()


def main() -> None:
    informes = [
        "ENT_FAC_001.txt",
        "ENT_COM_001.txt",
        "SAL_FAC_001.txt",
        "SAL_COM_001.txt",
        "MIX_FAC_001.txt",
        "MIX_COM_001.txt",
        "ENT_PED_001.txt",
    ]
    procesador = crear_procesador()
    for archivo in informes:
        print(procesador.procesar(archivo))


if __name__ == "__main__":
    main()
