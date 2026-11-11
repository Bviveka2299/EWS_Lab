import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Experimental measurements
V = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
I = np.array([
    0.098, 0.201, 0.299, 0.402, 0.498,
    0.601, 0.699, 0.802, 0.901, 1.001
])

# Prepare input data
X = I.reshape(-1, 1)

# Fit regression model
model = LinearRegression()
model.fit(X, V)
V_pred = model.predict(X)

# Estimate resistance and error
R_exp = model.coef_[0]
R_nominal = 10
error = abs(R_exp - R_nominal) / R_nominal * 100
R2 = model.score(X, V)

print("Nominal Resistance:", R_nominal, "Ohms")
print("Experimental Resistance:", R_exp, "Ohms")
print("Percentage Error:", error, "%")
print("R-squared:", R2)

# Plot measurements and regression line
plt.scatter(I, V, label="Measured Data")
plt.plot(I, V_pred, label="Regression Line")
plt.xlabel("Current (A)")
plt.ylabel("Voltage (V)")
plt.title("Verification of Ohm's Law")
plt.legend()
plt.grid(True)
plt.show()

