# Cuarta lista de ejercicios — Introducción al Machine Learning

Universidad El Bosque, Programa de Matemáticas y Estadística, Semestre 2026–2.

**Integrantes:** <completar>

## Estructura del repositorio

- `data/` — los seis archivos CSV usados en los ejercicios (`experimento_1.csv`,
  `experimento_2_a.csv`, `experimento_2_b.csv`, `experimento_2_c.csv`,
  `experimento_3.csv`, `clientes.csv`).
- `src/lista4/` — paquete con el código reutilizable:
  - `data.py`: carga de los CSV desde `data/`.
  - `models.py`: ajuste de modelos de regresión lineal y logística (sklearn).
  - `metrics.py`: riesgo empírico cuadrático, riesgo empírico logístico,
    errores de clasificación y umbral de clasificación.
- `notebooks/` — un cuaderno por ejercicio (`ejercicio_1.ipynb` a
  `ejercicio_4.ipynb`), ya ejecutados, que importan las funciones de
  `src/lista4/` en vez de redefinirlas.

## Instalación

1. Clona el repositorio y ubícate en su carpeta.
2. Crea un entorno virtual:
   ```bash
   python -m venv venv
   # Windows:
   .\venv\Scripts\Activate.ps1
   # Mac/Linux:
   source venv/bin/activate
   ```
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Instala el paquete local `lista4` en modo editable, para que los notebooks
   puedan hacer `from lista4...import ...`:
   ```bash
   pip install -e .
   ```

## Ejecución

1. Abre cualquiera de los cuadernos en `notebooks/` (en VS Code o Jupyter).
2. Selecciona el kernel del entorno `venv`.
3. Ejecuta todas las celdas ("Run All"). Cada cuaderno es independiente y
   reutiliza las funciones de `src/lista4/` para cargar datos, ajustar
   modelos y calcular riesgos.
