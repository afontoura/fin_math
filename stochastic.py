import numpy as np
import matplotlib.pyplot as plt


class RandomWalk:

    def __init__(self, T, n=None):
        self.T = T
        if not n:
            self.n = T
            self.dt = 1
            self.is_scaled = False
        else:
            self.n = n
            self.dt = T / n
            if T == n:
                self.is_scaled = False
            else:
                self.is_scaled = True
        path = np.random.choice([-1, 1], size=self.n) * np.sqrt(self.dt)
        path = path.cumsum().tolist()
        path.insert(0, 0)
        self.path = path
        self.abs_var = np.round(np.sum(np.abs(np.diff(path))), 8)
        self.quad_var = np.round(np.sum(np.diff(path) ** 2), 8)

    def plot(self):
        time = np.arange(0, self.T + self.dt, self.dt)
        fig, ax = plt.subplots()
        ax.plot(time, self.path)
        ax.set(xlabel="time (Y)", ylabel="path", title="Random Walk")
        ax.grid()
        plt.show()
