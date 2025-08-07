# zoran-pypi

Ce dépôt contient la configuration et le packaging nécessaires pour distribuer Zoran IA via PyPI. Il s'agit d'une passerelle permettant d'installer facilement le cadre mimétique Zoran et d'exposer une interface Python minimaliste.

## Contenu

- `setup.py` : script de configuration du paquet. Décrit le package, ses dépendances et les métadonnées.
- `zoran_pypi/__init__.py` : module initial exposant une fonction `get_parser()` qui retourne la classe `GlottalParser` du projet zoran-ia (si celui‑ci est installé).

## Installation depuis PyPI (à venir)

Le package n'est pas encore publié sur PyPI. Lorsque cela sera fait, vous pourrez l'installer via :

```bash
pip install zoran-ia
```

## Utilisation

```python
from zoran_pypi import get_parser

Parser = get_parser()
parser = Parser(grammar_path="glottal_grammar.json")
result = parser.parse("ARTNODE:Epsilon Zeta Eta")
print(result)
```

## Développement

Pour développer ce package localement :

1. Cloner ce dépôt et le dépôt principal `zoran-ia`.
2. Créer un environnement virtuel et installer les dépendances si nécessaire.
3. Modifier le fichier `setup.py` pour inclure les packages appropriés.

## Licence

Ce dépôt est distribué sous licence MIT. Consultez le fichier LICENSE pour plus de détails.
