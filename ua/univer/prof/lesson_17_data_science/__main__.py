import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    x = np.arange(0, 4 * np.pi, 0.1)
    y = np.sin(x)
    plt.plot(x, y)
    plt.show()