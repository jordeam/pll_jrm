import math as m
import math_utils as mu

def alphabeta_2_dq(alpha: float, beta: float, theta: float) -> tuple:
    sin_theta = m.sin(theta)
    cos_theta = m.cos(theta)
    d = alpha * cos_theta + beta * sin_theta
    q = -alpha * sin_theta + beta * cos_theta
    return d, q

def abc_to_alphabeta(a: float, b: float, c: float) -> tuple:
    alpha = mu.M_sqrt_2_3f * (a - 0.5 * b - 0.5 * c)
    beta = mu.M_sqrt_2_3f * (mu.M_sqrt3_2f * b - mu.M_sqrt3_2f * c)
    return alpha, beta

