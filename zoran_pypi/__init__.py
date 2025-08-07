"""
Zoran PyPI Package

This package sert de conteneur installable pour le cadre Zoran IA via PyPI.
Il fournit un accès pratique au parseur glottal, aux glyphes et aux injecteurs du projet principal.
"""

from importlib import import_module


def get_parser():
    """Retourne la classe GlottalParser depuis le package zoran-ia si installé."""
    try:
        module = import_module("glottal_parser")
        return module.GlottalParser
    except ImportError as e:
        raise ImportError("glottal_parser n'est pas installé. Installez zoran-ia.") from e
