import torch
import matplotlib.pyplot as plt

x = torch.linspace(-5, 5, 200)
y = torch.tanh(x)

plt.plot(x, y)
plt.title("Tanh Activation Function")
plt.xlabel("Input")
plt.ylabel("Output")
plt.grid(True)
plt.show()

