fn = 'pll_test_ramp5k.dat'
set ylabel '$f(\hertz)$'
set xlabel '$t(\second)$'
plot \
     fn using 1:($4*1) with lines title '$\epsilon_{SRF}$', \
     fn using 1:5 with lines title '$\hat\omega_{SRF}$', \
     fn using 1:($6*1) with lines lw 4 lt 1 title '$\epsilon_{API}$', \
     fn using 1:7 with lines lw 4 title '$\hat\omega_{API}$', \
     fn using 1:8 with lines title '$\omega_{grid}$', \
     fn using 1:($9*1) with lines title '$\epsilon_{QT1}$', \
     fn using 1:10 with lines title '$\hat\omega_{QT1}$'

# gp-size: 12cm,8cm
