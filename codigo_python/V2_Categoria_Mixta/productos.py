"""Productos abstractos y concretos para procesar informes."""
from abc import ABC, abstractmethod


class Informe(ABC):
    """Contrato comun a todos los informes."""

    @abstractmethod
    def procesar(self, nombre_archivo: str) -> str:
        """Simula el procesamiento y devuelve un mensaje descriptivo."""


class InformeFactura(Informe, ABC):
    """Producto abstracto para informes FACTURA."""


class InformeCompra(Informe, ABC):
    """Producto abstracto para informes COMPRA."""


class FacturaEntrada(InformeFactura):
    def procesar(self, nombre_archivo: str) -> str:
        return f"Procesando informe de ENTRADA de tipo FACTURA ({nombre_archivo})"


class CompraEntrada(InformeCompra):
    def procesar(self, nombre_archivo: str) -> str:
        return f"Procesando informe de ENTRADA de tipo COMPRA ({nombre_archivo})"


class FacturaSalida(InformeFactura):
    def procesar(self, nombre_archivo: str) -> str:
        return f"Procesando informe de SALIDA de tipo FACTURA ({nombre_archivo})"


class CompraSalida(InformeCompra):
    def procesar(self, nombre_archivo: str) -> str:
        return f"Procesando informe de SALIDA de tipo COMPRA ({nombre_archivo})"


class FacturaMixta(InformeFactura):
    def procesar(self, nombre_archivo: str) -> str:
        return f"Procesando informe de MIXTA de tipo FACTURA ({nombre_archivo})"


class CompraMixta(InformeCompra):
    def procesar(self, nombre_archivo: str) -> str:
        return f"Procesando informe de MIXTA de tipo COMPRA ({nombre_archivo})"
