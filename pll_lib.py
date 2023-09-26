import tranforms as tr
import math_utils as mu
import math as m


class PllSrf:
    """SRF PLL"""

    def __init__(self, T_sample: float, k_p: float, k_i: float, omega_nominal: float):
        self.T: float = T_sample  # time sample
        self.k_p: float = k_p
        self.k_i: float = k_i
        self.omega_n: float = omega_nominal  # grid nominal frequency
        self.omega: float = 0.0  # estimated grid frequency
        self.v_q_: float = 0.0  # filtered q axis voltage
        self.v_q: float = 0.0  # axis voltage
        self.v_q_acc: float = 0.0  # accumulated v_q value
        self.theta = 0.0  # estimated grid angle

    def step(self, v_alpha: float, v_beta: float) -> float:
        _, v_q = tr.alphabeta_2_dq(v_alpha, v_beta, self.theta)
        self.v_q_acc += v_q * self.T
        Delta_omega = self.k_p * v_q + self.k_i * self.v_q_acc
        self.omega = Delta_omega + self.omega_n
        self.theta += self.omega * self.T
        self.theta = mu.cycle(self.theta)
        return self.theta


class PllJrm:
    """Proposed PLL"""

    def __init__(self, Tpwm: float, k_p: float, k_i: float, omega0: float):
        self.theta: float = 0.0  # estimated grid frequency
        self.T: float = Tpwm  # time sample
        self.k_p: float = k_p
        self.k_i: float = k_i
        self.omega: float = 0.0 # estimated grid frequency
        self.v_d_: float = 0.0
        self.v_q_: float = 0.0
        self.theta_ge: float = 0.0
        self.omega_acc: float = 0.0  # accumulated omega
        self.theta: float  # estimated grid angle

    def step(self, v_alpha: float, v_beta: float) -> float:
        """Eval one time sample"""
        v_d, v_q = tr.alphabeta_2_dq(v_alpha, v_beta, self.theta)
        tau = 2.0 / (abs(self.omega) + 10.0)
        k_f = self.T / tau
        self.v_d_ = k_f * v_d + (1.0 - k_f) * self.v_d_
        self.v_q_ = k_f * v_q + (1.0 - k_f) * self.v_q_
        theta_e = m.atan2(self.v_q_, self.v_d_)
        self.omega_acc += self.k_i * self.T * theta_e
        omega_g = self.omega_acc + self.k_p * theta_e
        self.theta_ge += omega_g * self.T
        self.theta = mu.cycle(self.theta_ge + theta_e)
        self.omega = omega_g
        self.theta_ge = mu.cycle(self.theta_ge)
        return self.theta


class PllQT1:
    """Quase Type 1 PLL (Golestan)"""

    def __init__(self, Tpwm: float, k_p: float, omega_nominal: float):
        self.theta: float = 0.0 # output grid angle
        self.T: float = Tpwm
        self.k_p: float = k_p
        self.omega_n: float = omega_nominal  # nominal grid voltage
        self.v_d_: float = 0.0  # filtered d axis voltage
        self.v_q_: float = 0.0  # filtered q axis voltage
        self.theta_e: float = 0.0
        self.omega_acc: float = 0.0  # accumulated omega
        self.theta_o: float = 0.0
        self.omega: float = 0.0

    def step(self, v_alpha: float, v_beta: float) -> float:
        """Eval one time sample"""
        v_d, v_q = tr.alphabeta_2_dq(v_alpha, v_beta, self.theta_o)
        tau = 2.0 / (abs(self.omega) + 10.0)
        k_f = self.T / tau
        self.v_d_ = k_f * v_d + (1.0 - k_f) * self.v_d_
        self.v_q_ = k_f * v_q + (1.0 - k_f) * self.v_q_
        theta_e = m.atan2(self.v_q_, self.v_d_)
        self.omega = self.k_p * theta_e + self.omega_n
        self.theta_o += self.omega * self.T
        self.theta = mu.cycle(self.theta_o + theta_e)
        return self.theta
