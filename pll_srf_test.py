import math_utils as mu
import math as m
import tranforms as tt
import pll_lib as pll

filename = 'pll_srf.dat'
f_grid = 60.0
ws = 2 * m.pi * f_grid
tf = 0.1
Tpwm = 200e-6
V = 220
pllsrf = pll.pll_srf(Tpwm, 1.0, 1.0, ws)
plljrm = pll.pll_jrm(Tpwm, 57.0, ws)

def plls_test():
    with open(filename, 'w') as f:
        f.write('#t u_g theta omega theta_srf theta_jrm\n')
        t = 0.0
        while(t < tf):
            v_a = mu.M_sqrt2f * V * m.sin(ws * t)
            v_b = mu.M_sqrt2f * V * m.sin(ws * t - mu.A120f)
            v_c = mu.M_sqrt2f * V * m.sin(ws * t + mu.A120f)
            v_alpha, v_beta = tt.abc_to_alphabeta(v_a, v_b, v_c)
            theta_srf = pllsrf.step(v_alpha, v_beta)
            theta_jrm = plljrm.step(v_alpha, v_beta)
            print(f'{t} {v_a} {pllsrf.theta} {pllsrf.omega} {theta_jrm} {plljrm.omega}', file=f)
            t += Tpwm
        print("Finished\n")

