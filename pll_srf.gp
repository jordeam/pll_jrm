fn = 'pll_srf.dat'
plot fn using 1:2 with lines title 'v_a', \
     fn using 1:($3*100) with lines title 'theta_{grid}', \
     fn using 1:($4*100) with lines title 'theta_{srf}', \
     fn using 1:5 with lines title 'w_{srf}', \
     fn using 1:($6*100) with lines title 'theta_{jrm}', \
     fn using 1:7 with lines title 'w_{jrm}', \
     fn using 1:8 with lines title 'ws'