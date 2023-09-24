fn = 'pll_srf.dat'
plot fn using 1:2 with lines title 'v_a', \
     fn using 1:($3*100) with lines title 'theta_{srf}', \
     fn using 1:4 with lines title 'w_{srf}', \
     fn using 1:($5*100) with lines title 'theta_{jrm}', \
     fn using 1:6 with lines title 'w_{jrm}'