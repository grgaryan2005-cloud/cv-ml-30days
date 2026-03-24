import matplotlib
matplotlib.use('Agg')
import  numpy as np
import matplotlib.pyplot as plt

balls = np.array([10, 20, 30, 40, 12,  15, 23, 40, 8,  91, 22])
runs = np.array([30, 10, 90, 109, 80, 11,  60, 100, 19, 100, 22])
balls_mean = balls.mean()
runs_mean = runs.mean()
m = np.sum((balls - balls_mean) * (runs - runs_mean)) /\
     np.sum((balls - balls_mean) ** 2)
b = runs_mean - m * balls_mean
print(f"Every extra ball = {m:.2f} extra runs")
print(f"Intercept = {b:.2f}")
runs_pred = m * balls + b
mse = np.mean((runs - runs_pred) ** 2)
print(f"MSE = {mse:.2f}")
new_balls = 75
predicted = m * new_balls + b
print(f"75 balls ->predicted {predicted:.0f} runs")
plt.figure(figsize=(9, 5))
plt.scatter(balls, runs, color='green',  s=60, label='actual scores')
plt.plot(balls, runs_pred, color='purple',  linewidth=2, label='prediction line')
plt.scatter(new_balls, predicted, color='orange', s=100, label='new prediction')
plt.xlabel('Balls Faced')
plt.ylabel('Runs Scored')
plt.title('Cricket score predictor')
plt.legend()
plt.savefig('cricket_plt.png')
print("plt saved")
