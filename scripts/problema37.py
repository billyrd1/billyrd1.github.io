import numpy as np
import matplotlib.pyplot as plt

def ecuacion_poblacional(N, k=0.000095, N_M=5000):
    return k * N * (N_M - N)

def heun(f, y0, t_range, h, *args):
    t = np.arange(t_range[0], t_range[1]+h, h)
    y = np.zeros(len(t))
    y[0] = y0
    
    for i in range(len(t)-1):
        k1 = f(y[i], *args)
        k2 = f(y[i] + h*k1, *args)
        y[i+1] = y[i] + 0.5*h*(k1 + k2)
    
    return t, y

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

N0 = 100
t_range = (0, 20)
h = 0.1

t_heun, N_heun = heun(ecuacion_poblacional, N0, t_range, h)
t_rk4, N_rk4 = rk4(ecuacion_poblacional, N0, t_range, h)

# Graficar resultados
plt.figure(figsize=(12, 6))
plt.plot(t_heun, N_heun, 'b-', linewidth=2, label='Heun')
plt.plot(t_rk4, N_rk4, 'r--', linewidth=2, label='RK4')
plt.title('Problema 37: Crecimiento Poblacional', fontsize=14)
plt.xlabel('Tiempo (años)', fontsize=12)
plt.ylabel('Población (N)', fontsize=12)
plt.legend(fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.savefig('problema37.png')
plt.show()

print(f"Comparación en t=20 años:")
print(f"Método de Heun: N = {N_heun[-1]:.2f}")
print(f"Método RK4:     N = {N_rk4[-1]:.2f}")