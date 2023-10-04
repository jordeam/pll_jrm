set key bottom right
set xrange [0.7:1.5]
set yrange [0:]

set ylabel '$f(\hertz)$'
set xlabel '$t(\second)$'

fn = 'pll_test_step_60-30.dat'
plot \
     fn using 1:5 with lines title '$\hat\omega_{SRF}$', \
\
     fn using 1:7 with lines lw 4 title '$\hat\omega_{API}$', \
     fn using 1:8 with lines title '$\omega_{grid}$', \
     fn using 1:10 with lines title '$\hat\omega_{QT1}$'
