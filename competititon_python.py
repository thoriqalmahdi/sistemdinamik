#Competition Model

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Parameter sebagai list (panjang list harus sama untuk setiap parameter)
r1_values = [1.0, 1.2]
r2_values = [0.8, 0.9]
c11_values = [0.1, 0.2]
c22_values = [0.1, 0.15]
c12_values = [0.02, 0.03]
c21_values = [0.02, 0.04]

# Fungsi sistem diferensial Lotka-Volterra kompetisi
def competition_model(pop, t, r1, r2, c11, c22, c12, c21):
    n1, n2 = pop
    dn1_dt = r1 * n1 - c11 * n1**2 - c12 * n1 * n2
    dn2_dt = r2 * n2 - c22 * n2**2 - c21 * n2 * n1
    return [dn1_dt, dn2_dt]

# Waktu simulasi
t = np.linspace(0, 50, 500)

# Kondisi awal [n1, n2]
initial_conditions = [20, 15]

# Pastikan semua list parameter memiliki panjang yang sama
num_iterations = len(r1_values)
if not all(len(lst) == num_iterations for lst in [r2_values, c11_values, c22_values, c12_values, c21_values]):
    raise ValueError("Semua list parameter harus memiliki panjang yang sama!")

# Loop untuk setiap set parameter
for i in range(num_iterations):
    # Ambil parameter untuk iterasi ini
    r1 = r1_values[i]
    r2 = r2_values[i]
    c11 = c11_values[i]
    c22 = c22_values[i]
    c12 = c12_values[i]
    c21 = c21_values[i]

    # Solusi ODE untuk parameter saat ini
    solution = odeint(competition_model, initial_conditions, t, args=(r1, r2, c11, c22, c12, c21))
    n1, n2 = solution.T

    # Buat figure dengan 2 subplots sejajar
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # Subplot 1: Evolusi populasi
    axes[0].plot(t, n1, 'b-', label="n1 (Spesies 1)")
    axes[0].plot(t, n2, 'r--', label="n2 (Spesies 2)")
    axes[0].set_title(f"r1={r1}, r2={r2}, c11={c11}, c22={c22}, c12={c12}, c21={c21}\nEvolusi Populasi")
    axes[0].set_xlabel("Waktu (t)")
    axes[0].set_ylabel("Populasi")
    axes[0].legend()
    axes[0].grid()

    # Subplot 2: Diagram fase
    axes[1].plot(n1, n2, 'g-')
    axes[1].set_title("Diagram Fase")
    axes[1].set_xlabel("Populasi Spesies 1 (n1)")
    axes[1].set_ylabel("Populasi Spesies 2 (n2)")
    axes[1].grid()

    # Atur layout agar tidak saling tumpang tindih
    plt.tight_layout()

# Tampilkan grafik
plt.show()
