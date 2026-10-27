"""Factorias: familias coherentes de productos (patron Abstract Factory)."""
from abc import ABC, abstractmethod
from productos import (
    InformeFactura, InformeCompra,
    FacturaEntrada, CompraEntrada, FacturaSalida, CompraSalida,
    FacturaMixta, CompraMixta, InformePedido, PedidoEntrada,
)


class FabricaInformes(ABC):
    """Contrato de la familia basica: FACTURA y COMPRA."""

    @abstractmethod
    def crear_factura(self) -> InformeFactura:
        pass

    @abstractmethod
    def crear_compra(self) -> InformeCompra:
        pass


class FabricaPedidos(ABC):
    """Interfaz segregada: capacidad especifica de crear pedidos."""

    @abstractmethod
    def crear_pedido(self) -> InformePedido:
        pass


class FabricaEntrada(FabricaInformes, FabricaPedidos):
    def crear_factura(self) -> InformeFactura:
        return FacturaEntrada()

    def crear_compra(self) -> InformeCompra:
        return CompraEntrada()

    def crear_pedido(self) -> InformePedido:
        return PedidoEntrada()


class FabricaSalida(FabricaInformes):
    def crear_factura(self) -> InformeFactura:
        return FacturaSalida()

    def crear_compra(self) -> InformeCompra:
        return CompraSalida()


class FabricaMixta(FabricaInformes):
    def crear_factura(self) -> InformeFactura:
        return FacturaMixta()

    def crear_compra(self) -> InformeCompra:
        return CompraMixta()
