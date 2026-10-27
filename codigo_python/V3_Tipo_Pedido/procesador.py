"""Procesador agnostico a las factorias y a los tipos concretos.

Este modulo no cambia entre V1, V2 y V3. La composicion de la
aplicacion registra nuevas factorias y tipos al evolucionar.
"""
from dataclasses import dataclass
from pathlib import Path
import re
from typing import Callable, Mapping

from fabricas import FabricaInformes
from productos import Informe


class InformeInvalido(ValueError):
    """El nombre de archivo no cumple el formato CAT_TIPO_codigo.txt."""


class CategoriaNoSoportada(ValueError):
    """No existe una factoria registrada para esta categoria."""


class TipoNoSoportado(ValueError):
    """El tipo no existe o no esta disponible para esa categoria."""


@dataclass(frozen=True)
class IdentificadorInforme:
    categoria: str
    tipo: str
    codigo: str


class ProcesadorInformes:
    """Coordina la identificacion, creacion abstracta y procesamiento."""

    _PATRON = re.compile(r"^([A-Z]{3})_([A-Z]{3})_([A-Za-z0-9-]+)\.txt$")

    def __init__(
        self,
        fabricas: Mapping[str, FabricaInformes],
        creadores: Mapping[str, Callable[[FabricaInformes], Informe]],
    ) -> None:
        self._fabricas = dict(fabricas)
        self._creadores = dict(creadores)

    @classmethod
    def identificar(cls, ruta: str) -> IdentificadorInforme:
        nombre = Path(ruta).name
        coincidencia = cls._PATRON.fullmatch(nombre)
        if coincidencia is None:
            raise InformeInvalido(
                f"Nombre invalido: {nombre!r}. Formato esperado: CAT_TIPO_codigo.txt"
            )
        return IdentificadorInforme(*coincidencia.groups())

    def procesar(self, ruta: str) -> str:
        identificador = self.identificar(ruta)
        fabrica = self._fabricas.get(identificador.categoria)
        if fabrica is None:
            raise CategoriaNoSoportada(
                f"Categoria no registrada: {identificador.categoria}"
            )
        creador = self._creadores.get(identificador.tipo)
        if creador is None:
            raise TipoNoSoportado(f"Tipo no registrado: {identificador.tipo}")
        informe = creador(fabrica)
        return informe.procesar(Path(ruta).name)
