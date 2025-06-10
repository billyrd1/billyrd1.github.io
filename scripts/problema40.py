import numpy as np
import matplotlib.pyplot as plt

# Definición de la ecuación diferencial
def ecuacion_caida(v, m=5, g=9.81, k=0.05):
    return (-m*g + k*v**2) / m

# Método de Heun
def heun(f, y0, t_range, h, *args):
    t = np.arange(t_range[0], t_range[1]+h, h)
    y = np.zeros(len(t))
    y[0] = y0
    
    for i in range(len(t)-1):
        k1 = f(y[i], *args)
        k2 = f(y[i] + h*k1, *args)
        y[i+1] = y[i] + 0.5*h*(k1 + k2)
    
    return t, y

# Método RK4
def rk4(f, y0, t_range, h, *args):
    t = np.arange(t_range[0], t_range[1]+h, h)
    y = np.zeros(len(t))
    y[0] = y0
    
    for i in range(len(t)-1):
        k1 = f(y[i], *args)
        k2 = f(y[i] + 0.5*h*k1, *args)
        k3 = f(y[i] + 0.5*h*k2, *args)
        k4 = f(y[i] + h*k3, *args)
        y[i+1] = y[i] + (h/6)*(k1 + 2*k2 + 2*k3 + k4)
    
    return t, y

# Parámetros y condiciones iniciales
v0 = 0
t_range = (0, 15)
h = 0.1  # tamaño de paso

# Resolver con ambos métodos
t_heun, v_heun = heun(ecuacion_caida, v0, t_range, h)
t_rk4, v_rk4 = rk4(ecuacion_caida, v0, t_range, h)

# Graficar resultados
plt.figure(figsize=(12, 6))
plt.plot(t_heun, v_heun, 'b-', linewidth=2, label='Heun')
plt.plot(t_rk4, v_rk4, 'r--', linewidth=2, label='RK4')
plt.title('Problema 40: Caída de Objeto con Resistencia del Aire', fontsize=14)
plt.xlabel('Tiempo (s)', fontsize=12)
plt.ylabel('Velocidad (m/s)', fontsize=12)
plt.legend(fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.savefig('problema40.png')
plt.show()

# Comparación en un punto específico (t=15)
print(f"Comparación en t=15 s:")
print(f"Método de Heun: v = {v_heun[-1]:.4f} m/s")
print(f"Método RK4:     v = {v_rk4[-1]:.4f} m/s")