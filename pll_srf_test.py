import math_utils as mu
import math as m
import tranforms as tt
import pll_lib as pll
import filters as fi

filename = 'pll_srf.dat'
f_grid = 60.0
w_grid = 2 * m.pi * f_grid
Tpwm = 100e-6
V = 220

def plls_test_step(omega0: float = 2*m.pi*60, t1: float = 0.5, omega1: float = 2*m.pi*30, tf: float = 4.0):
    pllsrf = pll.PllSrf(Tpwm, 1.0, 1.0, w_grid)
    plljrm = pll.PllJrm(Tpwm, 240.0, 1800.0, w_grid)
    pllqt1 = pll.PllQT1(Tpwm, 57.0, w_grid)
    ws = omega0
    theta_grid = 0.0
    with open(filename, 'w') as f:
        f.write('#t u_g theta omega theta_srf theta_jrm\n')
        t = 0.0
        while t < tf:
            if t > t1:
                ws = omega1
            theta_grid += ws * Tpwm
            theta_grid = mu.cycle(theta_grid)
            v_a = mu.M_sqrt2f * V * m.cos(theta_grid)
            v_b = mu.M_sqrt2f * V * m.cos(theta_grid - mu.A120f)
            v_c = mu.M_sqrt2f * V * m.cos(theta_grid + mu.A120f)
            v_alpha, v_beta = tt.abc_to_alphabeta(v_a, v_b, v_c)
            pllsrf.step(v_alpha, v_beta)
            plljrm.step(v_alpha, v_beta)
            pllqt1.step(v_alpha, v_beta)
            err_srf = mu.mcycle(pllsrf.theta - theta_grid)
            err_jrm = mu.mcycle(plljrm.theta - theta_grid)
            err_qt1 = mu.mcycle(pllqt1.theta - theta_grid)
            print(f'{t} {v_a} {theta_grid} {err_srf} {pllsrf.omega} {err_jrm} {plljrm.omega} {ws} {err_qt1} {pllqt1.omega}', file=f)
            t += Tpwm
        print("Finished\n")


def plls_test_ramp(omega0: float = 2*m.pi*10, omegaf: float = 2*m.pi*1e3, tf: float = 4.0):
    pllsrf = pll.PllSrf(Tpwm, 1.0, 1.0, w_grid)
    plljrm = pll.PllJrm(Tpwm, 240.0, 1800.0, w_grid)
    pllqt1 = pll.PllQT1(Tpwm, 57.0, w_grid)
    theta_grid = 0.0
    with open(filename, 'w') as f:
        f.write('#t u_g theta omega theta_srf theta_jrm\n')
        t = 0.0
        while t < tf:
            ws = omega0 + (omegaf - omega0) / tf * t
            theta_grid += ws * Tpwm
            theta_grid = mu.cycle(theta_grid)
            v_a = mu.M_sqrt2f * V * m.cos(theta_grid)
            v_b = mu.M_sqrt2f * V * m.cos(theta_grid - mu.A120f)
            v_c = mu.M_sqrt2f * V * m.cos(theta_grid + mu.A120f)
            v_alpha, v_beta = tt.abc_to_alphabeta(v_a, v_b, v_c)
            pllsrf.step(v_alpha, v_beta)
            plljrm.step(v_alpha, v_beta)
            pllqt1.step(v_alpha, v_beta)
            err_srf = mu.mcycle(pllsrf.theta - theta_grid)
            err_jrm = mu.mcycle(plljrm.theta - theta_grid)
            err_qt1 = mu.mcycle(pllqt1.theta - theta_grid)
            print(f'{t} {v_a} {theta_grid} {err_srf} {pllsrf.omega} {err_jrm} {plljrm.omega} {ws} {err_qt1} {pllqt1.omega}', file=f)
            t += Tpwm
        print("Finished\n")


def test_mobavg(f: float, Tpwm: float, tf: float):
    size: int = int(1.0 / (f * Tpwm))
    maf = fi.MobAvg(size)
    omega = 2 * m.pi * f
    lpf1 = fi.DLPF(1 / omega, Tpwm)
    lpf2 = fi.DLPF(1 / (2 * omega), Tpwm)
    lpf3 = fi.DLPF(1 / (3 * omega), Tpwm)
    lpf5 = fi.DLPF(1 / (5 * omega), Tpwm)
    with open('mobavg_test.dat', 'w', ) as fo:
        fo.write(f'{0} {0} {0} {0} {0}\n')
        t: float = Tpwm
        while t < tf:
            # insert a unit step
            v = 1.0
            fo.write(f'{t} {maf.update_avg(v)} {lpf1.update(v)} {lpf2.update(v)} {lpf3.update(v)} {lpf5.update(v)} \n')
            t += Tpwm

