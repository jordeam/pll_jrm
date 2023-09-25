import tranforms as tr
import math_utils as mu
import math as m

class pll_srf:
    T: float
    omega_n: float # nominal grid voltage
    omega: float
    theta: float
    v_q_: float # filtered q axis voltage
    v_q: float # axis voltage
    v_q_acc: float # accumulated q axis voltage
    k_p: float
    k_i: float

    def __init__(self, T_sample: float, k_p: float, k_i: float, omega_nominal: float):
        self.T = T_sample
        self.k_p = k_p
        self.k_i = k_i
        self.omega_n = omega_nominal
        self.omega = 0
        self.v_q_acc = 0
        self.theta = 0

    def step(self, v_alpha: float, v_beta: float) -> float:
        _, v_q = tr.alphabeta_2_dq(v_alpha, v_beta, self.theta)
        self.v_q_acc += v_q * self.T
        Delta_omega = self.k_p * v_q + self.k_i * self.v_q_acc
        self.omega = Delta_omega + self.omega_n
        self.theta += self.omega * self.T
        self.theta = mu.cycle(self.theta)
        return self.theta

class pll_jrm:
    pll_good: bool
    T: float
    omega_n: float # nominal grid voltage
    omega_acc: float # accumulated omega
    omega: float
    theta_ge: float
    theta: float # output grid angle
    v_d_: float # filtered d axis voltage
    v_q_: float # filtered q axis voltage
    k_p: float
    k_i: float

    def __init__(self, Tpwm: float, k_p: float, k_i: float, omega0: float):
        self.theta = 0.0
        self.T = Tpwm
        self.k_p = k_p
        self.k_i = k_i
        self.omega = omega0
        self.v_d_ = 0.0
        self.v_q_ = 0.0
        self.theta_ge = 0.0
        self.omega_acc = 0.0

    def step(self, v_alpha: float, v_beta: float) -> float:
        v_d, v_q = tr.alphabeta_2_dq(v_alpha, v_beta, self.theta)
        tau = 2.0 / (abs(self.omega) + 10.0)
        kf = self.T / tau
        self.v_d_ = kf * v_d + (1.0 - kf) * self.v_d_
        self.v_q_ = kf * v_q + (1.0 - kf) * self.v_q_
        theta_e = m.atan2(self.v_q_, self.v_d_);
        self.omega_acc += self.k_i * self.T * theta_e
        omega_g = self.omega_acc + self.k_p * theta_e
        self.theta_ge += omega_g * self.T
        self.theta = mu.cycle(self.theta_ge + theta_e)
        self.omega = omega_g
        self.theta_ge = mu.cycle(self.theta_ge);
        return self.theta
