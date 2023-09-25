import math_utils as mu
import math as m
import tranforms as tt
import pll_lib as pll

filename = 'pll_srf.dat'
f_grid = 60.0
w_grid = 2 * m.pi * f_grid
tf = 4
Tpwm = 100e-6
V = 220
pllsrf = pll.pll_srf(Tpwm, 1.0, 1.0, w_grid)
plljrm = pll.pll_jrm(Tpwm, 240.0, 1800.0, w_grid)


def plls_test():
    global w_grid
    ws = w_grid
    theta_grid = 0.0
    with open(filename, 'w') as f:
        f.write('#t u_g theta omega theta_srf theta_jrm\n')
        t = 0.0
        while t < tf:
            if t > 0.5:
                ws = 2 * m.pi * 30.0
            theta_grid += ws * Tpwm
            theta_grid = mu.cycle(theta_grid)
            v_a = mu.M_sqrt2f * V * m.cos(theta_grid)
            v_b = mu.M_sqrt2f * V * m.cos(theta_grid - mu.A120f)
            v_c = mu.M_sqrt2f * V * m.cos(theta_grid + mu.A120f)
            v_alpha, v_beta = tt.abc_to_alphabeta(v_a, v_b, v_c)
            theta_srf = pllsrf.step(v_alpha, v_beta)
            theta_jrm = plljrm.step(v_alpha, v_beta)

            print(f'{t} {v_a} {theta_grid} {theta_srf} {pllsrf.omega} {theta_jrm} {plljrm.omega} {ws} {plljrm.v_d_} {plljrm.v_q_}', file=f)
            t += Tpwm
        print("Finished\n")

