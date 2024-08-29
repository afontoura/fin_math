import numpy as np
import matplotlib.pyplot as plt

class RandomWalk:
    
    def __init__(self, T):
        self.T = T
        path = np.random.choice([-1, 1], size=T)
        path = path.cumsum().tolist()
        path.insert(0, 0)
        self.path = path
        
    def plot(self):
        time = np.arange(0, self.T+1, 1)
        fig, ax = plt.subplots()
        ax.plot(time, self.path)
        ax.set(xlabel="time (Y)", ylabel="path", title="Random Walk")
        ax.grid()
        plt.show()
        