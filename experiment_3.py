
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------------
# 1. SINGLE-PHASE PHASOR DIAGRAM
# -----------------------------------------

V = 230
I = 10
phase_angle = 30

# Voltage and current phasors
V_phasor = V * np.exp(1j * np.deg2rad(0))
I_phasor = I * np.exp(1j * np.deg2rad(-phase_angle))

plt.figure(figsize=(6, 6))

plt.quiver(0, 0, V_phasor.real, V_phasor.imag,
           angles='xy', scale_units='xy', scale=1,
           label='Voltage (230 V)')

plt.quiver(0, 0, I_phasor.real, I_phasor.imag,
           angles='xy', scale_units='xy', scale=1,
           label='Current (10 A)')

plt.xlim(-20, 260)
plt.ylim(-100, 150)
plt.xlabel("Real Axis")
plt.ylabel("Imaginary Axis")
plt.title("Single-Phase Phasor Diagram")
plt.grid()
plt.axhline(0)
plt.axvline(0)
plt.legend()
plt.show()


# -----------------------------------------
# 2. THREE-PHASE PHASOR DIAGRAM
# -----------------------------------------

V_phase = 230

# Three balanced phase voltages
angles = [0, -120, 120]
phase_names = ['R Phase', 'Y Phase', 'B Phase']

plt.figure(figsize=(6, 6))

for angle, name in zip(angles, phase_names):

    phasor = V_phase * np.exp(1j * np.deg2rad(angle))

    plt.quiver(0, 0, phasor.real, phasor.imag,
               angles='xy', scale_units='xy', scale=1,
               label=name)

plt.xlim(-260, 260)
plt.ylim(-260, 260)
plt.xlabel("Real Axis")
plt.ylabel("Imaginary Axis")
plt.title("Three-Phase Voltage Phasor Diagram")
plt.grid()
plt.axhline(0)
plt.axvline(0)
plt.legend()
plt.gca().set_aspect('equal')
plt.show()


# -----------------------------------------
# 3. TRANSFORMER TURNS RATIO CALCULATION
# -----------------------------------------

Vp = float(input("Enter primary voltage (V): "))
Np = float(input("Enter primary turns: "))
Ns = float(input("Enter secondary turns: "))

# Transformer turns ratio
turns_ratio = Np / Ns

# Secondary voltage
Vs = Vp * (Ns / Np)

print("\nTRANSFORMER ANALYSIS")
print("-------------------------")
print("Primary Voltage:", Vp, "V")
print("Primary Turns:", Np)
print("Secondary Turns:", Ns)
print("Turns Ratio (Np/Ns):", round(turns_ratio, 2))
print("Secondary Voltage:", round(Vs, 2), "V")
