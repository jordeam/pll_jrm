import numpy as np
import math as m

class MobAvg:

    def __init__(self, size: int):
        self.n: int = size
        self.acc: float = 0
        self.cursor: int = 0
        self.data = np.zeros((size))

    def inc(self):
        self.cursor += 1
        if self.cursor >= self.n:
            self.cursor = 0

    def update_avg(self, v: float) -> float:
        self.acc -= self.data[self.cursor]  # extract last value from AVG
        self.data[self.cursor] = v  # insert new value
        self.inc()
        self.acc += v
        return self.acc / self.n


class DLPF:
    """Digital low pass filter"""
    def __init__(self, tau: float, Tpwm: float) -> None:
        self.alpha: float = Tpwm / (2 * m.pi * tau)
        self.v: float = 0  # last filtered value

    def update(self, v: float) -> float:
        """Apply next value to filter and return filtered result"""
        self.v = self.alpha * v + (1.0 - self.alpha) * self.v
        return self.v
