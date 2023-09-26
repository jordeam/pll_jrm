fn = 'pll_srf.dat'
plot \
     fn using 1:($4*100) with lines title '# err_{srf}', \
     fn using 1:5 with lines title 'w_{srf}', \
     fn using 1:($6*100) with lines lw 4 lt 1 title 'err_{jrm}', \
     fn using 1:7 with lines lw 4 title 'w_{jrm}', \
     fn using 1:8 with lines title 'ws', \
     fn using 1:($9*100) with lines title 'err_{QT1}', \
     fn using 1:10 with lines title 'w_{QT1}'
