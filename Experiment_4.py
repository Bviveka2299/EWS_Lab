
import pandas as pd
import matplotlib.pyplot as plt

# 1. Simulated Megger readings
data = {
    'Electrode_Depth_m': [1, 2, 3, 4, 5, 6, 7, 8],
    'Earth_Resistance_Ohm': [12.5, 9.8, 7.2, 5.8, 4.5, 3.8, 3.2, 2.7]
}

df = pd.DataFrame(data)

# 2. Define the illustrative safety threshold
threshold = 5.0

# 3. Rule-based classifier
def classify_resistance(value):
    if value > threshold:
        return "Exceeds Threshold"
    else:
        return "Within Threshold"

df['Safety_Status'] = df['Earth_Resistance_Ohm'].apply(
    classify_resistance
)

# 4. Display analysis results
print("EARTH RESISTANCE ANALYSIS")
print("-------------------------")
print(df.to_string(index=False))

# 5. Identify readings exceeding threshold
flagged = df[df['Earth_Resistance_Ohm'] > threshold]

print("\nREADINGS EXCEEDING THE THRESHOLD")
print("--------------------------------")
print(flagged.to_string(index=False))

# 6. Plot resistance versus electrode depth
plt.figure(figsize=(8, 5))

plt.plot(
    df['Electrode_Depth_m'],
    df['Earth_Resistance_Ohm'],
    marker='o',
    label='Earth Resistance'
)

plt.axhline(
    y=threshold,
    linestyle='--',
    label='Illustrative Threshold'
)

plt.xlabel("Electrode Depth (m)")
plt.ylabel("Earth Resistance (Ohm)")
plt.title("Earth Resistance vs Electrode Depth")

plt.grid(True)
plt.legend()
plt.show()
