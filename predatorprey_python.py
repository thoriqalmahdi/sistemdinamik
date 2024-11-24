#predator prey

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


# Parameter sebagai list (panjang list harus sama untuk setiap parameter)
r1_values = [1, 1.2, 0.1]
r2_values = [0.8, 1.0, 0.3]
a1_values = [0.1, 0.15, 0.05]
a2_values = [0.1, 0.15, 0.01]
v1_values = [0.02, 0.03, 0.01]
v2_values = [0.02, 0.03, 0.03]

# Fungsi sistem diferensial
def predator_prey_model(pop, t, r1, r2, a1, a2, v1, v2):
    x, y = pop
    dxdt = r1 * x - a1 * x**2 - v1 * x * y
    dydt = r2 * y - a2 * y**2 + v2 * x * y
    return [dxdt, dydt]

# Waktu simulasi
t = np.linspace(0, 50, 500)

# Kondisi awal [mangsa, predator]
initial_conditions = [10, 5]

# Pastikan semua list parameter memiliki panjang yang sama
num_iterations = len(r1_values)
if not all(len(lst) == num_iterations for lst in [r2_values, a1_values, a2_values, v1_values, v2_values]):
    raise ValueError("Semua list parameter harus memiliki panjang yang sama!")

# Loop untuk setiap set parameter
for i in range(num_iterations):
    # Ambil parameter untuk iterasi ini
    r1 = r1_values[i]
    r2 = r2_values[i]
    a1 = a1_values[i]
    a2 = a2_values[i]
    v1 = v1_values[i]
    v2 = v2_values[i]

    # Solusi ODE untuk parameter saat ini
    solution = odeint(predator_prey_model, initial_conditions, t, args=(r1, r2, a1, a2, v1, v2))
    x, y = solution.T

    # Buat figure dengan 2 subplots sejajar
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # Subplot 1: Evolusi populasi
    axes[0].plot(t, x, 'r-', label="x(t) (Mangsa)")
    axes[0].plot(t, y, 'g--', label="y(t) (Predator)")
    axes[0].set_title(f"r1={r1}, r2={r2}, a1={a1}, a2={a2}, v1={v1}, v2={v2}\nEvolusi Populasi")
    axes[0].set_xlabel("Waktu (t)")
    axes[0].set_ylabel("Populasi")
    axes[0].legend()
    axes[0].grid()

    # Subplot 2: Diagram fase
    axes[1].plot(x, y, 'b-')
    axes[1].set_title("Diagram Fase")
    axes[1].set_xlabel("Populasi Mangsa, x")
    axes[1].set_ylabel("Populasi Predator, y")
    axes[1].grid()

    # Atur layout agar tidak saling tumpang tindih
    plt.tight_layout()

# Tampilkan grafik
plt.show()
