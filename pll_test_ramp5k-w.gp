fn = 'pll_test_ramp5k.dat'
set ylabel '$f(\unit\hertz)$'
set xlabel '$t(\unit\second)$'
set key top left
plot \
     fn using 1:5 with lines title '$\hat\omega_{SRF}$', \
     fn using 1:7 with lines lw 4 title '$\hat\omega_{API}$', \
     fn using 1:8 with lines title '$\omega_{grid}$', \
     fn using 1:10 with lines title '$\hat\omega_{QT1}$'

# gp-size: 12cm,8cm
