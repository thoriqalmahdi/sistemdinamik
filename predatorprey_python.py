import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Parameter
r1 = 0.1;   # Pertumbuhan populasi x
r2 = 0.3;  # Pertumbuhan populasi y
a1 = 0.05;  # Kompetisi populasi x
a2 = 0.01;  # Kompetisi populasi y
v1 = 0.01; # Interaksi antara x dan y
v2 = 0.03; # Interaksi antara y dan x


# Fungsi sistem persamaan diferensial
def predator_prey(t, z):
    x, y = z
    dxdt = r1 * x - a1 * x**2 - v1 * x * y
    dydt = r2 * y - a2 * y**2 + v2 * x * y
    return [dxdt, dydt]

# Kondisi awal
x0 = 10  # Populasi awal mangsa
y0 = 5   # Populasi awal predator
z0 = [x0, y0]

# Rentang waktu simulasi
t_span = (0, 50)          # Interval waktu
t_eval = np.linspace(0, 50, 500)  # Titik evaluasi

# Penyelesaian menggunakan metode Runge-Kutta
sol = solve_ivp(predator_prey, t_span, z0, t_eval=t_eval)

# Hasil simulasi
t = sol.t
x = sol.y[0]  # Populasi mangsa
y = sol.y[1]  # Populasi predator

# Plot evolusi populasi
plt.figure(figsize=(10, 5))
plt.plot(t, x, 'r-', label="x(t) (Mangsa)", linewidth=2)
plt.plot(t, y, 'g--', label="y(t) (Predator)", linewidth=2)
plt.title("Evolusi Populasi Predator-Prey")
plt.xlabel("Waktu (t)")
plt.ylabel("Populasi")
plt.legend()
plt.grid()
plt.show()

# Plot diagram fase
plt.figure(figsize=(8, 6))
plt.plot(x, y, 'b-', linewidth=2)
plt.title("Diagram Fase Predator-Prey")
plt.xlabel("Populasi Mangsa, x")
plt.ylabel("Populasi Predator, y")
plt.grid()
plt.show()
