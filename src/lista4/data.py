
from pathlib import Path
import pandas as pd

# Carpeta data/ en la raíz del repositorio, calculada en relación a este
# archivo: .../lista_4/src/lista4/data.py -> sube 2 niveles -> .../lista_4
DATA_DIR = Path(__file__).resolve().parents[2] / "data"


def load_csv(filename: str) -> pd.DataFrame:
    """
    Carga un archivo CSV desde la carpeta data/ del repositorio.

    Parámetros
    ----------
    filename : nombre del archivo, p.ej. "experimento_1.csv"

    Devuelve
    --------
    pandas.DataFrame con el contenido del archivo.
    """
    path = DATA_DIR / filename
    return pd.read_csv(path)
