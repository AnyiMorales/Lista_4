
import numpy as np


def riesgo_cuadratico(y_true, y_pred):
    """
    Riesgo empírico con pérdida cuadrática:
        R_S(h) = (1/n) * sum_i (y_i - h(x_i))^2
    """
    y_true = np.asarray(y_true, dtype=float)
    y_pred = np.asarray(y_pred, dtype=float)
    return np.mean((y_true - y_pred) ** 2)


def riesgo_logistico(y_true, p_hat, eps=1e-12):
    """
    Riesgo empírico logístico:
        R_S(h) = -(1/n) * sum_i [ y_i log(p_i) + (1-y_i) log(1-p_i) ]

    p_hat son las probabilidades estimadas P(Y=1|X=x_i). Se recortan a
    [eps, 1-eps] para evitar log(0) por redondeo numérico.
    """
    y_true = np.asarray(y_true, dtype=float)
    p_hat = np.clip(np.asarray(p_hat, dtype=float), eps, 1 - eps)
    return -np.mean(y_true * np.log(p_hat) + (1 - y_true) * np.log(1 - p_hat))


def errores_clasificacion(y_true, y_pred_clase):
    """
    Número y proporción de errores de clasificación.

    Devuelve
    --------
    (numero_errores, proporcion_errores)
    """
    y_true = np.asarray(y_true)
    y_pred_clase = np.asarray(y_pred_clase)
    n = y_true.shape[0]
    n_errores = int(np.sum(y_true != y_pred_clase))
    return n_errores, n_errores / n


def clasificar(p_hat, umbral=0.5):
    """
    Convierte probabilidades en clases usando un umbral (p_hat >= umbral -> 1).
    """
    p_hat = np.asarray(p_hat, dtype=float)
    return (p_hat >= umbral).astype(int)
