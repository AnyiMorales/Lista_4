import numpy as np
from sklearn.linear_model import LinearRegression, LogisticRegression


def fit_linear(X, y):
    """
    Ajusta una regresión lineal con intercepto.

    Parámetros
    ----------
    X : array-like de forma (n, p) -- una o varias columnas predictoras
    y : array-like de forma (n,)

    Devuelve
    --------
    Un modelo LinearRegression ya ajustado (sklearn). Se puede acceder a
    model.intercept_ y model.coef_ para los coeficientes.
    """
    X = np.asarray(X)
    if X.ndim == 1:
        X = X.reshape(-1, 1)
    model = LinearRegression()
    model.fit(X, y)
    return model


def fit_logistic(X, y, C=1e6, max_iter=5000):
    """
    Ajusta una regresión logística con solver 'lbfgs'.

    Parámetros
    ----------
    X       : array-like de forma (n, p)
    y       : array-like de forma (n,), valores en {0, 1}
    C       : inverso de la fuerza de regularización (1e6 = casi sin
              regularización, tal como pide el enunciado)
    max_iter: número máximo de iteraciones del optimizador

    Devuelve
    --------
    Un modelo LogisticRegression ya ajustado (sklearn).
    """
    X = np.asarray(X)
    if X.ndim == 1:
        X = X.reshape(-1, 1)
    model = LogisticRegression(solver="lbfgs", C=C, max_iter=max_iter)
    model.fit(X, y)
    return model
