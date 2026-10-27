"""Pruebas funcionales de la V1 con unittest (biblioteca estandar)."""
import unittest

from main import crear_procesador
from procesador import (
    InformeInvalido, CategoriaNoSoportada, TipoNoSoportado, ProcesadorInformes
)


class PruebasInformes(unittest.TestCase):
    def setUp(self) -> None:
        self.procesador = crear_procesador()

    def test_combinaciones_admitidas(self) -> None:
        casos = [
            ("ENT_FAC_001.txt", "ENTRADA de tipo FACTURA"),
            ("ENT_COM_001.txt", "ENTRADA de tipo COMPRA"),
            ("SAL_FAC_001.txt", "SALIDA de tipo FACTURA"),
            ("SAL_COM_001.txt", "SALIDA de tipo COMPRA"),
        ]
        for nombre, fragmento in casos:
            with self.subTest(nombre=nombre):
                self.assertIn(fragmento, self.procesador.procesar(nombre))

    def test_reconoce_rutas_de_archivo(self) -> None:
        self.assertIn("ENTRADA de tipo FACTURA", self.procesador.procesar("/datos/ENT_FAC_002.txt"))

    def test_formato_invalido(self) -> None:
        for nombre in ("FACTURA.txt", "ENT-FAC-001.txt", "ENT_FAC_.txt"):
            with self.subTest(nombre=nombre):
                with self.assertRaises(InformeInvalido):
                    self.procesador.procesar(nombre)

    def test_categoria_desconocida(self) -> None:
        with self.assertRaises(CategoriaNoSoportada):
            self.procesador.procesar("ZZZ_FAC_001.txt")

    def test_tipo_desconocido(self) -> None:
        with self.assertRaises(TipoNoSoportado):
            self.procesador.procesar("ENT_ZZZ_001.txt")


if __name__ == "__main__":
    unittest.main()
