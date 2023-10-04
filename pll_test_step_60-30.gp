set key bottom right
set xrange [0:1]
set ylabel '$f(\hertz)$'
set xlabel '$t(\second)$'

set y2label '$\theta_{err}(\degree)$'

fn = 'pll_test_step-60-30.dat'
plot \
     fn using 1:($4*180/pi) with lines title '$\theta_{errSRF}$', \
     fn using 1:5 with lines title '$\hat\omega_{SRF}$', \
     fn using 1:($6*180/pi) with lines lw 4 lt 1 title '$\theta_{errAPI}$', \
     fn using 1:7 with lines lw 4 title '$\hat\omega_{API}$', \
     fn using 1:8 with lines title '$\hat\omega_{grid}$', \
     fn using 1:($9*180/pi) with lines title '$\theta_{errQT1}$', \
     fn using 1:10 with lines title '$\hat\omega_{QT1}$'
