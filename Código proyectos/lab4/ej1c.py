import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 20)
y = 3/4 * x - 1/2

pdispersos = y + np.random.randn(20)

aproximacion = np.polyval(np.polyfit(x, pdispersos, 1), x)

plt.plot(x, y, '*')
plt.plot(x, pdispersos, 'o')
plt.plot(x, aproximacion ,label="Aproximación lineal")
plt.legend()
plt.show()