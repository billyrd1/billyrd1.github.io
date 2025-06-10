import numpy as np
import pandas as pd
import json

def heun(f, y0, t):
    y = [y0]
    for i in range(1, len(t)):
        h = t[i] - t[i - 1]
        y_pred = y[-1] + h * f(t[i - 1], y[-1])
        y_next = y[-1] + (h / 2) * (f(t[i - 1], y[-1]) + f(t[i], y_pred))
        y.append(y_next)
    return y

def rk4(f, y0, t):
    y = [y0]
    for i in range(1, len(t)):
        h = t[i] - t[i - 1]
        k1 = f(t[i - 1], y[-1])
        k2 = f(t[i - 1] + h / 2, y[-1] + h * k1 / 2)
        k3 = f(t[i - 1] + h / 2, y[-1] + h * k2 / 2)
        k4 = f(t[i], y[-1] + h * k3)
        y_next = y[-1] + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        y.append(y_next)
    return y

def ejercicio_37():
    k = 0.000095
    Nm = 5000
    N0 = 100
    t = np.linspace(0, 20, 21)
    f = lambda t, N: k * N * (Nm - N)
    heun_vals = heun(f, N0, t)
    rk4_vals = rk4(f, N0, t)
    tabla = pd.DataFrame({
        "Tiempo": t,
        "Heun": heun_vals,
        "RungeKutta4": rk4_vals
    })
    return tabla

def ejercicio_39():
    alpha = 0.8
    k_val = 60
    nu = 0.25
    A0 = 1
    t = np.linspace(0, 30, 31)
    f = lambda t, A: alpha * A * (1 - (A / k_val) ** nu)
    heun_vals = heun(f, A0, t)
    rk4_vals = rk4(f, A0, t)
    tabla = pd.DataFrame({
        "Tiempo": t,
        "Heun": heun_vals,
        "RungeKutta4": rk4_vals
    })
    return tabla

def ejercicio_40():
    m = 5
    g = 9.81
    k = 0.05
    v0 = 0
    t = np.linspace(0, 15, 31)
    f = lambda t, v: (-m * g + k * v ** 2) / m
    heun_vals = heun(f, v0, t)
    rk4_vals = rk4(f, v0, t)
    tabla = pd.DataFrame({
        "Tiempo": t,
        "Heun": heun_vals,
        "RungeKutta4": rk4_vals
    })
    return tabla

tabla_37 = ejercicio_37()
tabla_39 = ejercicio_39()
tabla_40 = ejercicio_40()

# Exportar a archivos JSON
tabla_37.to_json("ejercicio_37.json", orient="records", indent=2)
tabla_39.to_json("ejercicio_39.json", orient="records", indent=2)
tabla_40.to_json("ejercicio_40.json", orient="records", indent=2)

print("✅ Archivos generados: JSON y CSV para los 3 ejercicios.")
