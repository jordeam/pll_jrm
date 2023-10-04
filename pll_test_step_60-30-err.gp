set key bottom right

set xrange [0.7:1.5]
set ylabel '$\tilde\theta_{\square}(\unit\radian)$'
set xlabel '$t(\unit\second)$'

fn = 'pll_test_step_60-30.dat'

plot \
     fn using 1:($4*180/pi) with lines title '$\tilde\theta_{SRF}$', \
     fn using 1:($6*180/pi) with lines lw 4 lt 1 title '$\tilde\theta_{API}$', \
     fn using 1:($9*180/pi) with lines title '$\tilde\theta_{QT1}$'

# gp-debug: nil
