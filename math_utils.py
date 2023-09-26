import math

A30f: float = 0.523598775598
A60f: float = 1.0471975512
A90f: float = 1.5707963268
A120f: float = 2.0943951023931953
A180f: float = 3.14159265359
A240f: float = 4.18879020478
A300f: float = 5.235987756
A360f: float = 2 * math.pi

M_sqrt3_3f: float = 0.57735026919
M_sqrt2_2f: float = 0.707106781185
M_sqrt_2_3f: float = 0.816496580927726
M_sqrt_1_3f: float = 0.577350269189
M_sqrt3_2f: float = 0.866025403785
M_2PIf: float = 6.28318530718
M_sqrt3f: float = 1.73205080757
M_sqrt2f: float = 1.41421356237
M_sqrt_1_3f: float = 0.577350269189
M_sqrt_3_2f: float = 1.22474487139

def cycle(x: float) -> float:
    x /= 2 * math.pi
    x -= math.floor(x)
    return x * 2 * math.pi


def mcycle(x: float) -> float:
    x /= 2 * math.pi
    x -= math.floor(x)
    if x > 0.5:
        x -= 1.0
    return x * 2 * math.pi

