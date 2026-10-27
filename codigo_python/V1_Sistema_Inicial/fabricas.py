"""Factorias: familias coherentes de productos (patron Abstract Factory)."""
from abc import ABC, abstractmethod
from productos import (
    InformeFactura, InformeCompra,
    FacturaEntrada, CompraEntrada, FacturaSalida, CompraSalida,
)


class FabricaInformes(ABC):
    """Contrato de la familia basica: FACTURA y COMPRA."""

    @abstractmethod
    def crear_factura(self) -> InformeFactura:
        pass

    @abstractmethod
    def crear_compra(self) -> InformeCompra:
        pass


class FabricaEntrada(FabricaInformes):
    def crear_factura(self) -> InformeFactura:
        return FacturaEntrada()

    def crear_compra(self) -> InformeCompra:
        return CompraEntrada()


class FabricaSalida(FabricaInformes):
    def crear_factura(self) -> InformeFactura:
        return FacturaSalida()

    def crear_compra(self) -> InformeCompra:
        return CompraSalida()
